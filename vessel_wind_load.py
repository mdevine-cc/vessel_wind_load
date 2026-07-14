
#Inputs: Design wind speed, vessel length, shielding factor, direction factor, 

#CALCULATIONS
def check_vessel_dimensions(vessel_length_ft) -> None: # Upper limit 300 ft, anything larger is not represented by approximation formulas
    if(vessel_length_ft <=0):
        raise ValueError("Error: Invalid Vessel Length")
    elif(vessel_length_ft > 300):
        raise ValueError("Error: Vessel Length too large")
    
def check_shielding_factor(shielding_factor) -> None: # Tobiasson & Kollmeyer, 15-4
    if((shielding_factor > 1.0) or (shielding_factor < 0.3)):
        raise ValueError("Error: Invalid Shielding Factor")

def check_direction_factor(direction_factor) -> None: # Tobiasson & Kollmeyer, 15-3
    if((direction_factor < 1.0) or (direction_factor > 3.5)):
        raise ValueError("Error: Invalid Direction Factor")


def calculate_vessel_beam(vessel_length_ft) -> float: # Tobiasson & Kollmeyer
    check_vessel_dimensions(vessel_length_ft)
    if(vessel_length_ft >= 120):
        return 1.1*(vessel_length_ft ** 0.7)
    else:
        return 0.9*(vessel_length_ft ** 0.7)    
    

def calculate_vessel_height(vessel_length_ft) -> float: # Tobiasson & Kollmeyer
    check_vessel_dimensions(vessel_length_ft)
    if(vessel_length_ft <= 55):
        return (0.179429*vessel_length_ft) + 0.438095
    else:
        return (0.074049*vessel_length_ft) + 6.811872

def calculate_vessel_draft(vessel_length_ft) -> float: # Tobiasson & Kollmeyer
    check_vessel_dimensions(vessel_length_ft)
    if(vessel_length_ft >= 120):
        return 0.3*(vessel_length_ft ** 0.7)
    else:
        return 0.25*(vessel_length_ft ** 0.7)    

def calculate_end_area(vessel_length_ft) -> float:
    check_vessel_dimensions(vessel_length_ft)
    beam_ft = calculate_vessel_beam(vessel_length_ft)
    height_above_waterline_ft = calculate_vessel_height(vessel_length_ft)
    return beam_ft*height_above_waterline_ft


def calculate_wind_force(vessel_length_ft, direction_factor,  shielding_factor, design_wind_speed_mph) -> float:
    #Check Inputs
    check_vessel_dimensions(vessel_length_ft)
    check_direction_factor(direction_factor)
    check_shielding_factor(shielding_factor)


    #Calculate Force
    vessel_end_area_m2 = (0.09290304)*calculate_end_area(vessel_length_ft)
    # print("area m^2: ", vessel_end_area_m2)
    design_wind_speed_ms = design_wind_speed_mph/(2.236936)
    # print("wind speed m/s", design_wind_speed_ms)
    wind_force_N = 0.72*(vessel_end_area_m2)*(direction_factor)*(shielding_factor)*(design_wind_speed_ms**2) # Tobiasson, 15.3
    # print("wind force N: ",wind_force_N)
    wind_force_kips = (0.000224809)*wind_force_N
    # print("wind force kips: ",wind_force_kips)
    return wind_force_kips

