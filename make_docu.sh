#!/usr/bin/env bash
rm docs/rst/*.rst
sphinx-apidoc -F -f -o docs/rst  scripts
cp docs/rst/modules.rst docs/rst/index.rst
cp docs/conf.py docs/rst/conf.py
sphinx-build -b html docs/rst/ docs/html/