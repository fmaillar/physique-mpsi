#!/bin/bash

for py_file in $(find -name *.py)
do
    python3 py_file
done
