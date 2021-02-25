#!/usr/bin/env python3
# Serve Site Locally

from os import P_WAIT, spawnlp

spawnlp(P_WAIT, 'bundle', 'bundle', 'exec', 'jekyll', 'serve', '--watch', '--port', '8080', '--host', '0.0.0.0')
