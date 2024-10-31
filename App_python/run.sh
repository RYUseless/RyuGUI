#!/bin/bash
## Shell script that checks for venv and installs requirements if needed, then starts the APP.
## Written by RYUseless

CURRENT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd) # working dir
VENV_DIR="$CURRENT_DIR/.venv"  # venv path (where venv should be)
REQUIREMENTS_PATH="$CURRENT_DIR/requirements.txt" # path for requirements file

echo "Starting Script, checking for venv dir"

# Go to program directory.
cd "$CURRENT_DIR" || { echo "Failed to cd to $CURRENT_DIR"; exit 1; }

# Create new venv if there is not one already
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Function to check and install requirements if necessary
install_requirements_if_needed() {
    if [ -f "$REQUIREMENTS_PATH" ]; then
        echo "Checking requirements..."

        # Get a list of installed packages and their versions
        installed_packages=$(pip freeze)

        # Read the requirements.txt into a variable
        required_packages=$(cat "$REQUIREMENTS_PATH")

        # Function to determine if the installed packages are up to date
        packages_need_update=false

       while IFS= read -r line; do
    	# Extraxting requirements.txt and splitting it into version, sadly it still does work only with ==
    	required_name=$(echo "$line" | sed 's/[=><][^=><]*$//')
    	required_version=$(echo "$line" | sed -e 's/^[^=><]*[=><]//')


    	installed_version=$(echo "$installed_packages" | grep "^$required_name" | sed -e 's/^[^=><]*[=><]//')

    	# Find missing and outdated packages
    	if [ -z "$installed_version" ]; then
        	packages_need_update=true
        	echo "$required_name is not installed."
    	elif [ "$installed_version" != "$required_version" ]; then
        	packages_need_update=true
        	echo "$required_name is outdated. Installed: $installed_version, Required: $required_version."
    	fi
        done <<< "$required_packages"

        # ONLY IF NEEDED install packages for the app
        if [ "$packages_need_update" = true ]; then
            echo "Installing or updating requirements..."
            pip install -r "$REQUIREMENTS_PATH"
            echo "Requirements installed/updated."
        else
            echo "All requirements are up to date."
        fi

    else
        echo "No requirements.txt file found."
    fi
}

# launch the install req IF NEEDED
install_requirements_if_needed

echo -e "\n--- Starting the application ---"
# Start the app itself -- python
python -m src.main

exit 0







