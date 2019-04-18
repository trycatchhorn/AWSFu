#!/usr/bin/env bash

echo "Running python"
python main.py

# echo "Running python3"
# python3 main.py

find . -name "*.py~" -type f -delete
find . -name "*.pyc" -type f -delete
find . -name "*.sh~" -type f -delete
find . -name "__pycache__" -type d -delete


