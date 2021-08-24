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

def check_for_only_two_files(folder_path):
    """Checks that working directory contains two text files."""
    filenames = os.listdir(folder_path)       # Generates a list of files in working dir
    files = [folder_path + "/" + file for file in filenames if file.lower().endswith('.txt')] # Siphons out .txt files and joins folder path and filename
    num_files = len(files)             # Counts files in list
    if num_files != 2:
        raise ValueError(f"Expected 2 files, found {num_files}. Quiting program.")
    else:
        return files

def read_text_file(file_path):
    """Reads list of text files and returns contents as a list of lines"""
    try: 
        with open(file_path,'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Text file not found. Quiting program.")
    else:
        return lines

if __name__ == '__main__':
    # Run the app
    input_path = get_path_to_input_files()
    files_to_read = check_for_only_two_files(input_path)
    user_file_contents = read_text_file(input_path + "/user.txt")
    tweet_file_contents = read_text_file(input_path + "/tweet.txt")
    print(tweet_file_contents)