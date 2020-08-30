# Contributing

## Contributing to code

### Local development

You will first need to clone the repository using git and place yourself in its directory:

```shell script
git clone git@github.com:timzatko/Sklearn-Nature-Inspired-Search.git
cd Sklearn-Nature-Inspired-Search
```

You need to install [Poetry](https://python-poetry.org/docs/#introduction) on your local machine. They execute the following commands within the project directory. Make sure that the tests are passing on your machine. 

```shell script
poetry install
poetry run python -m unittest tests
```

You can also run tests with test coverage and then print out the report.

```shell script
poetry run coverage run --source=./sklearn_nature_inspired_algorithms -m unittest tests
poetry run coverage report -m
```

### Branching strategy

This repository follows _trunk based development branching strategy_. You can read more about it [here](https://trunkbaseddevelopment.com/).

## Releasing

Use [semantic versioning](https://semver.org/) for versions.

### Bump version

1. Bump version with
    ```shell script
    sh ./version.sh v0.1.1
    ```
1. Push the created commit and a tag 
    ```shell script
    git push --tags
    ```
   This will trigger a pipeline which will make a draft release.
1. Publish the draft release, don't forget to edit release notes. Publishing the release will trigger the release pipeline which will publish the package to the [pypi](pypi.org) registry. 
   
