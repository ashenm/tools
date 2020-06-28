#!/usr/bin/env python3
# Clean Build Artifacts

from glob import iglob
from os import P_WAIT, remove, spawnlp

# clean generated icons
for icon in iglob('icons/*'):

  if icon.endswith('.svg'):
    continue

  remove(icon)

# clean jekyll build cache
spawnlp(P_WAIT, 'jekyll', 'jekyll', 'clean', '--quiet')

# remove generated index
spawnlp(P_WAIT, 'rm', 'rm', '--force', 'catalogue.html')
