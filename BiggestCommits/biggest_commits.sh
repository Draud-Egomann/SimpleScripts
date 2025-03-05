#!/bin/bash

# Ensure the script is run inside a Git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "This is not a Git repository."
    exit 1
fi

echo "Finding the 10 biggest commits by size..."

git log --pretty=format:"%H %an %s" --numstat | awk '
    /^[0-9]/ {added += $1} 
    /^[0-9]/ {removed += $2} 
    /^[a-f0-9]/ {if (commit) print commit, author, added + removed; commit=$1; author=$2; added=0; removed=0} 
    END {if (commit) print commit, author, added + removed}
' | sort -k3 -nr | head -n 10
