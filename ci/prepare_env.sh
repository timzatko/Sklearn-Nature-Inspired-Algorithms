#!/usr/bin/env bash

python -m pip install --upgrade pip
curl -sSL https://install.python-poetry.org | python3 -
echo "$HOME/.poetry/bin" >> "$GITHUB_PATH"
