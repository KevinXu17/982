#!/bin/bash

# List of repository URLs
REPOS=("https://github.com/education/codespaces-project-template-js.git")

# Directory where repositories will be cloned
CLONE_DIR="/Users/kevinxu/Desktop/SFU/C982/pj/py/projects"

# Directory to store ESLint results
RESULTS_DIR="/Users/kevinxu/Desktop/SFU/C982/pj/py/results"

# Clone and run ESLint
for repo in "${REPOS[@]}"; do
    # Extracting repo name from URL
    REPO_NAME=$(basename "$repo" .git)

    # Clone the repository
    git clone "$repo" "$CLONE_DIR/$REPO_NAME"

    # Navigate to the repository directory
    cd "$CLONE_DIR/$REPO_NAME"

    # Install ESLint locally if needed
    # npm init -y
    # npm install eslint

    # Run ESLint and save results in JSON format
    npx standard --verbose > "$RESULTS_DIR/${REPO_NAME}.txt"
done
