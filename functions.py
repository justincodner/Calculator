epsilon = 1e-15
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

pi = 6*arctan(1/3**.5)

def arcsin(x):
    return arctan(x/(1-x**2)**0.5)

def arccos(x):
    return arctan(((1-x**2)**0.5)/x)

def ln(x):
  if abs(1-x) > 1e-5:
    return 1e5*ln(x**1e-5)
  res = 0
  term = x-1
  for n in range(1, 100):
    res += term/n
    term *= 1-x
    if abs(term/(n+1)) < epsilon:
      break
  return res

def sin(x):
  x %= 2*pi
  res = 0
  term = x
  for n in range(1, 100):
    res += term
    term *= (-1)*(x**2)
    term /= (2*n)*(2*n+1)
    if abs(term) < epsilon:
      break
  return res

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

def tan(x):
    return sin(x)/cos(x)

def parse(input, val):
    input = input.replace('x', f'({val})')
    try:
        result = eval(input)
        return result
    except:
        print("oops")

def leftReimannSum(f, step, start, end):
    i = start
    total = 0
    while(i < end):
        total += parse(f, i) * step
        i += step
    return total

def rightReimannSum(f, step, start, end):
    i = start + step
    total = 0
    while(i <= end):
        total += parse(f, i) * step
        i += step
    return total

def trapazoidReimannSum(f, step, start, end):
    i = start
    total = 0
    while(i <= end):
        total += ((parse(f, i) + parse(f, i + 1)) / 2) * step
        i += step
    return total

def midpointReimannSum(f, step, start, end):
    i = start
    total = 0
    while(i < end):
        mid = i + step / 2
        total += parse(f, mid) * step
        i += step
    return total

def NumericIntegral(f, start, end):
    return midpointReimannSum(f, ((end - start) / 100.0), start, end)

def derivative(f, x):
    h = 1e-7
    return round((parse(f, (x+h)) - parse(f, x)) / h, 4)

def newtons_method(f, x):
    error_small = False
    while error_small == False:
        a = x
        b = x - (parse(f, x) / derivative(f, x))
        if abs(a - b) < 1e-4:
            error_small = True
            break
        return newtons_method(f, b)
    return b

def intersection(f1, f2, guess):
    f = f1 + "-" + f2
    return newtons_method(f, guess)

def parse2(input, val1, val2):
    input = input.replace('x', f'({val1})')
    input = input.replace('y',f'({val2})')
    try:
        result = eval(input)
        return result
    except:
        print("oops")


def eulerMethod(x1, x2, y1, step, eq):
    x = x1
    y = y1
    steps = int((x2-x1) / step)
    slope = parse2(eq, x,y)
    for i in range(steps):
        x+=step
        y+=step*slope
        slope = parse2(eq, x,y)
    return round(y, 4)
