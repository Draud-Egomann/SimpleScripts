# License Filter

A Python tool to analyze and filter packages by their licenses from a JSON file.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the files.
2. Ensure Python 3.x is installed on your system.
3. No additional Python packages are required, as only the standard library is used.

## Usage

### `list_all.py`

Lists all unique licenses and their associated packages.

**Usage:**

```bash
python list_all.py [path_to_json]
```

**Parameters:**

- `path_to_json` (optional): The path to the JSON file. Defaults to `package.json` if not provided.

**Example:**

```bash
python list_all.py
```

This will list all unique licenses and the packages associated with each license, as well as a summary of all licenses at the end.

### `find_specific_packages.py`

Finds and lists packages that use a specific license.

**Usage:**

```bash
python find_specific_packages.py [path_to_json] [license_name]
```

**Parameters:**

- `path_to_json` (optional): The path to the JSON file. Defaults to `package.json` if not provided.
- `license_name` (optional): The license name to search for. Defaults to `"MIT"` if not provided.

**Example:**

```bash
python find_specific_packages.py package.json MIT
```

This will list all packages that use the `"MIT"` license.

## Example

Given a `package.json` file with the following content:

```json
{
    "resolve-from@5.0.0": {
        "licenses": "MIT",
        "repository": "https://github.com/example/other-package",
        "publisher": "Example Publisher",
        "email": "example@example.com",
        "path": "C:\\path\\to\\resolve-from",
        "licenseFile": "C:\\path\\to\\resolve-from\\license"
    },
    "other-package@1.2.3": {
        "licenses": "Apache-2.0",
        "repository": "https://github.com/example/other-package",
        "publisher": "Example Publisher",
        "email": "example@example.com",
        "path": "C:\\path\\to\\other-package",
        "licenseFile": "C:\\path\\to\\other-package\\license"
    }
}
```

Running `list_all.py` will output:

```
License: MIT in 1 packages
  - resolve-from@5.0.0

License: Apache-2.0 in 1 packages
  - other-package@1.2.3

Licenses in project:
- MIT
- Apache-2.0
```

Running `find_specific_packages.py` with the license `"MIT"` will output:

```
Packages with the license 'MIT':
resolve-from@5.0.0
```

## Important Notes

- Both scripts assume the JSON file is in the same directory. You can specify a different path using command line arguments.
- The license names and package names are taken directly from the JSON file, so ensure the file is formatted correctly to avoid errors.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
