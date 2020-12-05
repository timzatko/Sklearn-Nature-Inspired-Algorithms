#!/usr/bin/env bash

python -m pip install --upgrade pip
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
echo "$HOME/.poetry/bin" >> "$GITHUB_PATH"
