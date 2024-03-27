import os

def scan_folders(root_dir, folder_names, found_paths):
    for root, dirs, files in os.walk(root_dir):
        for folder_name in folder_names:
            if folder_name in dirs:
                folder_path = os.path.join(root, folder_name)
                found_paths.append({folder_name: [folder_path]})
                dirs.remove(folder_name)  # Exclude found folder from further search

# Mock array of folder names (replace with actual folder names as needed)
mock_array = ["node_modules", "vendor", ".nuxt"]
found_paths = []

# Replace 'root_directory_path' with the path of the root directory you want to scan
root_directory_path = "C:/Users/Justin/Documents/"

if __name__ == "__main__":
    scan_folders(root_directory_path, mock_array, found_paths)
    
    # Printing all found paths
    print("\nFound paths:")
    printed_folders = set()  # Set to keep track of printed folder names
    for item in found_paths:
        for folder_name, paths in item.items():
            if folder_name not in printed_folders:
                print(f"{folder_name}:")
                printed_folders.add(folder_name)  # Add folder name to printed set
                for path in paths:
                    print(f"   {path}")
            else:
                for path in paths:
                    print(f"   {path}")
