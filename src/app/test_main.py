import unittest
import main

class TestGetMethods(unittest.TestCase):
    
    def setUp(self):
        # Test_files directory in ubuntu_docker container
        self.path = "/usr/src/app/test_files"
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

if __name__ == '__main__':
    unittest.main()