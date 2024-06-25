#!/bin/bash
## Shell script, that checks for venv and install requirements if needed, then laucnhed the APP.
## Written by RYUseless

CURRENT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd) # working dir
VENV_DIR="$CURRENT_DIR/.venv"  # venv path (where venv should be)
REQUIREMENTS_PATH="$CURRENT_DIR/requirements.txt" # path for requirements file

echo "Starting Script, checking for venv dir"

# Create new venv if there is not one already
if [ ! -d "$VENV_DIR" ]; then
    python -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
else
    source "$VENV_DIR/bin/activate"
fi

# Install requirements if the requirements.txt file exists
if [ -f "$REQUIREMENTS_PATH" ]; then
    pip install -r "$REQUIREMENTS_PATH"
fi
 
echo "Launching App"
python -m src.main

exit 0

# ------
# For debug etc, copy it above exit 0 somehwere where the script doesnt crash or shows signs of issues.
# ------
# echo "Working shell dir: $CURRENT_DIR"
