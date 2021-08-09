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
<a href="https://doi.org/10.1101/2021.01.08.425840">
  <img src="http://img.shields.io/badge/DOI-10.1101/2021.01.08.425840-B31B1B.svg" alt="DOI:10.1101/2021.01.08.425840">
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
Authors: Sergio Pérez-Conesa and Lea Rems.
![](path_to_pic_no_tildes)

This project uses Bayesian Survival Analysis (PYMC3) to study the rate of membrane electroporation events. The first electroporation times are obtained from coarse-grained molecular dynamics simulations using realistic membrane compositions with a constant external electric field. The simulations were run by [prof. Lea Rems](https://scholar.google.com/citations?user=0pOfoCcAAAAJ&hl=en) and the bayesian inference by myself, Dr. [Sergio Pérez-Conesa](https://www.linkedin.com/in/sperezconesa/). All the explanations can be found in the article.

I am happy to connect and discuss this and other projects through [github](https://github.com/sperezconesa), [linkedin](https://www.linkedin.com/in/sperezconesa), [twitter](https://twitter.com/sperezconesa), [email](sperezconesa@gmail.com) etc.
Feel free to suggest ways we could have improved this code.

If you want to cite this work, please use CITE.bib, thank you!

Published Preprint:

Published Article:

## Running the code

The code is based on the jupyter notebooks. `` is used to convert the raw data into ``. Notebooks `` do the actual calculations.

### Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sperezconesa/electroporation_modeling/HEAD)

Try out [mybinder](https://mybinder.org/v2/gh/sperezconesa/electroporation_modeling/HEAD) to run the notebooks live on the cloud!

### Recreate conda environment

To recreate the conda environment used:

```bash
conda env create -f environment.yml
```

Use `environment_exact.yml` for the exact environment.

### Getting additional data files

Unfortunatelly we cannot share heavy files on github, but you can get them...

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
├── environment.yml   <- The necessary packages to install in conda environment.
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
- [ ] Make binder-friendly the notebooks.
- [ ] Make a version specific `environment_exact.yml`.
- [ ] `make format` and `make clean`.
- [x] Rewrite `README.md`.
- [x] Save notebooks with images.
- [ ] Add latex or word preprint document to reports.
- [ ] Update arxiv link.
- [ ] Update `CITE.bib`.
- [ ] Make repo for big files and link it in `README.md`.
- [x] Consider getting a DOI with Zenodo and add the Zenodo DOI badge.
- [ ] Can we reproduce the data.
- [x] Add github badges.
- [x] Update github and go public.
- [ ] Update article link.
- [ ] Remove references to external scripts.
