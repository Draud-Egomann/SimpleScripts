# Remove Temporary Files

This folder contains scripts to remove temporary files from your system, helping to free up disk space.

## Scripts

### 1. rmTemp.ps1

A PowerShell script that removes temporary files from various locations, empties the Recycle Bin, and runs the Windows Disk Cleanup tool.

#### Usage

Run the script with PowerShell:

```powershell
.\rmTemp.ps1
```

### 2. rmTemp.bat

A batch script that deletes temporary files from common temporary directories.

#### Usage

Run the script with Command Prompt:

```cmd
rmTemp.bat
```

## Note

- Ensure you have the necessary permissions to delete files in the specified directories.
- Running these scripts will permanently delete files from the temporary directories and the Recycle Bin.
