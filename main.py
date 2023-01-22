import math
from decimal import Decimal


def input_0():
  equation = input("Please enter equation : ") # x^2 - 3 = 0
  n_low = Decimal(input("Please enter lower : "))
  n_high = Decimal(input("Please enter upper : "))
  dec = int(input("Enter the number of decimals : "))
  print("")
  return(equation, n_low, n_high, dec)


def calculate(equation, n_low, n_high, dec):
  mean_0 = ((n_low + n_high) / 2)
  total_min = Decimal(eval(equation, {}, {"x" : n_low, "e" : math.e, "pi" : math.pi, "sin" : math.sin, "cos" : math.cos}))
  total_mean = Decimal(eval(equation, {}, {"x" : mean_0, "e" : math.e, "pi" : math.pi, "sin" : math.sin, "cos" : math.cos}))
  total_max = Decimal(eval(equation, {}, {"x" : n_high, "e" : math.e, "pi" : math.pi, "sin" : math.sin, "cos" : math.cos}))

  
  if abs(mean_0.as_tuple().exponent) == dec or abs(mean_0.as_tuple().exponent) == 27 or total_mean == 0.00 :
    return(mean_0)

  print("By IVT, there is c ∈ ({} , {}) such that f(c)=0".format(n_low, n_high))
  print("x = {} , f({}) = {}".format(mean_0, mean_0, total_mean))

  if total_min < total_max :# min - , max +
    
    if total_mean < 0 : # mean -
      print("x = {} , f({}) = {}".format(n_high, n_high, total_max),end='\n\n')
      return calculate(equation, mean_0, n_high, dec)
    elif total_mean > 0 : # mean +
      print("x = {} , f({}) = {}".format(n_low, n_low, total_min),end='\n\n')
      return calculate(equation, n_low, mean_0, dec)
    
  if total_min > total_max : # min + , max -
    if total_mean < 0 : # mean -
      print("x = {} , f({}) = {}".format(n_low, n_low, total_min),end='\n\n')
      return calculate(equation, mean_0, n_low, dec)
    elif total_mean > 0 : # mean +
      print("x = {} , f({}) = {}".format(n_high, n_high, total_max),end='\n\n')
      return calculate(equation, n_high, mean_0, dec)
      

def display(equation, n_low, n_high):
  total_min = Decimal(eval(equation, {}, {"x" : n_low, "e" : math.e, "pi" : math.pi, "sin" : math.sin, "cos" : math.cos}))
  total_max = Decimal(eval(equation, {}, {"x" : n_high, "e" : math.e, "pi" : math.pi, "sin" : math.sin, "cos" : math.cos}))
  
  print("Let f(x) = {} we see that f is continuous on [{},{}]".format(equation, n_low, n_high))
  if total_min < 0 and total_max > 0 :
    print("f({}) = {}  {} 0".format(n_low, total_min, "<"))
    print("f({}) = {}  {} 0".format(n_high, total_max, ">"),end='\n\n')
  if total_min > 0 and total_max < 0 :
    print("f({}) = {}  {} 0".format(n_low, total_min, ">"))
    print("f({}) = {}  {} 0".format(n_high, total_max, "<"),end='\n\n')


equation, n_low, n_high, dec = input_0()
#equation, n_low, n_high, dec = "pow(x,2)-3", Decimal(0), Decimal(2), 200
display(equation, n_low, n_high)
ans = calculate(equation, n_low, n_high, dec)
print("*** Ans = {} ***".format(ans))