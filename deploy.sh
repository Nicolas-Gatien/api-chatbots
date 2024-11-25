#!/bin/bash

# Clean up any previous builds
rm -rf dist/
rm -rf build/
rm -rf *.egg-info

# Create new distribution packages
python -m build

# Check if we want to upload to PyPI or TestPyPI
if [ "$1" = "prod" ]; then
    echo "Uploading to PyPI..."
    python -m twine upload --repository pypi dist/*
else
    echo "Uploading to TestPyPI..."
    python -m twine upload --repository testpypi dist/*
fi
