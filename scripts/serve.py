#!/usr/bin/env python3
# Serve Site Locally

from os import P_WAIT, spawnlp

print(spawnlp(P_WAIT, 'jekyll', 'jekyll', 'serve', '--watch', '--quiet', '--port', '8080', '--host', '0.0.0.0'))
