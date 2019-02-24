#!/usr/bin/env python3
# Serve Site Locally

from os import P_NOWAIT, spawnlp

print(spawnlp(P_NOWAIT, 'jekyll', 'jekyll', 'serve', '--watch', '--quiet', '--port', '8080', '--host', '0.0.0.0'))
