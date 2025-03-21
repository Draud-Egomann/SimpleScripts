# Backup Source Code

This folder contains scripts to back up your source code by either compressing it into a zip file or pushing it to a remote Git server.

## Scripts

### 1. `toZip.py`

A Python script that zips a specified folder while skipping unnecessary directories.

#### Prerequisites

- Python 3.x

#### Usage

Run the script with:

```bash
python toZip.py
```

- Ensure the `FOLDER_NAME` variable in the script is set to the folder you want to back up.
- The zip file will be created in the current directory with a timestamped name.

#### Notes

- The script skips common directories like `.git`, `node_modules`, and `__pycache__`.
- Ensure the folder to be zipped exists in the current directory.

---

### 2. `toRemoteGitServer.py`

A Python script that pushes the current branch of a local Git repository to a specified remote Git server.

#### Prerequisites

- Python 3.x
- Git installed on your system

#### Usage

Run the script with:

```bash
python toRemoteGitServer.py
```

- Ensure the `FOLDER_NAME` variable in the script is set to the folder containing the Git repository.
- Configure the `REMOTE_SSH` or `REMOTE_HTTPS` variable with your remote repository URL.
- The script will temporarily add a remote, push the current branch, and then remove the remote.

#### Notes

- The script checks if the folder is a valid Git repository before proceeding.
- Ensure you have the necessary permissions to push to the remote repository.

---

## Important Notes

- Both scripts are designed to be run from the folder containing them.
- Modify the configuration variables (`FOLDER_NAME`, `REMOTE_SSH`, etc.) in the scripts as needed.
- For large repositories or folders, the operations may take some time.
