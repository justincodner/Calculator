pi = 0 # temp for arctan to compile
from arctan import arctan
pi = 6*arctan(1/3**.5)
def sqrt(n):
  a = n ** .5
  return a

def factorial(n):
  if n == 0:
    return 1
  a = 1
  for i in range (1,n + 1):
    a = a * i
  return a

e = 0
for i in range(15):
  e += 1/factorial(i)
print(e) 

def ln(x):
  a = 0
  if x > 1.1:
    return 2 * ln(x ** (1/2))
  for i in range(1, 15):
    a += (-(1 - x) ** i) / (i)
  return a


    
    
