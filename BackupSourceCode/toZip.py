import os
import zipfile
from datetime import datetime

# Configuration
FOLDER_NAME = "<folder>"  # Name of the folder to be zipped
ZIP_NAME = f"{FOLDER_NAME}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"

# Directories to skip
SKIP_FOLDERS = {
    ".git", ".idea", "node_modules", "dist", "android", "ios", "__pycache__", 
    "venv", "vendor", "bin", "obj", "packages", ".svn", ".hg", ".DS_Store", 
    "Thumbs.db", "build", "logs", "tmp", "temp", "cache", "backup", "backups",
}

def zip_folder(source_folder, zip_name, skip_folders):
    """Zips the source_folder while skipping specified directories."""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):
            # Filter out directories to be skipped
            dirs[:] = [d for d in dirs if d not in skip_folders]

            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_folder)
                zipf.write(file_path, arcname)

    print(f"Created zip archive: {zip_name}")


if __name__ == "__main__":
    current_dir = os.getcwd()
    source_path = os.path.join(current_dir, FOLDER_NAME)

    if os.path.exists(source_path):
        zip_folder(source_path, ZIP_NAME, SKIP_FOLDERS)
    else:
        print(f"Folder '{FOLDER_NAME}' not found in the current directory.")
