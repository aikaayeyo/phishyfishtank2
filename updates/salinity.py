def monitor():
  try:
    current = get_salinity()
    mesg = "salinity ok"

    # Desired safe salinity range: 30 to 35 (inclusive)
    if current < 30:
      mesg = "salinity too low"
    elif current > 35:
      mesg = "salinity too high"
    
  except:
    print("Unexpected error")

  return mesg

# Function to simulate actual fish tank monitoring
def get_salinity():
  return 31