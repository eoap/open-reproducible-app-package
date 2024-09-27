# Backround

## Personas

The scenario described below is implemented using two distinct user personas:

* **Alice** developed a Water Body detection Earth Observation application and package it as an EO Application Package
* **Bob** scripts the execution of application

## Scenario

Alice included in the Water Body detection Application Package software repository a Continuous Integration configuration relying on Github Actions to:

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