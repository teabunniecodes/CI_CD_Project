import unittest
import os
import io
from unittest.mock import patch # Used to mock (replace) sys.stdout

import config

class TestConfig(unittest.TestCase):
    def setUp(self):
        """
        Set up any common resources or initial states before each test.
        In this case, we define the path to the file we're testing.
        """
        print("\nSetting up for a test...")
        self.program_file_path = "config.py"
        
    def tearDown(self):
        """
        Clean up resources after each test.
        For these tests, no specific cleanup (like deleting files) is needed
        as we are only reading an existing file and capturing output.
        """
        print("Tearing down after a test.")
        
    def test_file_contains_hello_world(self):
        print("Running test_file_contains_hello_world string...")
        expected_string = "Hello World :)"
    
        # Checks that the file exists before trying to read it
        self.assertTrue(os.path.exists(self.program_file_path),
                        f"Error: The file '{self.program_file_path}' does not exist")
        
        # Opens and reads the entire contents of file
        with open(self.program_file_path, "r") as _file:
            file_content = _file.read()
            
        # Checks if the expected string is present in contents of file
        self.assertIn(expected_string, file_content,
                      f"'{expected_string}' not found in '{self.program_file_path}'")
        print(f"Successfully verified that '{expected_string}' is in '{self.program_file_path}'")
        
    def test_program_prints_hello_world(self):
        print("Running test_program_prints_hello_world...")
        expected_output = "Hello World :)\n"
        
        # Use patch to temporarily replace sys.stdout with a StringIO object.
        # This allows us to capture whatever is printed to the console.
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            config.hello()
            
            # Get the value that was "printed" to our mock_stdout
            captured_output = mock_stdout.getvalue()
            self.assertEqual(captured_output, expected_output,
                             f"Expected to print '{expected_output}', but got '{captured_output}'.")
        print(f"Successfully verified that 'config.hello()' prints '{expected_output.strip()}'.")
            
if __name__ == '__main__':
    unittest.main(verbosity=2)