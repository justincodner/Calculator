epsilon = 1e-15
def sin(x):
  res = 0
  term = x
  for n in range(1, 100):
    res += term
    term *= (-1)*(x**2)
    term /= (2*n)*(2*n+1)
    if abs(term) < epsilon:
      break
  return res
