def monitor():
  """Return a short status message for phosphate level.

  This mirrors other modules in `updates/` which return strings so the
  central `fishtank.monitor()` can concatenate results without side-effects.
  """


  current = get_posphate()

  return mesg

# Functiion to simulate actual fish tank monitoring
def get_posphate():
  return .05