"""A module for a matrix class
"""

import random

class Matrix():
    """A matrix class.
    """

    rows = 0
    columns = 0
    values = []

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.values = [[0.0 for _ in range(columns)] for _ in range(rows)]

    @staticmethod
    def random_int_matrix(rows, columns, _a, _b):
        """Returns a matrix with the size of rows and columns filled with random int values.
        Arguments:
            rows {int} -- The rows
            columns {int} -- The columns
            a {int} -- The start of the random
            b {int} -- The end of the random
        Returns:
            Matrix -- The random Matrix
        """
        result = Matrix(rows, columns)
        result.values = [[random.randint(_a, _b) for _ in range(columns)] for _ in range(rows)]
        return result

    @staticmethod
    def identity_matrix(size_n):
        """Returns the identity matrix with the size n,n
        Arguments:
            size_n {int} -- Determines the size of the matrix.
        Returns:
            Matrix -- The identity matrix with the size n,n
        """
        result = Matrix(size_n, size_n)
        for _i in range(size_n):
            result[_i][_i] = 1.0
        return result

    def __getitem__(self, key):
        return self.values[key]

    def __str__(self):
        _s = ""
        for column in self.values:
            _s += f"{column}\n"
        return _s[:-1]

    def __eg__(self, _m):
        if not isinstance(_m, Matrix):
            raise Exception()

        if not self.matrix_size_equal(_m):
            return False

        for row in range(self.rows):
            for col in range(self.columns):
                if self[row][col] != _m[row][col]:
                    return False
        return True

    def __add__(self, _m):
        if not self.matrix_size_equal(_m):
            raise Exception()

        if not isinstance(_m, Matrix):
            raise Exception()

        result = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                result[row][col] = self[row][col] + _m[row][col]

        return result

    def __neg__(self):
        result = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                result[row][col] = -self[row][col]
        return result

    def __sub__(self, _m):
        if not self.matrix_size_equal(_m):
            raise Exception()

        if not isinstance(_m, Matrix):
            raise Exception()

        return self + -_m

    def __mul__(self, numb):
        result = None
        if isinstance(numb, (int, float)):
            result = Matrix(self.rows, self.columns)
            for row in range(self.rows):
                for col in range(self.columns):
                    result[row][col] = self[row][col] * numb

        elif isinstance(numb, Matrix):
            if not self.columns == numb.rows:
                raise Exception()

            result = Matrix(self.rows, numb.columns)
            for row in range(result.rows):
                for col in range(result.columns):
                    for _i in range(self.columns):
                        result[row][col] += self[row][_i] * numb[_i][col]

        else:
            raise Exception()

        return result

    def transpose(self):
        """Transpose the current Matrix. (Turning rows into columns and columns into rows)
        Returns:
            Matrix -- The transposed matrix
        """
        result = Matrix(self.columns, self.rows)
        for row in range(self.rows):
            for col in range(self.columns):
                result[col][row] = self[row][col]
        return result

    def trace(self):
        """TODO
        """
        if not self.is_square_matrix():
            raise Exception()
        trace = 0
        for _i in range(self.rows):
            trace += self[_i][_i]
        return trace

    def determinant(self):
        """TODO
        """
        if not self.is_square_matrix():
            raise Exception()

        det = 0
        if self.rows == 1:
            det = self[0][0]
        elif self.rows == 2:
            det = self[0][0] * self[1][1] - self[1][0] * self[0][1]
        else:
            for row in range(self.rows):
                _comatrix = Matrix(self.rows - 1, self.columns - 1)
                factor = self[row][0]
                if row % 2 == 1:
                    factor = -factor

                for com_row in range(_comatrix.rows):
                    for com_col in range(_comatrix.columns):
                        if com_row >= row:
                            _comatrix[com_row][com_col] = self[com_row + 1][com_col + 1]
                        else:
                            _comatrix[com_row][com_col] = self[com_row][com_col + 1]

                det += factor * _comatrix.determinant()

        return det

    def matrix_size_equal(self, _m1):
        """Check if the size of 2 matrix is equal.
        Arguments:
            m1 {Matrix()} -- The matrix to check
        Returns:
            bool -- True if the size of them is equal. False if not.
        """
        return self.rows == _m1.rows and self.columns == _m1.columns

    def is_square_matrix(self):
        """Check if the matrix is a square matrix.
        i.e. the matrix have the same number of rows and columns
        Returns:
            bool -- True if the matrix is a square matrix. False if not
        """
        return self.rows == self.columns


def main():
    """Main method
    """
    _m1 = Matrix.random_int_matrix(3, 5, -9, 9)
    _m2 = Matrix.random_int_matrix(1, 8, -9, 9)
    _m3 = Matrix.random_int_matrix(5, 1, -9, 9)
    _m4 = Matrix.random_int_matrix(1, 8, -9, 9)
    _m5 = Matrix.random_int_matrix(7, 7, -9, 9)
    _m5[1][1] = 2.+3.j
    _m_identity = Matrix.identity_matrix(5)
    print("M5---------------")
    print(_m5)
    print("det(m5)")
    print(_m5.determinant())

if __name__ == "__main__":
    main()
