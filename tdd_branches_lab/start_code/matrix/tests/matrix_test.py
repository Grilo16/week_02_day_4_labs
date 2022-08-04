import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    # Tests

    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    # Test can extract a given row
    def test_can_extract_row(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
        self.assertEqual(matrix.row(1), [1, 2, 3])
        self.assertEqual(matrix.row(2), [4, 5, 6])
        self.assertEqual(matrix.row(3), [7, 8, 9])
   
    # Test can extract a given row where numbers have different number of digits
    # Example matrix:
    #
    # 1 2
    # 10 20
    def test_can_extract_row_different_number_digits(self):
        matrix = Matrix("1 2 3\n10 20 30\n100 200 300")
        self.assertEqual(matrix.row(1), [1, 2, 3])
        self.assertEqual(matrix.row(2), [10, 20, 30])
        self.assertEqual(matrix.row(3), [100, 200, 300])

    # Test can extract row from non-square matrix
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6
    def test_can_extract_row_non_square_matrix(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.row(1), [1, 2, 3])
        self.assertEqual(matrix.row(2), [4, 5, 6])
        self.assertEqual(matrix.row(3), [7, 8, 9])
        self.assertEqual(matrix.row(4), [8, 7, 6])

    # Test can extract a column

    # Test can extract column from a one number matrix
    def test_can_extract_column_1_number(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.column(1), [1])

    # Test can extract a column from non-square matrix
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6
    def test_can_extract_column_non_square(self):
        matrix = Matrix("1 2 3 4\n5 6 8 8\n9 8 7 6")
        self.assertEqual(matrix.column(1), [1, 5, 9])
        self.assertEqual(matrix.column(2), [2, 6, 8])
        self.assertEqual(matrix.column(3), [3, 8, 7])
        self.assertEqual(matrix.column(4), [4, 8, 6])

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    #
    # 89 1903 3
    # 18 3 1
    # 9 4 800
    def test_can_extract_column_differend_digits(self):
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        self.assertEqual(matrix.column(1), [89, 18, 9])
        self.assertEqual(matrix.column(2), [1903, 3, 4])
        self.assertEqual(matrix.column(3), [3, 1, 800])



