#!/usr/bin/env python3
# Package Site

from tarfile import open
from os import scandir

with open('artifacts.tar.bz2', mode='w:bz2') as stream:

  for node in scandir('src'):
    stream.add(node.path, arcname=node.name, recursive=True)

  stream.add('_config.yml')

# vim: set expandtab shiftwidth=2:
