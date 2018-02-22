#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Illegal number of arguments"
    echo "Usage: $0 input_directory"
    exit 1
fi

echo "NOTE! passing directory format should be like: /path/to/folder/"
dir=${PWD}
INPUT_DIR=$1

#creating virtual environment
virtualenv ENV
source ENV/bin/activate

export PYTHONPATH="$(dirname "$dir")"
pip3.6 install -r "$dir/requirements.txt"

python3.6 parser.py $INPUT_DIR

echo "Done!"
