#!/bin/bash

version=$1

# check semver regex
if [[ $(python ./scripts/is_semver.py $version) == "true" ]]; then
  echo "$version"
  poetry version "$version"
  git commit -am "Bump version to $version"
  git tag "$version"
else
  echo "Version \"$version\" does not satisfy semantic versioning requirements!"
  exit 2
fi

