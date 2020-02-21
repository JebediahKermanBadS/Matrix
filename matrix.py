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

    def __getitem__(self, key):
        return self.values[key]

    def __str__(self):
        _s = ""
        for column in self.values:
            _s += f"{column}\n"
        return _s[:-1]

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

    def matrix_size_equal(self, _m1):
        """Check if the size of 2 matrix is equal.
        Arguments:
            m1 {Matrix()} -- The matrix to check
        Returns:
            bool -- True if the size of them is equal. False if not.
        """
        return self.rows == _m1.rows and self.columns == _m1.columns

def main():
    """Main method
    """
    _m1 = Matrix(4, 5)
    _m2 = Matrix(1, 5)
    _m3 = Matrix(5, 1)
    print("M1---------------")
    print(_m1)
    print("M2---------------")
    print(_m2)
    print("M3---------------")
    print(_m3)
    print("M2 * M3---------------")
    print(_m3 * _m2)

if __name__ == "__main__":
    main()
