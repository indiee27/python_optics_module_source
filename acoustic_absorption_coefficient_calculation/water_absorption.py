from numpy.core.fromnumeric import reshape
import math

def water_absorption(f,T):
    if all(T) < 0 or all(T) > 60:
        print("WARNING: Temp outside experimental range")
    
    NEPER2DB = 8.686

    a_0 = 56.723531840522710
    a_1 = -2.899633796917384
    a_2 = 0.099253401567561
    a_3 = -0.002067402501557
    a_4 = 2.189417428917596e-005
    a_5 = -6.210860973978427e-008
    a_6 = -6.402634551821596e-010
    a_7 = 3.869387679459408e-012

    T = reshape(T, [1, len(T)])
    f = reshape(f, [len(f), 1])

    a_on_fsqr = (a_0 + a_1*T + math.pow(a_2*T,2) + math.pow(a_3*T,3) + math.pow(a_4*T,4) + math.pow(a_5*T,5) + math.pow(a_6*T,6) + math.pow(a_7*T,7)) * 1e-17

    abs = NEPER2DB * 1e12 * math.pow(f,2) * a_on_fsqr

    return abs