import unittest
from city_functions import world
class cityNameTest(unittest.TestCase):
    def test_city_country(self):
        name = world('santiago', 'chlie')
        self.assertEqual(name,'Santiago, Chlie')
unittest.main()
