# import unittest
#
# class TestMymaths(unittest.TestCase):
#     def test_addition(self):
#         self.assertEqual(3 + 3, 6)
#
#     def test_subtraction(self):
#         self.assertEqual(5 - 2, 3)
#
#     def test_multiply(self):
#         self.assertEqual(3*4,12)
#
# if __name__ == '__main__':
#     unittest.main()


import unittest

class ToconfirmUnitest(unittest.TestCase):

    def test_now(self):
        self.assertEqual(12/2,6)

    def test_whether_it_owrk(self):
        self.assertTrue(4 > 3) #actual , & expected 3+3=actual, 6=expected

    def test_ok(self):
        self.assertEqual(100 / 2 , 50)

    def test_again(self):
        self.assertFalse(2 > 5)


if __name__ == '__main__':
    unittest.main()
