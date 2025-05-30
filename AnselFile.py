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

print(intersection("2*x + 7","3*(x**2)", 1))
