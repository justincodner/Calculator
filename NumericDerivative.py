def derivative(f, x):
    h = 1e-7
    return round((f(x+h) - f(x)) / h, 4)
            

def function(x):
    return 2**(x+3)

print(derivative(function, 5))