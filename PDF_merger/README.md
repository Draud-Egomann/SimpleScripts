# PDF Merger

This script merges multiple PDF files into a single PDF file.

## Prerequisites

- Python 3.x
- PyPDF2 library

## Installation

1. Clone the repository:
2. Install the required dependencies:

```bash
pip install PyPDF2
```

## Usage

1. Place the PDF files you want to merge into the `data` directory.
2. Run the script:

```bash
python main.py [output_file_name] [data_directory_path] [output_directory_path]
```

- `[output_file_name]` (optional): Specify the name of the output merged PDF file. The .pdf suffix is automatically added. Default is `merged_pdf.pdf`.
- `[data_directory_path]` (optional): Specify the path to the directory containing the input PDF files. Default is `./data`.
- `[output_directory_path]` (optional): Specify the path to the directory where the output merged PDF file will be saved. Default is `./output`.

## Example

Merge PDF files with default settings:

```bash
python main.py
```

Merge PDF files with custom output file name and directory:

```bash
python main.py my_merged_file C:\data C:\output
```

## Important Notes

- The script can only select PDF files and ignores other files
- The Order how the PDF files will be merged, is based on the file name
- If the exported PDF file has the same filename as an existing file in the selected folder, the existing file will be overwritten