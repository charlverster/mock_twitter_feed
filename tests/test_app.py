from mock_twitter_feed import * #app installed as package, import so its accessible to tests

# def test_get_path_to_input_files():
#     assert get_path_to_input_files() == "/Users/charlverster/Documents/GitHub/mock_twitter_feed/app/files"
    # Works. Don't need to keep testing this

#Assumption: Program is run in a directory containing a folder 'files' with the relevant files
# def test_check_for_only_two_files():
#     path = "/Users/charlverster/Documents/GitHub/mock_twitter_feed/app/files"
#     check_for_only_two_files(path) # Checks that directory only contains two text files
    # Works

def test_read_text_file():
    read_text_file()