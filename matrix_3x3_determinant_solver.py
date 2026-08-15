import numpy as np

def matrix_det(matrix):
    plus = 0.0
    minus = 0.0

    if len(matrix) != len(matrix.T):
        print('Error. Non-squared matrix has no determinant.')
        return np.nan
        
    else:
        if len(matrix) == 2:    #2x2 matrix
            plus = matrix[0,0]*matrix[1,1]
            minus = matrix[1,0]*matrix[0,1]
            
        else: 
            for i in range(len(matrix)):  #3x3 matrix
                positive_term = 1.0
                negative_term = 1.0
                
                for j in range(len(matrix)):
                    d = (i + j) % len(matrix) 
                    positive_term *= matrix[j, d]
                    negative_term *= matrix[j, i-j]
                    
                plus += positive_term
                minus += negative_term

        return plus - minus
