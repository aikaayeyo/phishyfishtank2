def monitor():
  """Return a short status message for phosphate level.

  This mirrors other modules in `updates/` which return strings so the
  central `fishtank.monitor()` can concatenate results without side-effects.
  """

  ph_level_high = 8.4
  ph_level_low = 8.1

  current = get_posphate()

  if current > ph_level_high:
      return "Phosphate level is too high!"
  elif current < ph_level_low:
      return "Phosphate level is too low!"
  else:
      return "Phosphate level is normal."


# Function to simulate actual fish tank monitoring
def get_posphate():
  return 8.2


if __name__ == "__main__":
  # When run directly, print the phosphate status so this module is usable standalone.
  print(monitor())