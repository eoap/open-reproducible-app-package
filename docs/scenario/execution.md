# Execution

Bob's environment has a container runtime (e.g. `podman` or `docker`) and the `cwltool` CWL runner.

## Setting-up the environment on the AppHub Coder application

Firstly, clone this repo:

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