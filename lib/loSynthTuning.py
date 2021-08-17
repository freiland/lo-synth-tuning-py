def primary_input():
    control = True
    while control: 
        try:
            result=float(input('enter a value for Primary Line Sky Frequency: '))
            
        except:
            print("Please enter a numerical value")
            continue
        else:
            print("Primary Line Sky Frequency is:", result,"GHz")
            cont_var= input('is this value correct? y/n ')
            if cont_var == 'y':
                control = False
            else:
                control = True
    return result

def secondary_input():
    control = True
    while control: 
        try:
            result=float(input('enter a value for Secondary Line Sky Frequency: '))
            
        except:
            print("Please enter a numerical value")
            continue
        else:
            print("Secondary Line Sky Frequency is:", result,"GHz")
            cont_var= input('is this value correct? y/n ')
            if cont_var == 'y':
                control = False
            else:
                control = True
    return result 

def center_input():
    control = True
    while control: 
        try:
            result=float(input('enter a value for Center IF Line Sky Frequency: '))
            
        except:
            print("Please enter a numerical value")
            continue
        else:
            print("Center IF Line Sky Frequency is:", result,"GHz")
            cont_var= input('is this value correct? y/n ')
            if cont_var == 'y':
                control = False
            else:
                control = True
    return result
            
    

def sideband_input():
    control = True 
    while control:
        try:
            sideband=str(input('Enter either L or U for sideband: '))
            sideband in ['L', 'l', 'U', 'u']
        except:
            print('enter either L or U for sideband value')
        else:
            print('Sideband value is', sideband)
            cont_var = input('Is this value correct? y/n: ')

            if cont_var == 'y':
                control = False
            else: 
                control = True
    return sideband

def higher_if(f_error, freq_if_center):
    print('Raise the IF Center Frequency by at least', f_error)
    print('IF Center Frequency step size is 5 MHz')
    new_if_center = float(input('raise if center by: '))
    
    

def lower_if(f_error, freq_if_center):
    print('Lower the IF Center Frequency by at least', f_error)
    print('IF Center Frequency step size is 5 MHz')
    new_if_center = float(input('lower if center by: '))
    freq_if_center = freq_if_center - new_if_center
    return freq_if_center
    

              
def synth():
    control = True  

    freq_p = primary_input()

    freq_sec = secondary_input()

    freq_if_center = center_input()

    sideband = sideband_input()

    f_synth_p  =    10.4 + freq_if_center

    f_delta = freq_p - freq_sec   

    while control:

        print(freq_p, freq_sec, freq_if_center, sideband)


        if sideband == 'U' or sideband == 'u':
            f_synth_sec =  f_synth_p  -  f_delta

            if f_synth_sec < 15.05 or f_synth_sec > 17.95:

                print('Secondary LO Synth tuning Out-of-Range')
                if f_synth_sec <  15.05:
                    f_error =  15.05 -  f_synth_sec
                    freq_if_center = higher_if(f_error, freq_if_center)
                    continue
                else:
                    f_error =  f_synth_sec - 17.95
                    freq_if_center = lower_if(f_error, freq_if_center)
                    continue
            else:
                print('Secondary LO synth is:', f_synth_sec, 'GHz')
                control = False
        else:
            f_synth_sec =  f_synth_p  +   f_delta
        
            if f_synth_sec < 15.05 or f_synth_sec > 17.95:
                print('Secondary LO Synth tuning Out-of-Range')
                if f_synth_sec <  15.05:
                    f_error =  15.05 -  f_synth_sec
                    higher_if(f_error, freq_if_center)
                    continue
                else:
                    f_error =  f_synth_sec - 17.95
                    lower_if(f_error, freq_if_center)
                    continue
            else:
                print('Secondary LO synth is:', f_synth_sec, 'GHz')
                control = False




