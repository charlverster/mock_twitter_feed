from mock_twitter_feed import * #app installed as package, import so its accessible to tests

#Assumption: Program is run in a directory containing the relevant files
def test_check_for_files():
    assert check_for_files() == 2 # Checks that directory only contains two text files

