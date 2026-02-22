# Contributing

## Contributing to code

### Local development

You will first need to clone the repository using git and place yourself in its directory:

```shell script
git clone git@github.com:timzatko/Sklearn-Nature-Inspired-Search.git
cd Sklearn-Nature-Inspired-Search
```

Create a virtual environment and install the package with dev dependencies:

```shell script
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Make sure that the tests are passing on your machine:

```shell script
python -m unittest tests
```

You can also run tests with test coverage and then print out the report.

```shell script
coverage run --source=./sklearn_nature_inspired_algorithms -m unittest tests
coverage report -m
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
2. Push the created commit and a tag
    ```shell script
    git push --tags
    ```
   This will trigger a pipeline which will make a draft release.
3. Publish the draft release, don't forget to edit release notes. Publishing the release will trigger the release pipeline which will publish the package to the [pypi](https://pypi.org) registry.
