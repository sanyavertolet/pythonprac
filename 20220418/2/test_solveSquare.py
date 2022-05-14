import unittest

from unittest.mock import MagicMock
from unittest.mock import Mock

from SolveSquare import solveSquare
from SquareIO import SquareIO

class SolveSquareTest(unittest.TestCase):    
    def setUp(self):
        self.squareIO = Mock()
        def mock_input(name, mock_input = 0):
            print(f"Input {name}: {mock_input}")
            return mock_input
        self.squareIO.inputCoeff = mock_input
        self.squareIO.inputCoeff.return_value = 1
        self.squareIO.printResult = lambda l: print(f"Result: {l}")

    def test_positive_d(self):
        a = self.squareIO.inputCoeff("a", 1)
        b = self.squareIO.inputCoeff("b", 0)
        c = self.squareIO.inputCoeff("c", -1)

        coeffs = []
        result = solveSquare(a, b, c)
        self.assertTrue(type(result) is tuple)
        self.assertTrue(len(result) == 2)
        x1, x2 = result
        self.assertTrue(x1 != x2)
        self.assertTrue(x1 == -1)
        self.assertTrue(x2 == 1)
        self.squareIO.printResult(result)


    def test_zero_d(self):
        a = self.squareIO.inputCoeff("a", 1)
        b = self.squareIO.inputCoeff("b", -2)
        c = self.squareIO.inputCoeff("c", 1)

        coeffs = []
        result = solveSquare(a, b, c)
        self.assertTrue(type(result) is tuple)
        self.assertTrue(len(result) == 2)
        x1, x2 = result
        self.assertTrue(x1 == x2)
        self.assertTrue(x1 == 1)
        self.assertTrue(x2 == 1)
        self.squareIO.printResult(result)

    def test_zero_d(self):
        a = self.squareIO.inputCoeff("a", 1)
        b = self.squareIO.inputCoeff("b", 1)
        c = self.squareIO.inputCoeff("c", 1)

        coeffs = []
        result = solveSquare(a, b, c)
        self.assertTrue(result is None)
        self.squareIO.printResult(result)

    def test_linear_eq(self):
        a = self.squareIO.inputCoeff("a", 0)
        b = self.squareIO.inputCoeff("b", 1)
        c = self.squareIO.inputCoeff("c", -2)

        coeffs = []
        result = solveSquare(a, b, c)
        self.assertTrue(type(result) is float)
        self.assertTrue(result == 2)
        self.squareIO.printResult(result)

    def test_const_eq(self):
        a = self.squareIO.inputCoeff("a", 0)
        b = self.squareIO.inputCoeff("b", 0)
        c = self.squareIO.inputCoeff("c", 1)

        coeffs = []
        result = solveSquare(a, b, c)
        self.assertTrue(result is None)
        self.squareIO.printResult(result)

    def test_identity_eq(self):
        a = self.squareIO.inputCoeff("a", 0)
        b = self.squareIO.inputCoeff("b", 0)
        c = self.squareIO.inputCoeff("c", 0)

        coeffs = []
        result = solveSquare(a, b, c)
        self.assertTrue(type(result) is bool)
        self.assertTrue(result == True)
        self.squareIO.printResult(result)
