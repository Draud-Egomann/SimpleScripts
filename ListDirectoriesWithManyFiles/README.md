# Folder Scanner

This Python script allows you to scan a directory for specific folder names and optionally remove them.

## How to Use

1. **Requirements**: Make sure you have Python installed on your system.

2. **Usage**:

   ```bash
   python main.py root_directory_path folder_name_1 folder_name_2 ...
   ```

   - `root_directory_path`: The path to the directory you want to scan.
   - `folder_name_1`, `folder_name_2`, ...: Names of the folders you want to search for within the root directory.

3. **Output**: The script will list all found folders along with their paths.

4. **Removal**: After listing the found folders, you'll have the option to remove one or more of them.
   - Enter `y` to remove a folder or `n` to skip.

5. **Completion**: Once you've finished selecting folders to remove, the program execution will be completed.

## Note

- This script recursively scans the provided directory and its subdirectories.
- Use with caution as removing folders is irreversible.

## Example

Suppose you want to scan the directory `C:\Users\John\Documents` for folders named `node_modules` and `vendor`:

```bash
python main.py C:\Users\John\Documents node_modules vendor
```

This will list all occurrences of the `node_modules` and `vendor` folders within `C:\Users\John\Documents` and its subdirectories.  
The Script will **not** scan inside the `node_modules` and `vendor` folders.
