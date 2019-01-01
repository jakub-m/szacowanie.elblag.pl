#!/bin/bash

set -eux

rm -rfv docs/
mkdir -p docs
cp -rfv assets/* docs/
python3.6 generate.py
 
