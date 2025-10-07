def monitor():
    # List of calcium levels from 380 to 450 in intervals of 5
    calc_levels = [380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450]

    current = get_calcium_level()

    if current < 380:
        mesg = "Calcium level too low!"
    elif current > 450:
        mesg = "Calcium level too high!"
    else:
        mesg = "Calcium level perfect!"
    return mesg
  
# Functiion to simulate actual fish tank monitoring
def get_calcium_level():
    return 420

# Print the result when running the script
print(monitor())