#!/usr/bin/env sh
# Build Project

set -e

# build jekyll site
. /home/travis/virtualenv/python3.7.6/bin/activate \
  && ./scripts/index.py \
  && ./scripts/build.py

# list artifacts for cache purging
find _site -type f -printf 'https://tools.ashenm.ml/%P\n' \
  | jq --raw-input --slurp 'split("\n") | { files: .[:-1] }' \
  | tee '.artifacts'
