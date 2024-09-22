#!/bin/bash

# Restore the old shell prompt
if [ -n "$OLD_VIRTUAL_PROMPT" ]; then
    export PS1="$OLD_VIRTUAL_PROMPT"
    unset OLD_VIRTUAL_PROMPT
fi

# Restore the old Python home
if [ -n "$OLD_VIRTUAL_PYTHONHOME" ]; then
    export PYTHONHOME="$OLD_VIRTUAL_PYTHONHOME"
    unset OLD_VIRTUAL_PYTHONHOME
fi

# Restore the old PATH
if [ -n "$OLD_VIRTUAL_PATH" ]; then
    export PATH="$OLD_VIRTUAL_PATH"
    unset OLD_VIRTUAL_PATH
fi

# Clear virtual environment variables
unset VIRTUAL_ENV
unset VIRTUAL_ENV_PROMPT

# End of script