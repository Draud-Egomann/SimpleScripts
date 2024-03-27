import os
import shutil

def scan_folders(root_dir, folder_names, found_paths):
    for root, dirs, files in os.walk(root_dir):
        for folder_name in folder_names:
            if folder_name in dirs:
                folder_path = os.path.join(root, folder_name)

                found = False
                # Check if folder is already in found_paths
                for item in found_paths:
                    if folder_name in item:
                        # Append path to existing folder_name key
                        item[folder_name].append(folder_path)
                        found = True
                        break
                if not found:
                    # Add new folder_name key to found_paths
                    found_paths.append({folder_name: [folder_path]})
                dirs.remove(folder_name)  # Exclude found folder from further search

def remove_folders(found_paths, selection):
    for item in found_paths:
        for folder_name, paths in item.items():
            for path in paths:
                response = input(f"Do you want to remove the folder '{folder_name}' at path '{path}'? (y/n): ")
                if response.lower() == "y":
                    try:
                        shutil.rmtree(path) # remove folder with all its contents
                    except Exception as e:
                        print(f"Error when removing folder: {e}")

# Mock array of folder names (replace with actual folder names as needed)
mock_array = ["node_modules", "vendor", ".nuxt"]
found_paths = []

# Replace 'root_directory_path' with the path of the root directory you want to scan
root_directory_path = "C:/Users/Justin/Documents/pytest"

if __name__ == "__main__":
    scan_folders(root_directory_path, mock_array, found_paths)
    
    # Printing all found paths
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

    print("\n")
    response = input("Do you want to remove any of the found folders? (y/n): ")
    if response.lower() == "y":
        print(found_paths)

        # print("0: Select all")
        # for i, item in enumerate(found_paths):
        #     for folder_name, paths in item.items():
        #         for path in paths:
        #             print(f"{i+1}: {folder_name}")
        # try:
        #     selection = input("Your selection: ")
        #     selection = int(selection) # convert input to integer
        # except ValueError:
        #     print("Invalid input. Exiting program...")
        #     input("Press any key to exit...")
        #     exit()

        remove_folders(found_paths, selection)

    # temporary disable for testing
    # print("Program execution completed.")
    # input("Press any key to exit...")
