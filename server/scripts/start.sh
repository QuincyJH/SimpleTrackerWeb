#!/bin/bash

function main() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
        VENV_PATH=$(pipenv --venv)/Scripts/activate
    else
        VENV_PATH=$(pipenv --venv)/bin/activate
    fi

    source $VENV_PATH
    uvicorn app.main:app --reload
}
function handle_exception() {
    echo "An error occurred while starting. Exiting..."
    exit 1
}

main