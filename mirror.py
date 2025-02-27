#!/usr/bin/env python3

import sys
import os
import shutil
import subprocess
from datetime import datetime
import logging

from dotenv import load_dotenv

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

load_dotenv()

REPO_SOURCE = os.environ.get("REPO_SOURCE")
REPO_DESTINATION = os.environ.get("REPO_DESTINATION")
GH_TOKEN = os.environ.get("GH_TOKEN")
BRANCH = os.environ.get("BRANCH", "master")

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "./output")

if not REPO_SOURCE or not REPO_DESTINATION:
    raise Exception("Missing REPO_SOURCE/REPO_DESTINATION env vars")

def run_cmd(cmd, cwd=None):
    subprocess.run(cmd, check=True, cwd=cwd)

if __name__ == "__main__":
    repo_destination_url = REPO_DESTINATION
    repo_destination_local_path = os.path.join(OUTPUT_PATH, 'destination')

    # Configure git
    logging.info("Configuring git.")
    run_cmd(["gh", "auth", "setup-git"])

    # Clone the source repository
    logging.info("Cloning source repository.")

    run_cmd([
        "git", "clone",
        "--single-branch",
        "--branch", BRANCH,
        REPO_SOURCE,
        OUTPUT_PATH
    ])

    # Map the origin to the new repo
    logging.info(f"Setting origin to {REPO_DESTINATION}.")

    run_cmd(
        ["git", "remote", "set-url", "origin", REPO_DESTINATION],
        cwd=OUTPUT_PATH
    )

    # Push the changes to the new repo
    logging.info(f"Pushing branch '{BRANCH}' to the destination repository.")

    run_cmd(
        ["git", "push", "-u", "origin", BRANCH, '-f'],
        cwd=OUTPUT_PATH
    )

    # Changes have been synced to the destination repository
    logging.info("Repositories have been successfully synchronized. Done!")
