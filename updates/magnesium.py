def monitor():

    maglvl_low = 1250
    maglvl_high = 1350


    current = get_magnesium_level()
    mesg = "Magnesium level OK"

    if (current < maglvl_low):
      print("Magnesium level too low!")
    elif (current > maglvl_high):
      print("Magnesium level too high!")
    else:
      print("Magnesium level is normal.")
      
# Function to simulate actual fish tank monitoring
def get_magnesium_level():
  return 1300

monitor()
