from typing import List

class Matrix:
    def __init__(self, arg, val = 0):
        if isinstance(arg, tuple):
            rows, cols = arg
            for _ in range(cols):
                for _ in range(rows):
                    self.__matrix = val
        else:
            for value in range(row):
                for row in range(arg):
                    self.__matrix = value

        self.rows = rows
        self.cols = cols
    
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
                result[i,j] = self[i,j] + other[i,j]
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
                    suma += self[i,k] * other[k,j]
                result[i,j] = suma
        return result
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.size() != other.size():
            return False
        
        r,c = self.size()

        for i in range(r):
            for j in range(c):
                if self[i,j] != other[i,j]:
                    return False
        return True
    
    def
                
def transpose(matrix: Matrix):
    r,c = matrix.size()
    res = Matrix((c,r))
    for i in range(r):
        for j in range(c):
            res[i,j] = matrix[j,i]
    return res