#!/bin/sh

set -e

version=$1
PYTHON=${PYTHON:-}

if [ -z "$PYTHON" ]; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
  else
    PYTHON=python
  fi
fi

if ! command -v "$PYTHON" >/dev/null 2>&1; then
  echo "Python interpreter not found. Install python3 or set PYTHON=/path/to/python."
  exit 1
fi

# check semver regex
if "$PYTHON" ./scripts/is_semver.py "$version" >/dev/null; then
  echo "$version"
  sed -i.bak "s/^version = .*/version = \"${version#v}\"/" pyproject.toml && rm -f pyproject.toml.bak
  git commit -am "Bump version to $version"
  git tag "$version"
else
  echo "Version \"$version\" does not satisfy semantic versioning requirements!"
  exit 2
fi
