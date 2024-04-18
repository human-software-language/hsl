#!/bin/bash

# Get the list of commits for 'vscode_extension/src/extension.ts'
commit_hashes=$(git log --pretty=format:"%H" -- vscode_extension/build.js)

# Loop through each commit hash
for hash in $commit_hashes; do
  echo "Commit: $hash"
  echo "----------------------------------------"
  git show $hash:vscode_extension/build.js
  echo "----------------------------------------"
  echo ""
done
