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

def interection(f1, f2, guess1, guess2):
    derivative():

print(NumericIntegral("x**2", 0, 101))
print(leftReimannSum('x**2 - 7 * x + 65', 0.001, 0, 1))
print(rightReimannSum('x**2 - 7 * x + 65', 0.001, 0, 1))
print(midpointReimannSum('x**2 - 7 * x + 65', 0.001, 0, 1))
print(trapazoidReimannSum('x**2 - 7 * x + 65', 0.001, 0, 1))
