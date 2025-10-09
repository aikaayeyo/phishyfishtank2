def monitor():

    maglvl_low = 1250
    maglvl_high = 1350


    current = get_magnesium_level()
    mesg = "Magnesium level OK"

    if (current < maglvl_low):
      mesg = "Magnesium level too low!"
    elif (current > maglvl_high):
      mesg = "Magnesium level too high!"
    else:
      mesg = "Magnesium level is normal."

      return mesg
      
# Function to simulate actual fish tank monitoring
def get_magnesium_level():
  return 1300

monitor()
