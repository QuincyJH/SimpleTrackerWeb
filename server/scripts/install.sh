#!/bin/bash

function main() {
    pipenv install || handle_exception
}

function handle_exception() {
    echo "An error occurred while installing. Exiting..."
    exit 1
}

main