import os
import sys

def get_path_to_input_files():
    """Return absolute path of 'files' folder."""
    try:
        path = os.getcwd() + "/app/files" # Relative path to working dir expected to contain input files
    except FileNotFoundError:
        print("Folder named 'files' not found.")
        sys.exit()
    else:
        return path

def read_file(file_path,split_on,drop_list=None):
    """Read file_name line by line. Split each line based on split_on argument and drop list items that equal items in the drop_list.
    drop_list is optional and defaults to None.
    Return a list containing list of the extracted data."""
    content = []            # Empty list to store contents of file being read
    try:          
        file = open(file_path)
    except FileNotFoundError:
        print(f"File named '{file_path}' not found.")
        sys.exit()
    else:
        while (line := file.readline().rstrip()):
            if drop_list != None:
                for drop in drop_list:
                    line = line.replace(drop,"")
            fields = line.split(split_on)
            content.append(fields)
        file.close()
        return content