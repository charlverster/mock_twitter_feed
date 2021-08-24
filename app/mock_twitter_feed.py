# Mock Twitter Feed
import os
import sys

def get_path_to_input_files():
    """Gets path to folder where input files are expected."""
    try:
        path = os.getcwd() + "/app/files" # Relative path to working dir expected to contain input files
    except OSError:
        print("Could not find the current working directory. Quiting program.")
        sys.exit()
    else:
        return path

def check_for_only_two_files(file_path):
    """Checks that working directory contains two files."""
    files = os.listdir(file_path)       # Generates a list of files in working dir
    num_files = len(files)              # Counts files in list
    if num_files != 2:
        raise ValueError(f"Expected 2 files, found {num_files}. Quiting program.")

if __name__ == '__main__':
    # Run the app
    path = get_path_to_input_files()
    check_for_only_two_files(path)

