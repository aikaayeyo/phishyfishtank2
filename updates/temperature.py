def monitor():

  temps_high = 80
  temps_low = 74
  
  current = get_temps()
  
  if (current > temps_high):
      print("Temperature is too high!")
  elif (current < temps_low):
      print("Temperature is too low!")
  else:
      print("Temperature is at a normal rate.")
  
def get_temps():
  return 76

monitor()