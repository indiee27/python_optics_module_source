from acoustic_absorption_coefficient_calculation.db_to_neper import db_to_neper
import numpy as np

def attenuation_comp(signal, dt, c, alpha_0, y, varargin):

    PLOT_DNR = 40
    PLOT_RANGE_MULT = 1.5

    signal = np.transpose(signal)
    [N, num_signals] = np.shape(signal)

    alpha_0 = db_to_neper(alpha_0, y)

    Fs = 1 / dt

    t_array = dt * 
    return signal, tfd, cutoff_freq