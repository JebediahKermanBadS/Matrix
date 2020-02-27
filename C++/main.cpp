#include "matrix.h"
#include <iostream>

int main()
{
    Matrix m1 = Matrix(3, 4);
    Matrix m2 = Matrix(4, 3);

    int32_t test_1[3][4] = {{1, 2, 3, 4}, {5, 4, 9, 1}, {7, 3, -2, 3}};
    int32_t* ptr_1_1[3];
    for (uint8_t i = 0; i < 3; i++)
        ptr_1_1[i] = test_1[i];

    int32_t** ptr_1_2 = ptr_1_1;
    m1.setValues(ptr_1_2);

    std::cout << m1.toString() << "------------------------------------------\n";

    int32_t test_2[4][3] = {{5, -3, 2}, {9, 1, -2}, {3, -4, 2}, {1, 2, 3}};
    int32_t* ptr_2_1[4];
    for (uint8_t i = 0; i < 4; i++)
        ptr_2_1[i] = test_2[i];

    int32_t** ptr_2_2 = ptr_2_1;
    m2.setValues(ptr_2_2);

    std::cout << m2.toString() << "------------------------------------------\n";

    Matrix m3 = m1 * m2;

    std::cout << m3.toString();

    return 0;
}