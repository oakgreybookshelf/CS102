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
  if b == 0:
      return 1
  else:
    return a * raise_to_power(a, b-1)
a = int(input("enter 1st number"))
b = int(input("enter last number"))
print( a, "to the power of", b, "is", raise_to_power(a, b))

# division
def divide(divisor, dividend, count=0):
    if divisor == 0 :
        return count
    else:
        count += 1
        return divide(divisor - dividend, dividend, count)

a = int(input("enter 1st number (divisor) "))
b = int(input("enter last number (dividend) "))
print("the quotient of", a, "and", b, "is", divide(a, b, count=0))

# division with try/except block
def divide(divisor, dividend, count=0):
    try:
        if divisor == 0 :
            return count
        else:
            count += 1
            return divide(divisor - dividend, dividend, count)
    except RuntimeError:
        print("Error: These numbers are not divisible, try again")

a = int(input("enter 1st number (divisor) "))
b = int(input("enter last number (dividend) "))
print("the quotient of", a, "and", b, "is", divide(a, b, count=0))



def triangle_of_stars(n):
    if n > 0:
        triangle_of_stars(n-1)
        print("*" * n)
        
        
def list_length(my_list):
    count = 1
    if my_list == []:
        return 0
    else:
       
        return count + list_length(my_list[1:])
    
    
def number_of_digits(integer):
    count = 1
    if integer == 0:
        return 0
    else:
        return count + number_of_digits(integer // 10)
    
def capitalize(string):

    if string == "":
        return ""
    else:
        return string[0].upper() + capitalize(string[1:])
    

def count_characters(string, char):
    count = 0
    if string == "":
        return 0
    if string[0] == char:
        count = count + 1
    return count + count_characters(string[1:], char)


    
def main():
    n = int(input("Enter an intger: "))
    triangle_of_stars(n)
    
    print()
    
    my_list = input("Enter elements seperated by a comma: ").split(",")
    list_len = list_length(my_list)
    print("Your list has", list_len, "elements")
    
    print()
    
    integer = int(input("Enter an integer: "))
    num_digits = number_of_digits(integer)
    print("The integer", integer, "has", num_digits, "number(s) of digits")
    
    print()
    
    string = input("Enter a string: ")
    string_cap = capitalize(string)
    print(string_cap)
    
    print()
    
    string = input("Enter a string: ")
    char = input("Enter a single character: ")
    count = count_characters(string, char)
    print("The character ", "'", char, "'", " appears in the string ", "'", string, "' ", count, " time(s)", sep="")
    
main()
    
