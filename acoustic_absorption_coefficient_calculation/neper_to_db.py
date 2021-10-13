import math

def neper_to_db(attenuation, number=1):
    '''
    Convert nepers to decibel values
    
    INPUTS: attentuation - dB/(MHz^y cm)
            y - power law exponent (default = 1)
    
    OUTPUTS:alpha - attenuation in Nepers/((rad/s)^y m)  
    '''
    
    alpha = (20 * math.log10(math.exp(1))) * attenuation * (math.pow((1e-6 * 2 * math.pi),number))/100

    return alpha