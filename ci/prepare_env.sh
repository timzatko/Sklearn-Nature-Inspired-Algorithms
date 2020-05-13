#!/usr/bin/env bash

python -m pip install --upgrade pip
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
echo "::add-path::$HOME/.poetry/bin"