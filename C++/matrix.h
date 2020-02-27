#ifndef _MATRIX_H_
#define _MATRIX_H_

#include <string>
#include <stdint.h>

class Matrix
{
    public:
        Matrix(uint8_t rows, uint8_t columns);
        ~Matrix();

        void setValues(int32_t **values);
        Matrix copy();

        bool isSizeEqual(const Matrix *matrix) const;
        std::string toString();

        friend Matrix operator+(const Matrix &m1, const int32_t scalar);
        friend Matrix operator+(const Matrix &m1, const Matrix &m2);
        friend Matrix operator+=(Matrix &m1, const int32_t scalar);
        friend Matrix operator+=(Matrix &m1, const Matrix &m2);

        friend Matrix operator-(const Matrix &m1);
        friend Matrix operator-(const Matrix &m1, const int32_t scalar);
        friend Matrix operator-(const Matrix &m1, const Matrix &m2);
        friend Matrix operator-=(Matrix &m1, const int32_t scalar);
        friend Matrix operator-=(Matrix &m1, const Matrix &m2);

        friend Matrix operator*(const Matrix &m1, const int32_t scalar);
        friend Matrix operator*(const Matrix &m1, const Matrix &m2);        
        friend Matrix operator*=(Matrix &m1, const int32_t scalar);

        int32_t *operator [](int i) const { return values[i]; }

    private:
        uint8_t rows;
        uint8_t columns;

        int32_t **values;
};

#endif