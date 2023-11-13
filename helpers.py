from cwl_utils.parser import load_document_by_uri
import cwl_utils
import os
from typing import Any, Dict, Optional, List
from pydantic import BaseModel, DirectoryPath
from pydantic.fields import ModelField, FieldInfo
import json
import requests

import pystac
import stac_asset
import asyncio
from pathlib import PosixPath

os.environ["GH_PAT"] = "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"
def get_release_assets(
    user="Terradue", repo="app-package-training-bids23", token="", page=1
):
    pat = token
    result = {}

    response = requests.get(
        f"https://api.github.com/repos/{user}/{repo}/releases?per_page=100&page={page}",
        headers={"Authorization": "token " + pat},
    )
    for release in response.json():

        local_assets = []

        for asset in release["assets"]:
            cwl_obj = load_document_by_uri(asset["browser_download_url"])
            local_assets.append(
                {
                    "url": asset["browser_download_url"],
                    "cwl": cwl_obj,
                    "label": cwl_obj.label,
                    "doc": cwl_obj.doc,
                }
            )

        result[release["tag_name"]] = local_assets

    return result


def my_dumps(v, *, default):
    for key, value in v.items():
        if isinstance(value, PosixPath):
            v[key] = {"class": "Directory", "path": str(value)}
        else:
            v[key] = value
    return json.dumps(v)


class Params(BaseModel):
    @classmethod
    def set_fields(cls, **field_definitions: Any):

        cls.__fields__ = {}

        new_fields: Dict[str, ModelField] = {}
        new_annotations: Dict[str, Optional[type]] = {}

        for f_name, f_def in field_definitions.items():
            if isinstance(f_def, tuple):
                try:
                    f_annotation, f_value = f_def
                except ValueError as e:
                    raise Exception(
                        "field definitions should either be a tuple of (<type>, <default>) or just a "
                        "default value, unfortunately this means tuples as "
                        "default values are not allowed"
                    ) from e
            else:
                f_annotation, f_value = None, f_def

            if f_annotation:
                new_annotations[f_name] = f_annotation

            new_fields[f_name] = ModelField.infer(
                name=f_name,
                value=f_value,
                annotation=f_annotation,
                class_validators=None,
                config=cls.__config__,
            )

            new_fields[f_name].field_info = FieldInfo(title="aaa", description="bbb")
        cls.__fields__.update(new_fields)

    @classmethod
    def clear_fields(cls):

        cls.__fields__ = {}

    @classmethod
    def get_fields(cls):

        return cls.__fields__
    
    class Config:
        json_dumps = my_dumps


def get_param_model_fields(cwl_obj):
    fields = {}

    for inp in cwl_obj.inputs:
        key = os.path.basename(inp.id)
        if inp.type_ == "string":
            input_type = str
        if inp.type_ == "Directory":
            input_type = DirectoryPath
        if isinstance(inp.type_, cwl_utils.parser.cwl_v1_0.InputArraySchema):
            if inp.type_.items == "string":
                input_type = List[str]
            else:
                input_type = List
        if not inp.default:
            fields[key] = (input_type, ...)
        else:
            fields[key] = (input_type, inp.default, FieldInfo(title=inp.label, description=inp.doc)
    return fields


async def stage_in(stac_item, target_dir="."):

    config = stac_asset.Config(warn=True)

    os.makedirs(os.path.join(target_dir, stac_item.id), exist_ok=True)
    cwd = os.getcwd()

    os.chdir(os.path.join(target_dir, stac_item.id))
    item = await stac_asset.download_item(item=stac_item, directory=".", config=config)
    os.chdir(cwd)

    cat = pystac.Catalog(
        id="catalog",
        description=f"catalog with staged {item.id}",
        title=f"catalog with staged {item.id}",
    )
    cat.add_item(item)

    cat.normalize_hrefs(target_dir)
    cat.save(catalog_type=pystac.CatalogType.SELF_CONTAINED)

    return cat
