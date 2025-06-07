# multiplication
def multiply(a, b):
  c = 0
  for i in range(0, a):
      c += b
      multiply(a-1,b)
  return(c)
a = int(input("enter 1st number"))
b = int(input("enter last number"))
print("the product of", a, "and", b, "is", multiply(a, b))

# exponent
def raise_to_power(a, b):
  c = 1
    for i in range(b):
    c *= b
  raise_to_power(a-1, b)
  return(c)
a = int(input("enter 1st number"))
b = int(input("enter last number"))
print( a, "to the power of", b, "is", raise_to_power(a, b))
