def factorial(n):
  if n == 0:
    return 1
  a = 1
  for i in range(1,n + 1):
    a = a * i
  return a

e = 0
for i in range(100):
  e += 1/factorial(i)

pi = 0 # temp for arctan to compile
def arctan(x, epsilon=1e-15):
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
  n = 1
  while True:
    res += term/(2*n-1)
    term *= (-1)*(x**2)
    if abs(term/(2*n+1)) < epsilon:
      break
    n+=1
  return res

pi = 6*arctan(1/3**.5, 1e-30)

def arcsin(x, epsilon=1e-15):
    return arctan(x/(1-x**2)**0.5, epsilon)

def arccos(x, epsilon=1e-15):
    res = arctan(((1-x**2)**0.5)/x, epsilon) # Use trig sub with theta=arccos(x)
    if x < 0: # The above is only proved using a geometric proof, which requires positive inputs.
      return res + pi # arccos and above func are identities with diff. ranges
    return res

def ln(x, epsilon=1e-15):
  if abs(1-x) > 1e-5:
    return 1e5*ln(x**1e-5)
  res = 0
  term = x-1
  n = 1
  while True:
    res += term/n
    term *= 1-x
    if abs(term/(n+1)) < epsilon:
      break
    n+=1
  return res

def sin(x, epsilon=1e-15):
  x %= 2*pi # this will accumulate error really quick for any input > 10^12 (our pi is accurate up to 11~12 digits)
  res = 0
  term = x
  n = 1
  while True:
    res += term
    term *= (-1)*(x**2)
    term /= (2*n)*(2*n+1)
    if abs(term) < epsilon:
      break
    n += 1
  return res

def cos(x, epsilon=1e-15):
  x %= 2*pi # this will accumulate error really quick for any input > 10^12 (our pi is accurate up to 11~12 digits)
  res = 0
  term = 1
  n = 1
  while True:
    res += term
    term *= (-1)*(x**2)
    term /= (2*n-1)*(2*n)
    if abs(term) < epsilon:
      break
    n += 1
  return res

def tan(x, epsilon=1e-15):
    return sin(x, epsilon)/cos(x, epsilon)

def leftReimannSum(f, step, start, end):
    i = start
    total = 0
    while(i < end):
        total += f(i) * step
        i += step
    return total

def rightReimannSum(f, step, start, end):
    i = start + step
    total = 0
    while(i <= end):
        total += f(i) * step
        i += step
    return total

def trapazoidReimannSum(f, step, start, end):
    i = start
    total = 0
    while(i <= end):
        total += ((f(i) + f(i + 1)) / 2) * step
        i += step
    return total

def midpointReimannSum(f, step, start, end):
    i = start
    total = 0
    while(i < end):
        mid = i + step / 2
        total += f(mid) * step
        i += step
    return total

def NumericIntegral(f, start, end, nSteps = 1e6):
    return midpointReimannSum(f, ((end - start) / nSteps), start, end)

def derivative(f, x, h=1e-7):
    return round((f(x+h) - f(x)) / h, 4)

def newtons_method(f, x, epsilon = 1e-4):
    error_small = False
    # breaks when guess makes derivative zero
    while error_small == False:
        a = x
        b = x - (f(x) / derivative(f, x))
        if abs(a - b) < epsilon:
            error_small = True
            break
        return newtons_method(f, b)
    return b

def intersection(f1, f2, guess):
    f = f1 + "-" + f2
    return newtons_method(f, guess)

def eulerMethod(x1, x2, y1, step, eq):
    x = x1
    y = y1
    steps = int((x2-x1) / step)
    slope = eq(x,y)
    for i in range(steps):
        x+=step
        y+=step*slope
        slope = eq(x,y)
    return round(y, 4)

def roots_on_interval(f, a, b):
  lower_bound = min(a, b)
  deltax = abs(a - b) / 1000
  roots = []
  for i in range(1001):
    current_term = lower_bound + deltax * i
    next_term = current_term + deltax
    if (f(current_term) > 0 and f(next_term) < 0) or (f(current_term) < 0 and f(next_term)) > 0:
      roots.append(newtons_method(f, current_term))
  return roots

def points(f, xList):
  return [(x, f(x)) for x in xList]

def inverse_on_interval(f, y, a, b):
  def find_roots(x):
    return f(x) - y
  return roots_on_interval(find_roots, a, b)
