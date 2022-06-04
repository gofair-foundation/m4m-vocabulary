<img src="https://thumb.tildacdn.com/tild3934-3732-4633-b864-646466363531/-/format/webp/FAIRware_Logo.jpg" alt="incentive logo" height="75"/>

[![CI](https://github.com/fair-data-collective/M4M-21-FAIRware-Neuroscience-Subjects/workflows/Sheet2RDF/badge.svg)](https://github.com/fair-data-collective/M4M-21-FAIRware-Neuroscience-Subjects/actions?query=workflow%3ASheet2RDF)

# [Neuroscience Subjects](http://purl.org/m4m21/subjects/)

Controlled vocabularies allow an accurate and controlled approach in describing physical and digital assets (e.g., data). One of such controlled vocabulary is **Neuroscience Subjects**. This controlled vocabulary is produced in Metadata 4 Machine (M4M) Workshop 21 (M4M.21 FAIRware Neuroscience), which is one of deliverables of [FAIRware project](https://researchonresearch.org/projects#!/tab/273951116-3) funded by [RoRi](https://researchonresearch.org/).

`sheet2rdf` is used to build and serve **Neuroscience Subjects**, while [PURL](https://archive.org/services/purl/) is used to persist identifiers for the vocabulary, which resolve on [BioPortal](bioportal.bioontology.org/) (Stanford's ontology service):

http://purl.org/m4m21/subjects/

# Tooling

## [![DOI](https://zenodo.org/badge/327900313.svg)](https://zenodo.org/badge/latestdoi/327900313) sheet2rdf

This repository hosts automatic workflow, executed by means of Github actions, and underlying shell and python scripts which:

- Fetches Google Sheet, containing the vocabulary terms and their defitions, from Google Drive and stores it as `xlsx` and `csv` files
- Converts fetched sheet to machine-actionable and FAIR RDF vocabulary using [xls2rdf](https://github.com/sparna-git/xls2rdf)
- Tests the resulting RDF vocabulary using [qSKOS](https://github.com/cmader/qSKOS/)
- Commits conversion results and tests logs to this repository
