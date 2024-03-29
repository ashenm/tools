#!/usr/bin/env python3
#
# Generates favicon.ico from favicon.svg
#
# Ashen Gunaratne
# mail@ashenm.dev
#

from glob import iglob
from os.path import splitext
from PIL import Image
from cairosvg import svg2png

for icon in iglob('src/icons/*.svg'):

  root, ext = splitext(icon)

  # generate png
  # https://cairosvg.org/documentation/index.html#python
  svg2png(url=icon, output_width=256, output_height=256, write_to=f'{root}.png')

  # generate ico
  # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#ico
  Image.open(f'{root}.png').save(f'{root}.ico', format='ico')

# vim: set expandtab shiftwidth=2 syntax=python:
