#unit test: verifies one specific aspect of function's behaviour is correct
#test case: collection of unit tests that together prove function behaves as expected, 
#   within full rnage of situations
#test coverage: full range of unit tests to cover all possible ways to use function

import unittest
from name_function import get_formatted_name

#class name must include Test word
#inherit from unittest.TestCase
class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last__middle_name(self):
        formatted_name = get_formatted_name('janis', 'joplin', 'jo')
        self.assertEqual(formatted_name, 'Janis Jo Joplin')

#run the test
unittest.main()


#other assert methods
#assertEqual(a,b)
#assertNotEqual(a,b)
#assertTrue(x)
#assertFalse(x)
#assertIn(item,list)
#assertNotIn(item,list)

#to test classes, include a setUp method
#def setUp(self):
#It runs this setUp method each time before running each test method
