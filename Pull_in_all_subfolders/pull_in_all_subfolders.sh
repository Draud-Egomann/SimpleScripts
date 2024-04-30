#!/bin/bash

# Function to display usage information
usage() {
  echo "Usage: $0 <target_path> [depth]"
}

# Check if target path argument is provided
if [ $# -eq 0 ]; then
  usage
  exit 1
fi

# Get the target path from the first argument
target_path="$1"
# Default depth is 1
depth=1

# Check if depth argument is provided
if [ $# -gt 1 ]; then
  # Validate if depth is a positive integer
  if ! [[ $2 =~ ^[1-9][0-9]*$ ]]; then
    echo "Depth argument must be a positive integer."
    usage
    exit 1
  fi
  depth=$2
fi

# Check if the target path exists
if [ ! -d "$target_path" ]; then
  echo "Target path '$target_path' does not exist!"
  exit 1
fi

# Function to recursively pull changes in subdirectories up to the specified depth
pull_changes() {
  local current_dir="$1"
  local current_depth=$2

  if [ $current_depth -gt 0 ]; then
    for dir in "$current_dir"/*/; do
      if [ -d "$dir/.git" ]; then
        echo "Pulling changes in $dir"
        # Change directory and perform git pull
        (cd "$dir" && git pull)
      fi
      # Recursive call to process subdirectories
      pull_changes "$dir" $((current_depth - 1))
    done
  fi
}

# Call function to pull changes in subdirectories
pull_changes "$target_path" $depth

echo "Git pull complete for all subdirectories in $target_path up to depth $depth"