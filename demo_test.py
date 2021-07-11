import demo
import unittest


class TestDemo(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(demo.compare(10, 2), 10)
        self.assertEqual(demo.compare(100, 28), 100)
        self.assertEqual(demo.compare(3, 4), 4)
