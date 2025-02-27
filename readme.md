# Adomi-IO - Magic Mirror

## Overview

Magic Mirror is an automation tool designed to sync a source GitHub repository with a destination repository. 
This ensures that the latest updates from the source repository are copied and committed to the destination repository.

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
  -e REPO_SOURCE=https://github.com/owner_name_here/repo_name_here.git \
  -e REPO_DESTINATION=https://github.com/owner_name_here/repo_name_here.git \
  -e GH_TOKEN=<your-github-api-key> \
  -e BRANCH=master \
  ghcr.io/adomi-io/magic-mirror:latest
```

Alternatively, you can create a `.env` file with the required environment variables and run the container as follows:

```bash
docker run --rm --env-file .env ghcr.io/adomi-io/magic-mirror:latest
```

## Troubleshooting

- **Authentication Issues**: Ensure that API keys have the correct repository permissions.
- **Permission Denied**: Verify that API keys grant write access to the destination repository.
- **No Changes Detected**: Ensure that the source repository has new commits available for syncing.

## Contributing

We welcome contributions! Feel free to submit pull requests to enhance functionality, improve security, or add new features. 
Your feedback and suggestions are always appreciated.


