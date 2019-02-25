#!/usr/bin/env sh
# Build Project

set -e

. /home/travis/virtualenv/python3.7.2/bin/activate \
  && ./scripts/index.py \
  && ./scripts/build.py
