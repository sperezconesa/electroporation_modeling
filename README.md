# Bayesian Survival Analysis of Electroporation Times from Molecular Dynamics
<div align="center"><p>
<a href="">
  <img src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</a>
<a href="">
  <img src="https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter" alt="Jupyter">
</a>
<a href="">
  <img src="https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white" alt="VIM">
</a>
<a href="https://www.linkedin.com/in/sperezconesa/">
  <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
</p>
</div>

<div align="center"><p>
<a href="https://mybinder.org/v2/gh/sperezconesa/electroporation_modeling/HEAD">
    <img title="Star on GitHub" src="https://mybinder.org/badge_logo.svg">
</a>
<a href="https://github.com/psf/black">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
</a>
<a href="https://lbesson.mit-license.org/">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT license">
</a>
<a href="https://doi.org/YYYYYY">
  <img src="http://img.shields.io/badge/DOI-YYYYY-B31B1B.svg" alt="DOI:YYYYY">
</a>
<a href="https://twitter.com/intent/follow?screen_name=sperezconesa">
  <img src="https://img.shields.io/twitter/follow/sperezconesa?style=social&logo=twitter" alt="follow on Twitter">
</a>
<a href="https://github.com/sperezconesa/electroporation_modeling">
    <img title="Star on GitHub" src="https://img.shields.io/github/stars/sperezconesa/electroporation_modeling.svg?style=social&label=Star">
</a>
</p>
</div>



------------
Authors: Sergio Pérez-Conesa, Lea Rems and Lucie Delemotte.
![](path_to_pic_no_tildes)

This project uses Bayesian Survival Analysis (PYMC3) to study the rate of membrane electroporation events. The first electroporation times are obtained from coarse-grained molecular dynamics simulations using realistic membrane compositions with a constant external electric field. The simulations were run by [prof. Lea Rems](https://scholar.google.com/citations?user=0pOfoCcAAAAJ&hl=en) and the bayesian inference by myself, Dr. [Sergio Pérez-Conesa](https://www.linkedin.com/in/sperezconesa/). We are both members of the [Delemottelab](https://github.com/delemottelab) led by [prof. Lucie Delemotte](https://www.biophysics.se/index.php/members/lucie-delemotte/). All the explanations can be found in the article and the rest of code and data [here](https://github.com/delemottelab/electroporation_MD-CG_machine_learning/blob/main/README.md)

I am happy to connect and discuss this and other projects through [github](https://github.com/sperezconesa), [linkedin](https://www.linkedin.com/in/sperezconesa), [twitter](https://twitter.com/sperezconesa), [email](sperezconesa@gmail.com) etc.
Feel free to suggest ways we could have improved this code.

If you want to cite this code, please use CITE.bib, thank you!

Published Preprint: [Identification of electroporation sites in the complex lipid organization of the plasma membrane](https://www.biorxiv.org/content/10.1101/2021.10.16.464625v1.abstract)

Published Article:

## Running the code

The code is based on the jupyter notebooks. `` is used to convert the raw data into ``. Notebooks `` do the actual calculations.

### Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sperezconesa/electroporation_modeling/HEAD)

Try out [my binder](https://mybinder.org/v2/gh/sperezconesa/electroporation_modeling/HEAD) to run the notebooks live on the cloud! It's free :wink:

Unfortunatelly, you can't train the models (too few memory on binder), but you can load them from the [OSF](https://osf.io/fv98a/) repostory and analyze them in my binder.

### Recreate conda environment

To recreate the conda environment used:

```bash
conda env create -f environment.yml
```

Use `environment_exact.yml` for the exact environment.

### Getting additional data files

All the data, including the inference models, simulations etc. can be found in [Open Software Foundation](https://osf.io/fv98a/).

## Project Organization

```text
├── LICENSE
│
├── Makefile           <- Makefile with commands like `make update_data` or `make format`
│
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── models             <- Learned models
│
├── notebooks          <- Jupyter notebooks.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   ├── final_figures  <- Generated graphics and figures to be used in final report.
│   └── docs           <- Generated LaTeX, pdf, word, powerpoint etc.
│
├── environment.yml    <- The necessary packages to install in conda environment.
│
├── environment_exact.yml   <- The exact package versions used.
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   └── data           <- Scripts to download or generate data
│
└──
```

------------

Project based on the [cookiecutter for Molecular Dynamics](https://github.com/sperezconesa/cookiecutter-md). Which is itself based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/) \#cookiecutterdatascience

------------

## To Do

- [x] Clean-up the repository of unused or WIP files.
- [x] Make binder-friendly the notebooks.
- [x] Make a version specific `environment_exact.yml`.
- [x] Remove references to external scripts.
- [x] Can we reproduce the data in another computer.
- [x] Rewrite `README.md`.
- [x] Save notebooks with images.
- [x] Add github badges.
- [x] Update github and go public.
- [x] Update arxiv link.
- [x] Update `CITE.bib` and doi badge.
- [ ] Make repo for big files and link it in `README.md`.
- [ ] Update article link and doi badge.
