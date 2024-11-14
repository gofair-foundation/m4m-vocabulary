# [M4M Vocabulary](http://m4m.gofairfoundation.nl/Skosmos/m4m)

Controlled vocabularies allow an accurate and controlled approach in describing physical and digital assets (e.g., data). One of such controlled vocabulary is **M4M Vocabulary**. This controlled vocabulary is produced in Metadata 4 Machine (M4M) Workshop.

`sheet2rdf` is used to build and serve **M4M Vocabulary**, while [PURL](https://archive.org/services/purl/) is used to persist identifiers for the vocabulary:

http://m4m.gofairfoundation.nl/Skosmos/m4m

# Tooling

## [![DOI](https://zenodo.org/badge/327900313.svg)](https://zenodo.org/badge/latestdoi/327900313) sheet2rdf

This repository hosts automatic workflow, executed by means of Github actions, and underlying shell and python scripts which:

- Fetches Google Sheet, containing the vocabulary terms and their defitions, from Google Drive and stores it as `xlsx` and `csv` files
- Converts fetched sheet to machine-actionable and FAIR RDF vocabulary using [xls2rdf](https://github.com/sparna-git/xls2rdf)
- Commits conversion results and tests logs to this repository
