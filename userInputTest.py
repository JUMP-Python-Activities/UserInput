import unittest 
from unittest.mock import patch
from io import StringIO

import userInputAnswer as userInput

class TestUserInput(unittest.TestCase):

    @patch('sys.stdin', StringIO('Test\nTest\nTest'))
    @patch('sys.stdout', new_callable= StringIO)
    def test_output(self, stdout):
        #Run the function
        x = userInput
        x.userInput()

        #Save what we are expecting
        expected= """What is your name: What is your age: What is your profession: Test...Test...Test thank you!"""

        #Check values
        self.assertEqual(stdout.getvalue(), expected)

    
if __name__ == '__main__':
    unittest.main()