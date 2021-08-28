# Mock Twitter Feed
import os
import sys
from database import Database

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
        elem_list = elem.split()                # Split element on spaces into a list
        elem_list.remove("follows")     
        user_list = user_list + elem_list       # Append lists
        user_list = list(set(user_list))        # Convert to set to remove duplicates, convert back to list
        user_list.sort() # Sort                 # Sort alphabetically
    return user_list

#----------------------------------------------------------------

def add_followers_to_db(contents, db):
    """Accepts the user file contents, extracts the user and follows, and pushes that to the database."""

    for elem in contents:
        elem = elem.replace(',','')
        elem_list = elem.split()            # Split element on spaces into a list
        elem_list.remove("follows")
        user = elem_list[0]
        follows_user = elem_list[1:]
        for elem in follows_user:
            q = f"INSERT IGNORE INTO follows(username, follows_user) VALUES('{user}','{elem}');" # Inserts username and followee if it doesn't exist already
            db.insert_to_db(q)

#----------------------------------------------------------------
def add_users_to_db(users, db):
    for user in users:
        q = f"INSERT IGNORE INTO users VALUE('{user}');" # Inserts username only if it doesn't already exist
        db.insert_to_db(q)


def add_tweets_to_db(contents,db):
    """Reads tweet_file_contents and pushes username and tweet to posts table in database."""
    for elem in contents:
        elem = elem.replace('\n','')
        elem_list = elem.split("> ")
        user = elem_list[0]
        post = elem_list[1]
        q = f"INSERT INTO posts(username, post) VALUES('{user}','{post[:140]}');" # Inserts username and post (tweet) into database. Post is truncated at 140 characters.
        db.insert_to_db(q)

def print_twitter_histor(db):
    result = db.query_db("SELECT * FROM users;") # Returns list of tuples
    users = [_[0] for _ in result]         # Extract the first elements from the list of tuples
    for user in users:
        q = f"""
        WITH follower_posts AS
            (
            SELECT
                posts.*
            FROM
                posts 
                JOIN follows ON follows.follows_user = posts.username
            WHERE
                follows.username = '{user}'
            ),
        user_posts AS
            (
            SELECT
                *
            FROM 
                posts
            WHERE
                posts.username = '{user}'
            )
        SELECT
            *
        FROM
            user_posts
        UNION
        SELECT
            *
        FROM
            follower_posts
        ORDER BY
            post_id;
        """
        posts = db.query_db(q)
        print(user)
        for line in posts:
            user_who_posted = line[1]
            post = line[2]
            print(f"\t@{user_who_posted}: {post}")

if __name__ == '__main__':
    # Run the app
    input_path = get_path_to_input_files()
    files_to_read = check_for_only_two_files(input_path)
    user_file_contents = read_text_file(input_path + "/user.txt")
    tweet_file_contents = read_text_file(input_path + "/tweet.txt")
    users = get_users(user_file_contents)
    

    # Connect to database
    db_user = 'db_engineer'
    db_pwd = 'twitter_password'
    db_host = 'localhost'
    db_port = 3306
    db_name = 'twitter'
    db = Database(db_user,db_pwd,db_host,db_port,db_name)

    # Insert users into Database
    add_users_to_db(users, db)
    add_tweets_to_db(tweet_file_contents, db)
    add_followers_to_db(user_file_contents,db)
    print_twitter_histor(db)
    
     # Inserts username and post (tweet) into database. Post is truncated at 140 characters.
    # result = db.query_db(q)
    # print(key)
    # for line in result:
    #     post_id = line[0]
    #     user = line[1]
    #     post = line[2]
    #     print(f"\t@{user}: {post}")

#----------------------------------------------------------------
    db.insert_to_db("DELETE FROM posts WHERE post_id > 0;") # Purges posts table REMOVE!!
#----------------------------------------------------------------
    # result = db.query_db("SHOW TABLES;")
    # print(result)

    # db.close_connection()