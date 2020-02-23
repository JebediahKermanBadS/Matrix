"""Module
"""

# import math
# import cmath
from matrix import Matrix


def main():
    """Main method
    """

    _m1 = Matrix().random_int_matrix(3, 5, -9, 9)
    # _m2 = Matrix().random_int_matrix(1, 8, -9, 9)
    # _m3 = Matrix().random_int_matrix(5, 1, -9, 9)
    # _m4 = Matrix().random_int_matrix(1, 8, -9, 9)
    # _m5 = Matrix().random_int_matrix(7, 7, -9, 9)
    # _m6 = Matrix().random_int_matrix(4, 4, -9, 9)
    # _m_identity = Matrix.identity_matrix(5)

    print(_m1)


"""
def math_6a():

    _f = Matrix(4, 4)
    _f.values = [[1, 1, 2, -1], [0, 1, 0, 3], [0, 0, 2, 0], [0, 0, 0, 0]]

    _g = Matrix(2, 4)
    _g.values = [[1, -1, 1, -1], [1, 1, -1, -1]]

    _h = Matrix(3, 2)
    _h.values = [[1, 0], [1, 1], [1, -1]]

    _k = Matrix(4, 3)
    _k.values = [[1, 1, 0], [0, 1, -1], [1, 1, 0], [1, 1, -3]]


    _u = Matrix(4, 1)
    _u.values = [[2], [1], [3], [-1]]

    _v = Matrix(4, 1)
    _v.values = [[1], [2], [3], [4]]

    _w = Matrix(2, 1)
    _w.values = [[1], [-1]]

    print("2) --------------------")
    print(_f * _u)
    print("-----------------------")
    print(_g * _v)
    print("-----------------------")
    print(_h * _w)

    print("3) --------------------")
    print(_g * _f)
    print("-----------------------")
    print(f"H * G =\n{_h * _g}")
    print(f"K * H * G =\n{_k * _h * _g}")
    print("-----------------------")
    print(_h * _w)

def et_exercise36():
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
"""
if __name__ == "__main__":
    main()
