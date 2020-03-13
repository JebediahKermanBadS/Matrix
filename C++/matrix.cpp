#include "matrix.h"
#include <iostream>
#include <bits/stdc++.h>

Matrix::Matrix(uint8_t m, uint8_t n)
    : m(m), n(n)
{
    this->rows = m;
    this->cols = n;

    values = new int32_t* [rows];

    for (uint8_t row = 0; row < m; row++)
    {
        values[row] = new int32_t[n];

        for (uint8_t col = 0; col < n; col++)
        {
            values[row][col] = 0;
        }
    }
}

Matrix::~Matrix()
{

}

void Matrix::setValues(int32_t **values)
{
    for (uint8_t row = 0; row < rows; row++)
    {
        for (uint8_t col = 0; col < cols; col++)
        {
            this->values[row][col] = values[row][col];
        }
    }
}

Matrix Matrix::transpose() const
{
    Matrix result = Matrix(cols, rows);
    for (size_t row = 0; row < rows; row++)
    {
        for (size_t col = 0; col < cols; col++)
        {
            result[col][row] = values[row][col];   
        }
    }
    return result;
}

bool Matrix::isSquareMatrix() const
{
    return m == n;
}

bool Matrix::isSizeEqual(const Matrix *matrix) const
{
    return m == matrix->m && n == matrix->n;
}

int32_t Matrix::getTrace()
{
    int32_t trace = 0;
    if (isSquareMatrix())
    {
        for (uint8_t i = 0; i < m; i++)
        {
            trace += values[i][i];
        }
    }
    return trace;
}

int32_t Matrix::getDeterminant()
{
    return 0;
}

std::string Matrix::toString()
{
    std::ostringstream s;
    for (uint8_t row = 0; row < rows; row++)
    {
        s << "[ ";
        for (uint8_t col = 0; col < cols; col++)
        {
            s << values[row][col] << " ";
        }
        s << "]\n";
    }
    return s.str();
}

Matrix Matrix::copy(const Matrix &m1)
{
    return nullMatrix(0, 0);
}

Matrix Matrix::nullMatrix(uint8_t rows, uint8_t cols)
{
    return Matrix(rows, cols);
}

Matrix Matrix::identityMatrix(uint8_t m)
{
    Matrix matrix = Matrix(m, m);
    for (size_t i = 0; i < m; i++)
        matrix[i][i] = 1;
    return matrix;
}

Matrix operator+(const Matrix &m1, const int32_t scalar)
{
    Matrix m = Matrix(m1.rows, m1.cols);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.cols; col++)
        {
            m[row][col] = m1[row][col] + scalar;       
        }
    }
    return m;
}

Matrix operator+(const Matrix &m1, const Matrix &m2)
{
    if (m1.isSizeEqual(&m1))
    {
        Matrix m = Matrix(m1.rows, m1.cols);
        for (uint8_t row = 0; row < m1.rows; row++)
        {
            for (uint8_t col = 0; col < m1.cols; col++)
            {
                m[row][col] = m1[row][col] + m2[row][col];
            }
        }
        return m;
    }
    else
    {
        return Matrix(0, 0);   
    }
}

Matrix operator+=(Matrix &m1, const int32_t scalar)
{
    return m1 = m1 + scalar;
}

Matrix operator+=(Matrix &m1, const Matrix &m2)
{
    return m1 = m1 + m2;
}

Matrix operator-(const Matrix &m1)
{
    Matrix m = Matrix(m1.rows, m1.cols);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.cols; col++)
        {
            m[row][col] = -(m1[row][col]);
        }
    }
    return m;
}

Matrix operator-(const Matrix &m1, const int32_t scalar)
{
    Matrix m = Matrix(m1.rows, m1.cols);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.cols; col++)
        {
            m[row][col] = m1[row][col] - scalar;
        }
    }
    return m;
}

Matrix operator-(const Matrix &m1, const Matrix &m2)
{
    Matrix m = -m2;
    return m + m1;
}

Matrix operator-=(Matrix &m1, const int32_t scalar)
{
    return m1 = m1 - scalar;
}

Matrix operator-=(Matrix &m1, const Matrix &m2)
{
    return m1 = m1 - m2;
}

Matrix operator*(const Matrix &m1, const int32_t scalar)
{
    Matrix m = Matrix(m1.rows, m1.cols);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.cols; col++)
        {
            m[row][col] = m1[row][col] * scalar;
        }
    }
    return m;
}

Matrix operator*(const Matrix &m1, const Matrix &m2)
{
    if (m1.cols == m2.rows)
    {
        Matrix m = Matrix(m1.rows, m2.cols);
        for (uint8_t row = 0; row < m.rows; row++)
        {
            for (uint8_t col = 0; col < m.cols; col++)
            {
                for (uint8_t i = 0; i < m1.cols; i++)
                {
                    m[row][col] += m1[row][i] * m2[i][col];
                }
                
            }
            
        }
        return m;
    }
    else
    {
        return Matrix(0, 0);
    }
    
}

Matrix operator*=(Matrix &m1, const int32_t scalar)
{
    return m1 = m1 * scalar;
}
