from constants import *
epsilon = 1e-15
def cos(x):
  x %= 2*pi
  res = 0
  term = 1
  for n in range(1, 100):
    res += term
    term *= (-1)*(x**2)
    term /= (2*n-1)*(2*n)
    if abs(term) < epsilon:
      break
  return res
