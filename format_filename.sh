#!/bin/bash
for filename in *.ipynb; do
    echo $filename
    mv "$filename" $(echo $filename | cut -c1-9)".ipynb"
done
