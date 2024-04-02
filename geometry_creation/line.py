
def make_line(Nx, Ny, startpoint, endpoint, angle, length):
    
    if len(startpoint)!=2:
        error_message = "Start point should be a two element vector"
        raise ValueError(error_message)
    
    if (sum(startpoint < 1) > 0) or (startpoint[0] > Nx) or (startpoint[1] > Ny):
        error_message = f"The starting point must lie within the grid, between [1 1] and [{Nx} {Ny}]."
        raise ValueError(error_message)


Ny = [(1, 2), (2, 2)]

print((Ny[0][0]))