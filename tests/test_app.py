from mock_twitter_feed import * #app installed as package, import so its accessible to tests

#frist unit test tp check everything's working
def test_add():
    assert add(3,2) == 5


