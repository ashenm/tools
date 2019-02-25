#!/usr/bin/env python3
# Build Jekyll Site

from os import P_WAIT, spawnlp

spawnlp(P_WAIT, 'jekyll', 'jekyll', 'build')
