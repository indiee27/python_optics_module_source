import math
import numpy as np

def power_law_kramers_kronig(w, w0, c0, a0, y):
    if y >= 3 or y <= 0:
        print('WARNING: y must be 0 < y < 3.')
        c_kk = c0 * np.ones(w)
    
    elif y == 1:
        c_kk = 1 / (1 / c0 - 2 * a0 * math.log(w/w0) / math.pi)
    
    else:
        c_kk = 1 / (1 / c0 + a0 * math.tan(y * math.pi / 2) * (math.pow(w,(y-1)) - math.pow(w0, (y-1))))

    return c_kk   
