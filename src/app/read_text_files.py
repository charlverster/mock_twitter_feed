# functions for reading data from text files
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

def read_file(file_name,split_on,drop_list=None):
    """Reads file file_name line by line. Splits each line based on split_on argument and drops list items that equal items in the drop_list.
    drop_list is optional and defaults to None.
    Returns a list containing list of the extracted data."""
    content = []                                        # Empty list to store contents of file being read
    with open(file_name) as file:
        while (line := file.readline().rstrip()):
            if drop_list != None:
                for drop in drop_list:
                    line = line.replace(drop,"")
            fields = line.split(split_on)
            content.append(fields)
    return content