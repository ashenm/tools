#!/usr/bin/env python3
# Build Jekyll Site

from re import sub
from os import P_WAIT, spawnlp
from subprocess import CalledProcessError, check_output
from datetime import datetime

try:
  sha256 = check_output([ 'git', 'rev-parse', 'HEAD' ]).decode().strip()
except CalledProcessError:
  sha256 = ''

with open('src/_includes/base.html', mode='r+t') as conffile:

  configuration = conffile.read()

  configuration = sub(r'<!-- macro/build: build-timestamp --!>', f'<meta name="build-timestamp" content="{datetime.utcnow().ctime()}" />', configuration)
  configuration = sub(r'<!-- macro/build: build-commit --!>', f'<meta name="build-commit" content="{sha256}" />', configuration)

  conffile.seek(0)
  conffile.write(configuration)

spawnlp(P_WAIT, 'bundle', 'bundle', 'exec', 'jekyll', 'build', '--profile')
