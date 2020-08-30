#!/bin/bash

version=$1

if [ -n "$version" ]; then
  echo "$version"
  poetry version "$version"
  git commit -am "Bump version to $version"
  git tag "$version"
else
  echo "please specify a version!"
fi

