#!/usr/bin/env python3
# Clean Build Artifacts

from os import P_WAIT, spawnlp

spawnlp(P_WAIT, 'jekyll', 'jekyll', 'clean', '--quiet')

spawnlp(P_WAIT, 'rm', 'rm', '--force', 'legend.html')
