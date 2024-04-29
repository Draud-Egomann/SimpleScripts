import sys
import os
from PyPDF2 import PdfMerger

# Define paths for data and output directories
DATA_DIR_PATH = os.path.join(os.path.dirname(__file__), "..", "data")
OUTPUT_DIR_PATH = os.path.join(os.path.dirname(__file__), "..", "output")
OUTPUT_FILE_NAME = "merged_pdf.pdf"

def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        pdf_files (list): List of paths to PDF files to merge.
        output_path (str): Path to save the merged PDF file.
    """
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_path)
    merger.close()

def check_if_dir_exists(dir_path):
    """
    Check if a directory exists.

    Args:
        dir_path (str): Path to the directory.

    Returns:
        bool: True if the directory exists, False otherwise.
    """
    if not os.path.exists(dir_path):
        print("Directory does not exist:", dir_path)
        return False
    return True

def main():
    # Get a list of PDF files in the data directory
    pdf_files = [os.path.join(DATA_DIR_PATH, file) for file in os.listdir(DATA_DIR_PATH) if file.lower().endswith('.pdf')]

    if pdf_files:
        # Merge PDF files if there are any
        merge_pdfs(pdf_files, os.path.join(OUTPUT_DIR_PATH, (OUTPUT_FILE_NAME + ".pdf")))
        print("PDF files merged successfully!")
    else:
        print("No PDF files found in the data directory.")

if __name__ == '__main__':
    # Check if command line arguments are provided to customize output file and directories
    if len(sys.argv) > 1:
      OUTPUT_FILE_NAME = sys.argv[1]
    if len(sys.argv) > 2:
        DATA_DIR_PATH = sys.argv[2]
    if len(sys.argv) > 3:
        OUTPUT_DIR_PATH = sys.argv[3]

    # Ensure that the directories exist or create them if not
    if not check_if_dir_exists(DATA_DIR_PATH):
        os.makedirs(DATA_DIR_PATH)
    if not check_if_dir_exists(OUTPUT_DIR_PATH):
        os.makedirs(OUTPUT_DIR_PATH)

    main()
