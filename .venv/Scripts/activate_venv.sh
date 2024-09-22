#!/bin/bash

# Save the old locale to restore later
OLD_LANG=$LANG
OLD_LC_ALL=$LC_ALL

# Set UTF-8 encoding (should already be the default in most cases)
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Path to your virtual environment
VIRTUAL_ENV="/Users/carlo/PennApps/.venv"

# Update the PATH and prompt to indicate the virtual environment is active
if [ -z "$OLD_VIRTUAL_PROMPT" ]; then
    OLD_VIRTUAL_PROMPT=$PS1
fi

export PS1="(.venv) $PS1"

if [ -n "$VIRTUAL_ENV" ]; then
    export PATH="$VIRTUAL_ENV/bin:$PATH"
fi

# Function to deactivate the virtual environment and restore settings
deactivate() {
    if [ -n "$OLD_VIRTUAL_PROMPT" ]; then
        export PS1=$OLD_VIRTUAL_PROMPT
        unset OLD_VIRTUAL_PROMPT
    fi

    if [ -n "$OLD_LANG" ]; then
        export LANG=$OLD_LANG
        unset OLD_LANG
    fi

    if [ -n "$OLD_LC_ALL" ]; then
        export LC_ALL=$OLD_LC_ALL
        unset OLD_LC_ALL
    fi

    if [ -n "$OLD_VIRTUAL_PATH" ]; then
        export PATH=$OLD_VIRTUAL_PATH
        unset OLD_VIRTUAL_PATH
    fi

    unset VIRTUAL_ENV
}

# Uncomment this line to automatically deactivate when the script exits
# trap deactivate EXIT