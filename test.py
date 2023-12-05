import unittest
from function import is_palindrome, farewell, greeting

class TestApplication(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(greeting("English"), "Good morning")
        self.assertEqual(greeting("Français"), "Bonjour")
    
    def test_farewell(self):
        self.assertEqual(farewell("English"), "Goodbye")  
        self.assertEqual(farewell("Français"), "Au revoir")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertFalse(is_palindrome("python"))
        #self.assertTrue(is_palindrome("Ésope reste ici et se repose")) 

if __name__ == '__main__':
    unittest.main()
