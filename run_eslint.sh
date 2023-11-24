#!/bin/bash

# List of repository URLs
REPOS=("https://github.com/education/codespaces-project-template-js.git" "https://github.com/education/autograding.git")

# Directory where repositories will be cloned
CLONE_DIR="/Users/kevinxu/Desktop/SFU/C982/pj/data/projects"

# Directory to store ESLint results
RESULTS_DIR="/Users/kevinxu/Desktop/SFU/C982/pj/data/infos"

# Clone and run ESLint
for repo in "${REPOS[@]}"; do
    # Extracting repo name from URL
    REPO_NAME=$(basename "$repo" .git)

    # Clone the repository
    git clone "$repo" "$CLONE_DIR/$REPO_NAME"

    # Navigate to the repository directory
    cd "$CLONE_DIR/$REPO_NAME"

    # Install ESLint locally if needed
    npm init -y
    npm install eslint

    # Run ESLint and save results in JSON format
    npx eslint . -f json > "$RESULTS_DIR/${REPO_NAME}_eslint_results.json"
done
