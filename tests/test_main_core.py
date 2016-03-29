import unittest

from main_core import key, bspacing

class TestCache(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_key(self):
        k = key('x',1,2)
        self.assertEqual(k.hold, 1)
        self.assertEqual(k.releasedn, 2)
        self.assertEqual(k.name, 'x')


if __name__ == '__main__':
    unittest.main()