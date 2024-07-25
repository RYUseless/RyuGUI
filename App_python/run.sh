#!/bin/bash
## Shell script, that checks for venv and install requirements if needed, then starts the APP.
## Written by RYUseless

CURRENT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd) # working dir
VENV_DIR="$CURRENT_DIR/.venv"  # venv path (where venv should be)
REQUIREMENTS_PATH="$CURRENT_DIR/requirements.txt" # path for requirements file

echo "Starting Script, checking for venv dir"

# go to program directory.
cd "$CURRENT_DIR" || { echo "Failed to cd to $CURRENT_DIR"; exit 1; }

# Function to install requirements in the background
install_requirements() {
    if [ -f "$REQUIREMENTS_PATH" ]; then
        echo "Installing requirements..."
        pip install -r "$REQUIREMENTS_PATH"
        echo "Requirements installed."
    else
        echo "No requirements.txt file found."
    fi
}

# Create new venv if there is not one already
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    install_requirements &
else
    source "$VENV_DIR/bin/activate"
    # Check if requirements are already installed by verifying a common package
    if ! pip show -q some-common-package; then
        install_requirements &
    else
        echo "Requirements already installed."
    fi
fi

echo -e "\n--- Starting the application ---"
python -m src.main # start the app


exit 0

