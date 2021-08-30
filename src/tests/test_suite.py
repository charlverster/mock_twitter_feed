import unittest
import app.main as main
import app.database as database

class TestGetMethods(unittest.TestCase):
    
    def setUp(self):
        # Hardcoded test_files directory in ubuntu_docker container
        self.path = "/usr/src/tests/test_files"#"/Users/charlverster/Documents/GitHub/mock_twitter_feed/src/tests/test_files"
        # Test filenames
        self.test_user_file = "test_user.txt"
        self.test_tweet_file = "test_tweet.txt"

    def test_get_users_and_follows(self):
        # Arrange
            # Done in setUp()
        # Act
        users, content = main.get_users_and_follows(self.path,self.test_user_file)
        # Assert
        self.assertEqual(users,['Alan', 'Martin', 'Ward'])
        self.assertEqual(content,[['Ward', 'Alan'], ['Alan', 'Martin'], ['Ward', 'Martin', 'Alan']])

    def test_get_tweets(self):
        # Arrange
            # Done in setUp()
        # Act
        tweets = main.get_tweets(self.path,self.test_tweet_file)
        # Assert
        self.assertEqual(tweets,
            [
                ['Alan', 'If you have a procedure with 10 parameters, you probably missed some.'], 
                ['Ward', 'There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.'], 
                ['Alan', 'Random numbers should not be generated with a method chosen at random.']]
                        )

class TestAddMethods(unittest.TestCase):

    def setUp(self):
        db_user = 'db_engineer'
        db_pwd = 'twitter_password'
        db_host = 'mysqlserver' #'localhost'#
        db_port = 3306
        db_name = 'twitter'
        self.db = database.Database(db_user,db_pwd,db_host,db_port,db_name)

    def test_add_followers_to_db(self):
        # Arrange
        contents = ['test_user','user_followed']
        # Act
        main.add_followers_to_db(contents,self.db)
        # Assert

    def test_add_users_to_db(self):
        # Arrange
        contents = ['test_user1','test_user2']
        # Act
        main.add_users_to_db(contents,self.db)
        # Assert

    def test_add_tweets_to_db(self):
        # Arrange
        contents = ['test_user1','test tweet string']
        # Act
        main.add_tweets_to_db(contents,self.db)
        # Assert

class TestPrintMethods(TestAddMethods):
    
    def test_print_twitter_feed(self):
        # Arrange
            # Inherits database object from TestAddMethods
        # Act
        main.print_twitter_feed(self.db)

if __name__ == '__main__':
    unittest.main()

# Run with
# python -m unittest tests.test_suite -v (potentially python3 in container)