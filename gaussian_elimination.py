def gaussian_elimination(matrix, vector):
    vector = vector.reshape(-1,1)
    ext_matrix = np.hstack((matrix, vector)) #  Creates an extended matrix
    
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
                
        ext_matrix[idx] = ext_matrix[idx]/pivot  # pivot normalization
        pivot = ext_matrix[idx, idx]
        
        for i in range(len(ext_matrix)):  # Applies Gauss-Jordan elimination
            if i <= idx:
                continue
            else:
                factor = ext_matrix[i, idx]
                ext_matrix[i] -= ext_matrix[idx]*factor
                
    return ext_matrix 
