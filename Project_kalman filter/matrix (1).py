import math
from math import sqrt
import numbers

def zeroes(height, width):
        
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):
   
   
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

   

    def determinant(self):
       
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant ")
        if self.h > 2:
            raise (NotImplementedError, " not implemented for matrices larger than 2x2.")
        if self.h == 1:
            return self.g[0][0]
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a*d - b*c
            
    def trace(self):
        
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a  matrix.")
        result = 0.0
   
        for i in range(self.h):
            result += self[i][i]
        return result
    def inverse(self):
        
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        det = self.determinant()
       
        if det == 0.:
            raise ValueError(' matrix- no inverse')

        if self.h == 1:
            inverse = [[1 / det]]
     
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]

            DR = 1.0 / det

            inverse = [[d * DR, -b * DR], [-c * DR, a * DR]]

        return Matrix(inverse)

    def T(self):
        
        matrix_transpose = []

        new_col_cnt = self.h
        new_row_cnt = self.w

        for i in range(new_row_cnt):
            new_row = []

            for j in range(new_col_cnt):
                new_row.append(self.g[j][i])

            matrix_transpose.append(new_row)

        return Matrix(matrix_transpose)

    def is_square(self):
        
        return self.h == self.w

    def __getitem__(self, idx):
        
        return self.g[idx]

    def __repr__(self):
        
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can be added if  dimensions are the same")

        result = []

        for row_a, row_b in zip(self.g, other.g):
            new_row = []
            for col_a, col_b in zip(row_a, row_b):
                new_row.append(col_a + col_b)
            result.append(new_row)

        return Matrix(result)

    def __neg__(self):
       

        result = []

        for row in self.g:
            new_row = []
            for col in row:
                new_row.append(-col)
            result.append(new_row)

        return Matrix(result)

    def __sub__(self, other):
        
        result = []
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can be subtracted if  dimensions are the same")

        for row_a, row_b in zip(self.g, other.g):
            new_row = []
            for col_a, col_b in zip(row_a, row_b):
                new_row.append(col_a - col_b)
            result.append(new_row)

        return Matrix(result)

    def __mul__(self, other):
       
        product = []

        transp_b = other.T()

        if self.w != other.h:   
            raise (ValueError, "Matrices can only be multiplied if the own row count matches  column ")

        for row_index in range(self.h):
            new_row = []

            for col_index in range(transp_b.h):
                # calculate dot product of both given vectors
                result = 0.
                for a, b in zip(self.g[row_index], transp_b.g[col_index]):
                    result += a * b

                new_row.append(result)

            product.append(new_row)

        return Matrix(product)

    def __rmul__(self, other):
        
        if isinstance(other, numbers.Number):
            result = []
            for row in self.g:
                new_row = []
                for col in row:
                    new_row.append(col*other)
                result.append(new_row)
            return Matrix(result)
            

