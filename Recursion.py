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
