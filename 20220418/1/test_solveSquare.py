import unittest

from SolveSquare import solveSquare

class SolveSquareTest(unittest.TestCase):    
    def test_positive_d(self):
        result = solveSquare(1, -1, 0)
        self.assertTrue(type(result) is tuple)
        self.assertTrue(len(result) == 2)
        x1, x2 = result
        self.assertTrue(x1 != x2)
        self.assertTrue(x1 == 0)
        self.assertTrue(x2 == 1)

    def test_zero_d(self):
        result = solveSquare(1, -2, 1)
        self.assertTrue(type(result) is tuple)
        self.assertTrue(len(result) == 2)
        x1, x2 = result
        self.assertTrue(x1 == x2)
        self.assertTrue(x1 == 1)
        self.assertTrue(x2 == 1)

    def test_nagative_d(self):
        result = solveSquare(1, 1, 1)
        self.assertTrue(result is None)
