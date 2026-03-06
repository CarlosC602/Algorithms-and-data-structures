from typing import List
import string

class Matrix:
    def __init__(self, arg, val = 0):
        self.__matrix = []
        if isinstance(arg, tuple):
            rows, cols = arg
            for _ in range(rows):
                row_ = []
                for _ in range(cols):
                    row_.append(val)
                self.__matrix.append(row_)
        else:
            for row in arg:
                row_ = []
                for value in row:
                    row_.append(value)
                self.__matrix.append(row_)
    
    def size(self):
        rows = len(self.__matrix)
        cols = len(self.__matrix[0])
        return rows, cols
    
    def __getitem__(self, index):
        return self.__matrix[index]
    
    def __add__(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()
        if (r1, c1) != (r2, c2):
            return None
        
        result = Matrix((r1, c1))

        for i in range(r1):
            for j in range(c1):
                result[i][j] = self[i][j] + other[i][j]
        return result
    
    def __mul__(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()

        if c1 != r2:
            return None
        
        result = Matrix((r1,c2))

        for i in range(r1):
            for j in range(c2):
                suma = 0
                for k in range(c1):
                    suma += self[i][k] * other[k][j]
                result[i][j] = suma
        return result
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.size() != other.size():
            return False
        
        r,c = self.size()

        for i in range(r):
            for j in range(c):
                if self[i][j] != other[i][j]:
                    return False
        return True
    
    def __str__(self):
        result = ""
        for row in self.__matrix:
            result += "| "
            for elem in row:
                result += str(elem) + " "
            result += "|\n"
        return result
                
def transpose(matrix: Matrix):
    r,c = matrix.size()
    res = Matrix((c,r))
    for i in range(r):
        for j in range(c):
            res[j][i] = matrix[i][j]
    return res

def Chio(matrix: Matrix):
    multiplier = 1
    r,c = matrix.size()
    row_change = False
    if r != c:
        return None
    if r == 1:
        return matrix[0][0]
    if r == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    n = r    
    if matrix[0][0] == 0:
        for i in range(r):
            if matrix[i][0] != 0:
                for k in range(n):
                    matrix[i][k], matrix[0][k] = matrix[0][k], matrix[i][k]
                multiplier = -1
                row_change = True
                break
        if row_change == False:
            return 0
        
    matrix_1 = Matrix((n-1, n-1))
    
    for i in range(1,n):
        for j in range(1,n):
            matrix_1[i-1][j-1] = matrix[0][0] * matrix[i][j] - matrix[i][0] * matrix[0][j]

    return (Chio(matrix_1) * multiplier) / (matrix[0][0] ** (n-2))   
            


def main():
    m1 = Matrix([
                [5 , 1 , 1 , 2 , 3],
                [4 , 2 , 1 , 7 , 3],
                [2 , 1 , 2 , 4 , 7],
                [9 , 1 , 0 , 7 , 0],
                [1 , 4 , 7 , 2 , 2]
                ])
    
    m2 = Matrix([
                [0 , 1 , 1 , 2 , 3],
                [4 , 2 , 1 , 7 , 3],
                [2 , 1 , 2 , 4 , 7],
                [9 , 1 , 0 , 7 , 0],
                [1 , 4 , 7 , 2 , 2]
                ])
    
    m3 = Matrix([
                [0 , 0 , 0 , 0 , 0],
                [4 , 2 , 1 , 7 , 3],
                [2 , 1 , 2 , 4 , 7],
                [9 , 1 , 0 , 7 , 0],
                [1 , 4 , 7 , 2 , 2]
                ])
    
    m4 = Matrix([
                [0 , 1 , 1 , 2 , 3],
                [0 , 2 , 1 , 7 , 3],
                [0 , 1 , 2 , 4 , 7],
                [0 , 1 , 0 , 7 , 0],
                [0 , 4 , 7 , 2 , 2]
                ])


    print(Chio(m1))
    print(Chio(m2))
    print(Chio(m3))
    print(Chio(m4))

if __name__ == "__main__":
    main()