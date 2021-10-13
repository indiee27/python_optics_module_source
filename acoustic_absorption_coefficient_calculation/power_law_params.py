from acoustic_absorption_coefficient_calculation.neper_to_db import neper_to_db
from acoustic_absorption_coefficient_calculation.db_to_neper import db_to_neper
import math
import scipy.optimize
import matplotlib.pyplot as plt

def abs_func(trial_vals):
    a0_np_trial = trial_vals[0]
    y_trial = trial_vals[1]

    actual_absorption = a0_np_trial * math.pow(w, y_trial)/(1 - (y_trial + 1) * a0_np_trial * c0 * math.tan(math.pi * y_trial/2) * math.pow(w, (y_trial-1)))

    absorption_error = math.sqrt(sum(math.pow((desired_absorption - actual_absorption),2)))

    return absorption_error

def fit_power_law_params(a0, y, c0, f_min, f_max, plot_fit=False):

    f = get_spaced_points(f_min, f_max, 200)
    w = 2 * math.pi * f

    a0_np = db_to_neper(a0, y)

    desired_absorption = a0_np * w * y

    vals = scipy.optimize.fmin(func=abs_func(a0_np, y))

    a0_np_fit = vals[0]
    y_fit = vals[1]

    a0_fit = neper_to_db(a0_np_fit, y_fit)

    if plot_fit==True:
        absorption_wo_fit = a0_np * math.pow(w,y)/(1 - (y+1) * a0_np * c0 * math.tan(math.pi*y/2) * math.pow(w,(y-1)))
        absorption_fit = a0_np_fit * math.pow(w,y_fit)/(1 - (y_fit+1) * a0_np_fit * c0 * math.tan(math.pi*y_fit/2) * math.pow(w,(y_fit-1)))

        conv_factor = (0.01 * 20 * math.log10(math.exp(1)))
        desired_absorption = desired_absorption * conv_factor
        absorption_wo_fit = absorption_wo_fit * conv_factor
        absorption_fit = absorption_fit * conv_factor

        [x_sc, scale, prefix, prefix_fullname] = scaleSI(f[-1])

        ds = 5

        plt.figure()
        plt.plot(f*scale, desired_absorption)
        plt.plot(f*scale, absorption_wo_fit)
        plt.plot(f[1:ds:-1]*scale, absorption_fit[1,ds,-1])
        plt.xlabel(f"Frequency [{prefix} Hz]")
        plt.ylabel("Absorption [dB/cm]")
        plt.legend("Desired Power Law Absorption", "Actual Absorption Using Original Values", "Actual Absorption Using Fitted Values")
        plt.title(f"Fitted Absorption Values: alpha_0 = {a0_fit}, y = {y_fit}")

    return a0_fit, y_fit

