#include "matrix.h"
#include <iostream>
#include <bits/stdc++.h>

Matrix::Matrix(uint8_t rows, uint8_t columns)
{
    this->rows = rows;
    this->columns = columns;

    values = new int32_t* [rows];

    for (uint8_t row = 0; row < rows; row++)
    {
        values[row] = new int32_t[columns];

        for (uint8_t col = 0; col < columns; col++)
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
        for (uint8_t col = 0; col < columns; col++)
        {
            this->values[row][col] = values[row][col];
        }
    }
}

bool Matrix::isSizeEqual(const Matrix *matrix) const
{
    return this->rows == matrix->rows && this->columns == matrix->columns;
}

std::string Matrix::toString()
{
    std::ostringstream s;
    for (uint8_t row = 0; row < rows; row++)
    {
        s << "[ ";
        for (uint8_t col = 0; col < columns; col++)
        {
            s << values[row][col] << " ";
        }
        s << "]\n";
    }
    return s.str();
}

Matrix operator+(const Matrix &m1, const int32_t scalar)
{
    Matrix m = Matrix(m1.rows, m1.columns);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.columns; col++)
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
        Matrix m = Matrix(m1.rows, m1.columns);
        for (uint8_t row = 0; row < m1.rows; row++)
        {
            for (uint8_t col = 0; col < m1.columns; col++)
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
    Matrix m = Matrix(m1.rows, m1.columns);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.columns; col++)
        {
            m[row][col] = -(m1[row][col]);
        }
    }
    return m;
}

Matrix operator-(const Matrix &m1, const int32_t scalar)
{
    Matrix m = Matrix(m1.rows, m1.columns);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.columns; col++)
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
    Matrix m = Matrix(m1.rows, m1.columns);
    for (uint8_t row = 0; row < m.rows; row++)
    {
        for (uint8_t col = 0; col < m.columns; col++)
        {
            m[row][col] = m1[row][col] * scalar;
        }
    }
    return m;
}

Matrix operator*(const Matrix &m1, const Matrix &m2)
{
    if (m1.columns == m2.rows)
    {
        Matrix m = Matrix(m1.rows, m2.columns);
        for (uint8_t row = 0; row < m.rows; row++)
        {
            for (uint8_t col = 0; col < m.columns; col++)
            {
                for (uint8_t i = 0; i < m1.columns; i++)
                {
                    m[row][col] += m1[row][i] * m2[i][col];
                }
                
            }
            
        }
        return m;
    }
}

Matrix operator*=(Matrix &m1, const int32_t scalar)
{
    return m1 = m1 * scalar;
}
