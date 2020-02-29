using System;

namespace TestConsole
{

    class Program
    {
        static void Main(string[] args)
        {
            float[,] data = {{3, 2, 3}, {8, 12, -3}, {2, 3, 9}, {0, -1, 2}};
            Matrix<float> matrix = new Matrix<float>(data);

            System.Console.WriteLine(matrix.ToString());

            System.Console.WriteLine(matrix.Transpose().ToString());
            
            System.Console.WriteLine(matrix.SubMatrix(1, 1));

            int[,] data2 = {{1, 3, -4, 9, 1}, {-2, 4, 4, 5, 1}, {21, 3, 3, -2, 8}, {1, -12, 2, -16, 3}, {32, 16, 12, -45, -1}};
            Matrix<int> matrix_2 = new Matrix<int>(data2);

            System.Console.WriteLine(matrix_2);
            System.Console.WriteLine(matrix_2.Determinant());
        }
    }
}
