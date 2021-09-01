import unittest
import read_text_files as rd
import os

class TestGetMethods(unittest.TestCase):
        
    def test_get_path_to_input_files(self):
        # Arrange
        expected_result = '/usr/src/app/files'
        # Act
        test = rd.get_path_to_input_files()
        # Assert
        self.assertEqual(str(test),str(expected_result))

    def test_read_file(self):
        # Arrange
        filepath =  "/usr/src/app/test_files/test_user.txt"
        split_on = " "
        drop_list = [" follows",","]
        expected_result = [['Ward', 'Alan'], ['Alan', 'Martin'], ['Ward', 'Martin', 'Alan']]
        # Act
        test = rd.read_file(filepath,split_on,drop_list)
        # Assert
        self.assertEqual(test,expected_result)

if __name__ == '__main__':
    unittest.main()