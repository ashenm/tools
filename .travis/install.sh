#!/usr/bin/env sh
# Configure Build Environment

set -e

# install jekyll
sudo apt update \
  && sudo apt install --no-install-recommends ruby-dev \
  && sudo gem install --no-ri --no-rdoc jekyll

# install python 3.7.2
curl --silent --show-error --location --output /tmp/python-3.7.2.tar.bz2 \
    --url https://s3.amazonaws.com/travis-python-archives/binaries/ubuntu/16.04/x86_64/python-3.7.2.tar.bz2 \
  && sudo tar --extract --bzip2 --file /tmp/python-3.7.2.tar.bz2 --directory /

# install python dependencies
. /home/travis/virtualenv/python3.7.2/bin/activate \
  && pip3 install --upgrade --requirement requirements.txt
