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
            
        except:
            print('Please choose L or U for Sideband input')
        else:
            print('Sideband value is', sideband)
            cont_var = input('Is this value correct? y/n: ')

            if cont_var == 'y':
                control = False
            else: 
                control = True
    return sideband

def higher_if(f_error, freq_if_center):
    print('Raise the IF Center Frequency by at least', f_error, 'GHz')
    print('IF Center Frequency step size is 5 MHz')
      

def lower_if(f_error, freq_if_center):
    print('Lower the IF Center Frequency by at least', f_error, 'GHz')
    print('IF Center Frequency step size is 5 MHz')
                 
def synth():
    control = True  

    freq_p = primary_input()

    freq_sec = secondary_input()

    freq_if_center = center_input()

    sideband = sideband_input()

    
    while control:

        f_synth_p  =    10.4 + freq_if_center

        f_delta = freq_p - freq_sec  

        print(freq_p, freq_sec, freq_if_center, sideband, f_synth_p, f_delta)


        if sideband == 'U' or sideband == 'u':
            f_synth_sec =  f_synth_p  -  f_delta

            if f_synth_sec < 15.05 or f_synth_sec > 17.95:

                print('Secondary LO Synth tuning Out-of-Range')
                if f_synth_sec <  15.05:
                    f_error =  15.05 -  f_synth_sec
                    higher_if(f_error, freq_if_center)
                    while True:
                        try:
                            freq_if_center = float(input('enter a new value for IF Center frequency: '))
                            break
                        except: 
                            print('Please enter a numerical value for IF Center Frequency: ')
                            continue
                        
                    continue
                else:
                    f_error =  f_synth_sec - 17.95
                    lower_if(f_error, freq_if_center)
                    while True:
                        try:
                            freq_if_center = float(input('enter a new value for IF Center frequency: '))
                            break
                        except: 
                            print('Please enter a numerical value for IF Center Frequency: ')
                            continue
                    continue

            else:
                print('Secondary LO synth is:', f_synth_sec, 'GHz')
                control = False

        elif sideband == 'L' or sideband == 'l':

            f_synth_sec =  f_synth_p  +   f_delta
        
            if f_synth_sec < 15.05 or f_synth_sec > 17.95:
                print('Secondary LO Synth tuning Out-of-Range')
                if f_synth_sec <  15.05:
                    f_error =  15.05 -  f_synth_sec
                    higher_if(f_error, freq_if_center)
                    while True:
                        try:
                            freq_if_center = float(input('enter a new value for IF Center frequency: '))
                            break
                        except: 
                            print('Please enter a numerical value for IF Center Frequency: ')
                            continue
                    continue
                else:
                    f_error =  f_synth_sec - 17.95
                    lower_if(f_error, freq_if_center)
                    while True:
                        try:
                            freq_if_center = float(input('enter a new value for IF Center frequency: '))
                            break
                        except: 
                            print('Please enter a numerical value for IF Center Frequency: ')
                            continue
                    continue
            else:
                print('Secondary LO synth is:', f_synth_sec, 'GHz')
                control = False




