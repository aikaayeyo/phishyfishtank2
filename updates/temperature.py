def monitor():

  temps_high = 80
  temps_low = 74
  
  current = get_temps()
  
  if (current > temps_high):
      mesg = "Temperature is too high!"
  elif (current < temps_low):
      mesg = "Temperature is too low!"
  else:
      mesg = "Temperature is at a normal rate."

  return mesg
  
def get_temps():
  return 76

monitor()