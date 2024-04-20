#!/bin/bash

# Define the target path
target_path="C:\Users\Justin\DocumentsMy\_vue-nuxt\_web2.0"

# Check if the target path exists
if [ ! -d "$target_path" ]; then
  echo "Target path does not exist!"
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
