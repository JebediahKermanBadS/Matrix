#ifndef _MATRIX_H_
#define _MATRIX_H_

#include <string>
#include <stdint.h>

class Matrix
{
    public:
        Matrix(uint8_t m, uint8_t n);
        ~Matrix();
        
        void setValues(int32_t **values);
        bool isSquareMatrix() const;
        bool isSizeEqual(const Matrix *matrix) const;
        
        int32_t getTrace();
        int32_t getDeterminant();

        Matrix transpose() const;

        std::string toString();

        static Matrix copy(const Matrix &m1);
        static Matrix nullMatrix(uint8_t rows, uint8_t cols);
        static Matrix identityMatrix(uint8_t m);

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
        uint8_t cols;
        uint8_t m;
        uint8_t n;
        
        int32_t **values;
};

#endif