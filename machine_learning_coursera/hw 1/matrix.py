from sys import stdin
from copy import deepcopy

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)
    
    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

x = Matrix([[1,2,3],[4 ,5,6],[7 ,8,9]]) 
y = Matrix([[9,8,7],[6,5,4],[3,2,1]])  
res = x+y
for r in res:
    print(r)