import unittest
from internal import math

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(math.add(1, 2), 3)

def test_add3():
    assert math.add(1, 2) == 3