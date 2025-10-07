def monitor():
  try:
    # desired acceptable alkalinity range: 4 to 8 (inclusive)
    current = get_alkalinity()
    mesg = "alkalinity ok"

    if current < 4:
      mesg = "alkalinity too low"
    elif current > 8:
      mesg = "alkalinity too high"
    
  except:
    print("Unexpected error") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  return 9