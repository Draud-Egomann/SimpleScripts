#!/bin/bash

# Check if a target path argument is provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 <target_path>"
  exit 1
fi

# Get the target path from the first argument
target_path="$1"

# Check if the target path exists
if [ ! -d "$target_path" ]; then
  echo "Target path '$target_path' does not exist!"
  exit 1
fi

# Loop through each subdirectory in the target path
for dir in "$target_path"/*/; do
  if [ -d "$dir/.git" ]; then
    echo "Pulling changes in $dir"
    # Change directory and perform git pull
    (cd "$dir" && git pull)
  fi
done

echo "Git pull complete for all subdirectories in $target_path"
