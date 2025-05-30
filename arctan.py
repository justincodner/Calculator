from constants import pi
epsilon = 1e-15
def arctan(x):
  if x == 1:
    return pi/4
  if x == -1:
    return -pi/4
  if x > 1:
    return -arctan(1/x)+pi/2
  if x < -1:
    return -arctan(1/x)-pi/2
  res = 0
  term = x
  for n in range(1, 100):
    res += term/(2*n-1)
    term *= (-1)*(x**2)
    if abs(term/(2*n+1)) < epsilon:
      break
  return res
