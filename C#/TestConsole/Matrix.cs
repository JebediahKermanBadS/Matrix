using System;

namespace TestConsole
{
    public class Matrix<T> where T : IComparable<T>
    {
        private readonly uint m;
        private readonly uint n;
        private T[,] data;

        public Matrix(uint m, uint n)
        {
            this.m = m;
            this.n = n;

            data = new T[m, n];
        }

        public Matrix(T[,] data)
        {
            m = (uint)data.GetLength(0);
            n = (uint)data.GetLength(1);
        
            this.data = data;
        }

        public dynamic Trace()
        {
            if (IsSquareMatrix())
            {
                dynamic trace = 0;
                for (int i = 0; i < m; i++)
                {
                    trace += data[i, i];
                }
                return trace;
            }
            else
                throw new NotImplementedException();
        }

        public dynamic Determinant()
        {
            if (IsSquareMatrix())
            {
                dynamic det = 0;

                switch (m)
                {
                    case 0: 
                        return 0;
                    
                    case 1:
                        return data[0, 0];

                    case 2:
                        return (dynamic)data[0, 0] * (dynamic)data[1, 1] - (dynamic)data[0, 1] * (dynamic)data[1, 0];

                    default:
                        for (int row = 0; row < m; row++)
                        {
                            int factor = (dynamic)data[row, 0];
                            if (row % 2 == 1)
                                factor = -factor;

                            Matrix<T> subMatrix = SubMatrix(row, 0);
                            det += subMatrix.Determinant() * factor;
                        }
                        return det;
                }
            }
            else
                throw new NotImplementedException();
        }

        public Matrix<T> SubMatrix(int row, int col)
        {
            Matrix<T> subMatrix = new Matrix<T>(m - 1, n - 1);
            for (int i = 0; i < subMatrix.m; i++)
            {
                for (int j = 0; j < subMatrix.n; j++)
                {
                    int r = i, c = j;
                    if (i >= row)
                        r++;
                    if (j >= col)
                        c++;

                    subMatrix[i, j] = data[r, c];
                }
            }
            return subMatrix;
        }

        public Matrix<T> Transpose()
        {
            Matrix<T> matrix = new Matrix<T>(n, m);
            for (int row = 0; row < m; row++)
            {
                for (int col = 0; col < n; col++)
                {
                    matrix[col, row] = this[row, col];
                }
            }
            return matrix;
        }

        bool IsSquareMatrix() =>
            m == n;

        bool IsSizeEqual(Matrix<T> matrix) =>
            m == matrix.m && n == matrix.n;

        public override string ToString()
        {
            string s = string.Empty;
           
            for (int row = 0; row < m; row++)
            {
                s += "";
                for (int col = 0; col < n; col++)
                {
                    s += $"{data[row, col].ToString(), 3} ";                    
                }
                s += "\n";
            }
            return s;
        }
    
        public T this[int row, int col]
        {
            get { return data[row, col]; }
            set { data[row, col] = value; }
        }
    }
}
