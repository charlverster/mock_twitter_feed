import unittest
import read_text_files as rd

class TestGetMethods(unittest.TestCase):
        
    def test_get_path_to_input_files(self):
        # Arrange
        path = 'usr/src/app/files'
        # Act
        result = rd.get_path_to_input_files()
        # Assert
        self.assertEqual(str(path),str(result))

    def test_read_file(self):
        # Arrange
        filepath = "usr/src/app/test_files/test_user.txt"
        split_on = " "
        drop_list = [" follows",","]
        # Act
        result = rd.read_file(filepath,split_on,drop_list)
        # Assert
        self.assertEqual(result,[['Ward', 'Alan'], ['Alan', 'Martin'], ['Ward', 'Martin', 'Alan']])

if __name__ == '__main__':
    unittest.main()