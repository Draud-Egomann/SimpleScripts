# Commit Timestamp Filter

This script filers all git commits and their timestamps, displaying all commits made between specified times. It also includes an option to exclude weekends.

## Prerequisites

- Python 3.x
- `gitpython` library

## Installation

To install the required `gitpython` library, use the following command:

```sh
pip install gitpython
```

## Usage

Run the script with the following command:

```sh
python main.py [repo_path] [branch] [include_weekends] [start_time] [end_time]
```

- `repo_path` (optional): Path to your git repository. Default is the current directory.
- `branch` (optional): The branch to check. Default is `main`.
- `include_weekends` (optional): Whether to include weekends. Use `true` or `false`. Default is `false`.
- `start_time` (optional): Start time in `HH:MM` format. Default is `07:00`.
- `end_time` (optional): End time in `HH:MM` format. Default is `17:00`.

## Example

To check commits in the current directory's main branch, excluding weekends, between 07:00 and 17:00, run:

```sh
python main.py . main false 07:00 17:00
```

## Important Notes

- Ensure the provided repository path is valid and points to a git repository.
- Time range is inclusive of the start and end times.
- Command-line arguments are optional; defaults will be used if not provided; Arguments are recomended