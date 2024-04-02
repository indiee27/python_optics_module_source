# func for solving Pennes model

def bioheat(T0, S, material, dx, t):

    if len(T0) == 1:
        error_message = "T0 must be a matrix"
        raise ValueError(error_message)
    
    if (len(S) == 1) and (S == 0) and (S.shape != T0.shape):
        error_message = "T0 and S must be the same size"
        raise ValueError(error_message)
        