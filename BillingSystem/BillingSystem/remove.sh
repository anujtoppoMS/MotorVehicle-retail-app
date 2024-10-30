#!/bin/bash

# Define the directory and file type
DIRECTORY="/home/sheelu/MyProjects/BillingSystem/"
FILE_TYPE="*.Identifier"  # Change this to the file type you want to delete

# Find and delete the files
find "$DIRECTORY" -type f -name "$FILE_TYPE" -exec rm -f {} \;

echo "All $FILE_TYPE files have been deleted from $DIRECTORY and its subdirectories."
