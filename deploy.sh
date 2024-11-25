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
    twine upload --repository pypi dist/* --verbose
else
    echo "Uploading to TestPyPI..."
    twine upload --repository testpypi dist/* --verbose
fi
