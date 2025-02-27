# Adomi-IO - Magic Mirror

## Overview

Magic Mirror is an automation tool designed to sync a source GitHub repository with a destination repository. 
This ensures that the latest updates from the source repository are copied and committed to the destination repository.

## Features

- **Automated Cloning**: Fetches both the source and destination repositories automatically.
- **Efficient File Merging**: Copies only necessary files while excluding unnecessary ones like `.git`.
- **Automated Commit & Push**: Detects changes, commits with a timestamped message, and pushes updates to the destination repository.

## Running with Docker

We provide a pre-built Docker container hosted on GitHub Container Registry, making it easy to deploy and execute.

### Pull the Latest Image

```bash
docker pull ghcr.io/adomi-io/magic-mirror:latest
```

### Run the Container

Execute the following command to start the sync process:

```bash
docker run --rm \
  -e REPO_SOURCE=<your-source-repo> \
  -e REPO_DESTINATION=<your-destination-repo> \
  -e API_KEY=<your-github-api-key> \
  -e SOURCE_API_KEY=<optional-source-api-key> \
  -e DESTINATION_API_KEY=<optional-destination-api-key> \
  -e BRANCH=master \
  ghcr.io/adomi-io/magic-mirror:latest
```

Alternatively, you can create a `.env` file with the required environment variables and run the container as follows:

```bash
docker run --rm --env-file .env ghcr.io/adomi-io/magic-mirror:latest
```

## How It Works

1. **Cloning Repositories**: The script clones both the source and destination repositories into the `OUTPUT_PATH` directory.
2. **File Synchronization**: Source files (excluding `.git`) are copied into a merged directory.
3. **Change Detection**: The script checks for modifications in the merged folder.
4. **Automated Commit & Push**: If changes are found, they are committed with a timestamped message and pushed to the destination repository.

## Troubleshooting

- **Authentication Issues**: Ensure that API keys have the correct repository permissions.
- **Permission Denied**: Verify that API keys grant write access to the destination repository.
- **No Changes Detected**: Ensure that the source repository has new commits available for syncing.

## Contributing

We welcome contributions! Feel free to submit pull requests to enhance functionality, improve security, or add new features. 
Your feedback and suggestions are always appreciated.

## License

This project is licensed under the **MIT License**.

