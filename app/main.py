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

def get_users(lst):
    """Accepts user_file_contents. Removes commas (',') and the word "follows". Compiles a list of all the unique user names"""
    user_list = []
    for elem in lst:
        elem = elem.replace(',','')
        elem_list = elem.split()            # Split element on spaces into a list
        elem_list.remove("follows")     
        user_list = user_list + elem_list   # Append lists
    return tuple(set(user_list))     # Covert to set to remove duplicates then convert to tuple.

def get_user_followees(users,contents):
    """Accepts a tuple of user name and the user_file_contents, then populates a dictionary with who each user follows in the format:
    {user: [list of followees]}
    """
    user_followees = {user:[] for user in users}     # Dictionary containing list of followees for each user
    for elem in contents:
        elem = elem.replace(',','')
        elem_list = elem.split()            # Split element on spaces into a list
        elem_list.remove("follows")
        username = elem_list[0]
        if username in user_followees:
            user_followees[username] = user_followees[username] + elem_list[1:] #Concatenates user_followee list with followees read from contents
    return user_followees

def get_tweets(user,contents):
    """Reads tweet_file_contents and saves output in dictionary as strings with format:
    {user:tweet}
    """
    tweets = {}
    tweet_order = 1                     # Number tweets starting at 1. This could also be datetime
    for elem in contents:
        elem = elem.replace('\n','')
        elem_list = elem.split("> ")
        elem_list.append(tweet_order)   # Append the tweet order
        tweet_order += 1
        print(elem_list)

if __name__ == '__main__':
    # Run the app
    input_path = get_path_to_input_files()
    files_to_read = check_for_only_two_files(input_path)
    user_file_contents = read_text_file(input_path + "/user.txt")
    tweet_file_contents = read_text_file(input_path + "/tweet.txt")
    users = get_users(user_file_contents)
    users_with_followees = get_user_followees(users, user_file_contents)
    get_tweets(users,tweet_file_contents)