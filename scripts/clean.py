#!/usr/bin/env python3
# Clean Build Artifacts

from glob import iglob
from os import P_WAIT, remove, spawnlp

# build artifacts
artifacts = [
  'artifacts.list',
  'artifacts.tar.bz2',
  'src/catalogue.html',
]

# clean generated icons
for icon in iglob('src/icons/*'):

  if icon.endswith('.svg'):
    continue

  remove(icon)

# clean jekyll build cache
spawnlp(P_WAIT, 'jekyll', 'jekyll', 'clean', '--quiet')

# remove generated files
spawnlp(P_WAIT, 'rm', 'rm', '--force', *artifacts)
