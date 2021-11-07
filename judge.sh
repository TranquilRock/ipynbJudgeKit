#!/bin/bash
rm "$1" || echo "No such file."
for filename in $(ls . | grep "ipynb"); do
    jupyter nbconvert --to python "$filename" --output "answer.py"
    python3 grading.py --n 12 --name "$filename" --output "$1" # --passonly 
# 3>&1 1>&2 2>&3
done
