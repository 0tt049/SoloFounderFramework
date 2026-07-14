#!/bin/bash

# Directory of the SoloFounderFramework repository
REPO_DIR="/home/otavio/.gemini/config/plugins/SoloFounderFramework"

cd "$REPO_DIR" || exit 1

# Check if there are any changes
if [[ -n $(git status -s) ]]; then
    # There are changes, let's commit and push
    git add .
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    git commit -m "chore(auto-sync): update library at $TIMESTAMP"
    git push origin master
fi
