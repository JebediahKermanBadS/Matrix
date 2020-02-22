"""A module for a matrix class
"""

import math
import cmath
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

    def copy(self):
        """TODO DOKU
        """
        result = Matrix(self.rows, self.columns)
        for row in range(self.rows):
            for col in range(self.columns):
                result[row][col] = self[row][col]
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

    def inverse(self):
        """TODO
        """
        if not self.is_square_matrix:
            raise Exception()

        result = self.copy()
        det = self.determinant()

        if self.rows == 1:
            result = 1 / det
        elif self.rows == 2:
            result[0][0] = self[1][1] / det
            result[0][1] /= -det
            result[1][0] /= -det
            result[1][1] = self[0][0] / det
        else:
            for row in range(self.rows):
                for col in range(self.columns):
                    co_m = Matrix(self.rows - 1, self.columns - 1)

                    for co_row in range(co_m.rows):
                        for co_col in range(co_m.columns):
                            _r = co_row
                            _c = co_col
                            if co_row >= row:
                                _r += 1
                            if co_col >= col:
                                _c += 1

                            co_m[co_row][co_col] = self[_r][_c]

                    factor = co_m.determinant()
                    if (col + row) % 2 == 1:
                        factor = -factor

                    result[row][col] = factor / det

        return result.transpose()


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

    def get_sub_matrix(self, row, column):
        """TODO DOKU
        """
        sub_matrix = Matrix(self.rows - 1, self.columns - 1)
        for _row in range(sub_matrix.rows):
            for _col in range(sub_matrix.columns):
                _r = _row
                _c = _col
                if _row >= row:
                    _r += 1
                if _col >= column:
                    _c += 1

                sub_matrix[_row][_col] = self[_r][_c]
        return sub_matrix

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
    _m6 = Matrix.random_int_matrix(3, 3, -9, 9)
    _m_identity = Matrix.identity_matrix(5)

def et_exercise36():
    """a
    """

    u_01 = 30
    u_02 = 90j
    r_1 = 100
    r_2 = 200
    x_l1 = 2 * math.pi * 1200 * 0.1j
    x_l2 = 2 * math.pi * 1200 * 0.68j
    x_c = - 1j/(2 * math.pi * 1200 * 300e-9)

    print(x_l1)
    print(x_l2)
    print(x_c)

    _d = Matrix(2, 2)
    _d[0][0] = r_1 + x_l1 + x_l2
    _d[0][1] = -x_l2
    _d[1][0] = -x_l2
    _d[1][1] = x_c + r_2 + x_l2

    im1 = Matrix(2, 2)
    im1[0][0] = u_01
    im1[0][1] = -x_l2
    im1[1][0] = -u_02
    im1[1][1] = x_c + r_2 + x_l2

    im2 = Matrix(2, 2)
    im2[0][0] = r_1 + x_l1 + x_l2
    im2[0][1] = u_01
    im2[1][0] = -x_l2
    im2[1][1] = -u_02

    print("-------------------------------------------------")
    print(im2)
    print(-u_02 * (r_1 + x_l1 + x_l2))
    print(x_l2 * u_01)
    print(f"R1 + XL1 + XL2 = {r_1 + x_l1 + x_l2}")
    print(f"Xc + R2 + XL2 = {x_c + r_2 + x_l2}")

    print("-------------------------------------------------")

    print(f"D = {_d.determinant():.3f}")
    print(f"det Im1 = {im1.determinant():.3f}")
    print(f"det Im2 = {im2.determinant():.3f}")

    print("-------------------------------------------------")

    _im1 = im1.determinant() / _d.determinant()
    _im2 = im2.determinant() / _d.determinant()
    print(f"im1 = {_im1:.5f}")
    print(f"im2 = {_im2:.5f}")
    print(f"im1 = {cmath.polar(_im1)}")
    print(f"im2 = {cmath.polar(_im2)}")
    print(f"im1 - im2 = {cmath.polar(_im1 - _im2)}")

    print("-------------------------------------------------")

    print(f"UL2 = {cmath.polar(_im1 * x_l1)}")

if __name__ == "__main__":
    main()
