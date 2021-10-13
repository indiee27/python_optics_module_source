import math

def db_to_neper(attenuation, number):
    '''
    Convert decibel values to nepers
    
    INPUTS: attentuation - dB/(MHz^y cm)
            y - power law exponent (default = 1)
    
    OUTPUTS:alpha - attenuation in Nepers/((rad/s)^y m)  
    '''
    
    if number == False:
        number = 1
    
    alpha = 100 * attenuation * math.pow((1e-6/(2*math.pi)),number)/(20 * math.log10(math.exp(1)))

    return alpha

    