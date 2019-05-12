#linal hints
import numpy as np
import numpy.linalg as nplin

matrix = np.array([[5, 3, -8, -4],
                   [7.5, 0.5, -1, -7],
                   [-2.5, 1.5, -4, 1],
                   [10, -3, 8, -8]])

print(round(nplin.det(matrix), 3)) #solve the inaccuracy 23
#the answer should be equal to 15
