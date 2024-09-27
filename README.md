# Open & Reproducible workflows in Earth Observation

Many cloud-based solutions for workflows in EO are available to users today, but only few support reproducibility or comply with the [OGC FAIR (findability, accessibility, interoperability, reusability)](https://www.ogc.org/blog-article/how-ogc-contributes-to-fair-geospatial-data/) data principles. 

This short tutorial demonstrates a solution that meets these requirements.

## Application Package reproducibility

### Personas

* **Alice** developed a Water Body detection Earth Observation application and package it as an EO Application Package
* **Bob** scripts the execution of application

### Scenario

Alice included in the water bodies detection Application Package software repository a Continuous Integration configuration relying on Github Actions to:

* build the containers
* push the built containers to Github container registry
* update the Application Package with these new container references
* push the updated Application Package to Github's artifact registry

Alice sent an email to Bob:

<hr>
from: alice@acme.io

to: bob@acme.io

subject: Detecting water bodies with NDWI and the Otsu threshold


Hi Bob!

check out my new Application Package for detecting water bodies using NDWI and the Ostu threshold.

I've ran it over our test site bounding box and preliminary result look promising.

The github repo is https://github.com/eoap/quickwin and I've just released version 1.0.0.

Let me know!

Cheers

Alice
<hr>

With this information, Bob scripts the Application Execution in a Jupyter Notebook.

His environment has a container runtime (e.g. podman or docker) and the `cwltool` CWL runner.

## Setting-up the environment on the AppHub Coder application

Clone this repo:

```
git clone https://github.com/eoap/open-reproducible-app-package
```

Click on `File` then `Open Folder...` and browser to the cloned directory `open-reproducible-app-package`

Go back to the terminal and create the Python environment with:

```
python -m venv env_reproducible_app
source env_reproducible_app/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name env_reproducible_app --display-name "env_reproducible_app"
```

## Execution

The execution is operated with the Jupyter Notebook `notebook.ipynb`. 

The webpage of the documentation is https://eoap.github.io/open-reproducible-app-package/. 

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)