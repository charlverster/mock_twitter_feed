# Mock Twitter Feed
from database import Database
import read_text_files as rd

def add_followers_to_db(contents, db):
    """Accepts the user file contents, extracts the user and follows, and pushes that to the database."""
    for elem in contents:
        user = elem[0]
        follows_user = elem[1:]
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
        user = elem[0]
        post = elem[1]
        q = f"INSERT INTO posts(username, post) VALUES('{user}','{post[:140]}');" # Inserts username and post (tweet) into database. Post is truncated at 140 characters.
        db.insert_to_db(q)

def print_twitter_feed(db):
    result = db.query_db("SELECT * FROM users;")    # Get all the users in the database. Returns list of tuples
    users = [_[0] for _ in result]                  # Extract the first element (the username) from each tuple
    for user in users:                              # Queries the database for each username in the list
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
        result = db.query_db(q)                          # Returns the query results
        print(user)                                         
        for elem in result:
            user_who_posted = elem[1]
            post = elem[2]
            print(f"\t@{user_who_posted}: {post}")

def get_users_and_follows(path):
    """Reads the user.txt file. Returns list of unique users and list formatted as [user,[list of users they follow]] """
    contents = rd.read_file(path + "/user.txt"," ",[" follows",","])
    users = [item for sublist in contents for item in sublist]              # Flatten list of lists into single list
    users = list(set(users))                                                # Convert to set to remove duplicates. Convert back to list.
    users.sort()    
    return users, contents

def get_tweets(path):
    """Reads tweet.txt and returns contents as list with format [[user,tweet],[user,tweet],...]"""
    return rd.read_file(path + "/tweet.txt","> ")

if __name__ == '__main__':
    # Run the app
    input_path = rd.get_path_to_input_files()
    rd.check_for_only_two_files(input_path)
    
    # Connect to database
    db_user = 'db_engineer'
    db_pwd = 'twitter_password'
    db_host = 'localhost' #mysqlserver
    db_port = 3306
    db_name = 'twitter'
    db = Database(db_user,db_pwd,db_host,db_port,db_name)

    # Users
    users, follows = get_users_and_follows(input_path)   # Reads the user.txt file and return a list of unique usernames and list of users and who they follow.
    add_users_to_db(users, db)      # Insert users into Database

    # Tweets
    tweets = get_tweets(input_path)
    add_tweets_to_db(tweets, db)

    # Follows
    add_followers_to_db(follows,db)

    # Print twitter feed
    print_twitter_feed(db)

#----------------------------------------------------------------
    db.insert_to_db("DELETE FROM posts WHERE post_id > 0;") # Purges posts table REMOVE!!
#----------------------------------------------------------------
    # Close the connection to the database
    db.close_connection()   
