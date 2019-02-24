#!/usr/bin/env python3
# Build Site

from os import P_WAIT, spawnlp, walk

spawnlp(P_WAIT, 'jekyll', 'jekyll', 'build')
