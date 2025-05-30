def derivative(f, x):
    h = 1e-7
    return round((f(x+h) - f(x)) / h, 4)
