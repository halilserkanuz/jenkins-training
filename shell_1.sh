#!/bin/bash

# Attempt to copy a file
cp missingfile.txt /tmp

# Check the exit status of the `cp` command
if [ $? -eq 0 ]; then
    echo "The file was copied successfully."
else
    echo "The file could not be copied."
fi