
MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0
def get_planet_weight():
    while True:
        try:
            weight_on_earth = float(input("\nPlease enter the weight on Earth : "))
            break
        except ValueError as e:
            print(f"\033[1;31mInvalid input!\033[0m {e} Please enter a valid weight in number.")  
    
    planet = input("\nPlease enter the planet. ").lower()
    while planet != "mercury" and planet != "venus" and planet != "mars" and planet != "jupiter" and planet != "saturn" and planet != "uranus" and planet != "neptune" and planet != "earth":
        planet = input("\033[1;31mInvalid input!\033[0m Please enter a valid planet name (mercury, venus, mars, jupiter, saturn, uranus, neptune, earth). ").lower()
    
    
    if planet  == "mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "mars":  
        gravity_constant = MARS_GRAVITY
    elif planet == "jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "neptune":
        gravity_constant = NEPTUNE_GRAVITY
    elif planet == "earth":
        gravity_constant = EARTH_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY
    
    weight_on_planet = weight_on_earth * gravity_constant
    rounded_weight_on_planet = round(weight_on_planet, 2)
    print(f"\n\033[1;35m Weight on {planet.upper()} : \033[0m{rounded_weight_on_planet} .")

if __name__ == "__main__":
    get_planet_weight()