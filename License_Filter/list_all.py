import json
import sys
import os
from collections import defaultdict

def load_data_from_json(filename):
    """
    Load data from a JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def list_all_licenses(data):
    """
    List all unique licenses and their associated packages.
    """
    licenses = defaultdict(list)
    
    # Collect packages for each license
    for package_name, package_info in data.items():
        license_name = package_info["licenses"]
        licenses[license_name].append(package_name)
    
    # Print each license and the associated packages
    for license_name, packages in licenses.items():
        print(f"License: {license_name} in {len(packages)} packages")
        for package in packages:
            print(f"  - {package}")
        print("")
    
    # Print all unique licenses at the end
    print("Licenses in project:")
    for license_name in licenses.keys():
        print(f"- {license_name}")

def main():
    filename = 'package.json'

    # Check if command line arguments are provided to customize json path
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"File {filename} not found.")
        return
    
    # Load data from the JSON file
    data = load_data_from_json(filename)
    
    # List all packages and their licenses
    list_all_licenses(data)

if __name__ == '__main__':
    main()
