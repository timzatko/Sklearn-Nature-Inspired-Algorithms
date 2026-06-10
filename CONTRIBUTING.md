# Contributing

## Contributing to code

### Local development

First, clone the repository with Git and move into its directory:

```shell script
git clone git@github.com:timzatko/Sklearn-Nature-Inspired-Algorithms.git
cd Sklearn-Nature-Inspired-Algorithms
```

Create a virtual environment and install the package with dev dependencies:

```shell script
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Make sure the tests pass on your machine:

```shell script
python -m unittest tests
```

You can also run the tests with coverage and print the report:

```shell script
coverage run --source=./sklearn_nature_inspired_algorithms -m unittest tests
coverage report -m
```

### Branching strategy

This repository follows a _trunk-based development_ branching strategy. You can read more about it [here](https://trunkbaseddevelopment.com/).

## Releasing

Use [semantic versioning](https://semver.org/) for releases.

### Bump version

1. Bump the version:
    ```shell script
    sh ./version.sh v0.1.1
    ```
2. Push the generated commit and tag:
    ```shell script
    git push --tags
    ```
   This triggers a pipeline that creates a draft release.
3. Edit the release notes and publish the draft release. Publishing the release triggers the release pipeline, which publishes the package to the [PyPI](https://pypi.org) registry.
