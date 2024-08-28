import json
import sys
import os

def load_data_from_json(filename):
    """
    Load data from a JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_packages_by_license(data, license_name):
    """
    Return all packages with a specific license.
    """
    matching_packages = []
    for package_name, package_info in data.items():
        if package_info["licenses"] == license_name:
            matching_packages.append(package_name)
    return matching_packages

def main():
    filename = 'package.json'
    search_license = "MIT"

    # Check if command line arguments are provided to customize json path and license
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2:
        search_license = sys.argv[2]
    
    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"File {filename} not found.")
        return
    
    # Load data from the JSON file
    data = load_data_from_json(filename)
    
    # Find packages with the specified license
    packages_with_license = get_packages_by_license(data, search_license)
    print(f"Packages with the license '{search_license}':")
    for package in packages_with_license:
        print(package)

if __name__ == '__main__':
    main()
