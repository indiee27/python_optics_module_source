def apply_filter(signal, Fs, cutoff, filter_type, zero_phase=False, transition_width=0.1, stop_band_atten=60, plot_filter=False):
    if plot_filter == True:
        cutoff_f_plot = cutoff
    
    if filter_type == 'Bandpass':
        func_filt_lp = apply_filter(signal, Fs)