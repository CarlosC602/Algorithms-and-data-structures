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

def main():
    m1 = Matrix([[1,0,2],[-1,3,1]])
    m2 = Matrix((2,3), 1)
    m3 = Matrix([[3,1],[2,1],[1,0]])
    print(transpose(m1))
    print(m1 + m2)
    print(m1 * m3)

if __name__ == "__main__":
    main()