# Pull in all Subfolders

This script automates the process of performing a `git pull` in all subdirectories of a specified target path.

## How to Use

1. **Download the Script**: Download the script and save it to your local machine.
2. **Modify the Script (Optional)**: Open the script in a text editor and update the `target_path` variable with the path to the directory containing the subfolders you want to pull from.
3. **Run the Script**: Execute the script by running the following command in bash:

   ```bash
    sh pull_from_all_git_repos.sh
   ```

- On Windows:

   ```powershell
    bash .\pull_in_all_subfolders.sh
   ```

## Note

- This script assumes that Git is installed on your system and that you have appropriate permissions to perform `git pull` in the specified directories.
- Ensure that the target path provided in the script points to the correct directory containing the subfolders you want to update.

## Example

Suppose you have a directory structure as follows:

```
parent_directory/
│
├── subfolder1/
│   ├── .git/
│   └── files...
│
├── subfolder2/
│   ├── .git/
│   └── files...
│
└── subfolder3/
    ├── .git/
    └── files...
```

To update all subfolders, navigate to the directory containing the script and run it. Then the script will iterate through each subdirectory with an `.git` folder and perform the `git pull` command.
