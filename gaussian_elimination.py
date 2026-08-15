import numpy as np
def gaussian_elimination(matrix, vector=None):

    matrix = matrix.astype(float)
    ext_matrix = matrix.astype(float) 
    
    if vector is not None:
        vector = vector.reshape(-1,1)
        ext_matrix = np.hstack((matrix, vector)).astype(float)  #  Creates an extended matrix
    
    for idx, row in enumerate(ext_matrix):
        pivot = row[idx]
        count = 0
        
        while pivot == 0:  # if pivot == 0 it switches rows to find a better candidate for a pivot
            count += 1
            
            if idx + count >= len(matrix):
                print('ERROR! SINGULAR MATRIX')
                break
    
            pivot_row = ext_matrix[(idx + count)]
            pivot = pivot_row[idx]
            
            if pivot != 0:
                ext_matrix[[idx, idx+count]] = ext_matrix[[idx+count, idx]]
                break
                
        pivot = ext_matrix[idx, idx]
        
        for i in range(len(ext_matrix)):  # Applies Gaussian elimination
            if i <= idx:
                continue
            else:
                factor = ext_matrix[i, idx]/pivot
                ext_matrix[i] -= ext_matrix[idx]*factor
                
    return ext_matrix 
