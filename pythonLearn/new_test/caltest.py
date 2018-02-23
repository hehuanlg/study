from calculator import count
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print('test start')
    def tearDown(self):
        print('test end')
class TestAdd(MyTest):
    def test_add(self):
        j = count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = count(7,3)
        self.assertEqual(j.add(),10)
    def test_sub(self):
        j = count(2,3)
        self.assertEqual(j.sub(),-1)
    def test_sub2(self):
        j = count(7,3)
        self.assertEqual(j.sub(),4)
# if __name__ == '__main__':
#     unittest.main()

