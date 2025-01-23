#!/bin/bash

# Print start message
echo "Starting cleanup..."

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete

# Remove Jupyter notebook checkpoints
find . -type d -name ".ipynb_checkpoints" -exec rm -r {} +

# Remove temporary files
find . -type f -name "*~" -delete
find . -type f -name ".DS_Store" -delete

# Remove logs and temporary files
find . -type f -name "*.log" -delete
find . -type f -name "*.tmp" -delete

# Remove build and distribution directories
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# Print completion message
echo "Cleanup completed!"
echo "Removed:"
echo "- Python cache files (__pycache__, .pyc, .pyo, .pyd)"
echo "- Jupyter notebook checkpoints"
echo "- Temporary files and logs"
echo "- Build and distribution directories"
