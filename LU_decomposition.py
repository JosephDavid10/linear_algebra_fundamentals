def lu_decomposition(matrix):
    """
    Computes the LU Decomposition of a matrix (P @ matrix = L @ U).
    
    Args:
        matrix (np.ndarray): A square numeric matrix.
        
    Returns:
        tuple: (L, U, P) matrices.
    """
    num_rows = len(matrix)
    U = matrix.copy()
    L = np.eye(num_rows)
    P = np.eye(num_rows)
    
    for idx, row in enumerate(U):
        pivot = row[idx]
        count = 0
        
        while pivot == 0:  # if pivot == 0 it switches rows to find a better candidate for a pivot
            count += 1
            
            if idx + count >= num_rows:
                raise ValueError("The matrix is singular and cannot be decomposed.")
    
            pivot_row = U[(idx + count)]
            pivot = pivot_row[idx]
            
            if pivot != 0:
                U[[idx, idx+count], :] = U[[idx+count, idx], :]
                P[[idx, idx+count], :] = P[[idx+count, idx], :]
                break
        
        for i in range(num_rows):  # Applies Gaussian elimination
            if i <= idx:
                continue
            else:
                factor = U[i, idx]/pivot
                U[i] -= U[idx]*factor
                L[i,idx] = factor
                
    return L, U, P
