from unittest import mock
import unittest

from condep import utilities


class ReturnsSquareMatrix(unittest.TestCase):
    def runTest(self):
        matrix = utilities.square_matrix(4)

        self.assertEqual(len(matrix),4, 'Should be 4 columns')
        
        for col in matrix:
            self.assertEqual(len(col),4, 'Should be 4 cells per column')

if __name__ == '__main__':
    unittest.main(module='utilities_tests')
