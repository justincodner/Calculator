def parse(input, val1, val2):
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
    slope = parse(eq, x,y)
    for i in range(steps):
        x+=step
        y+=step*slope
        slope = parse(eq, x,y)
    return round(y, 4)
        

print(eulerMethod(0,1, 0,.01, "2*x-y"))
