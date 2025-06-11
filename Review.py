string = "I like to eat pizza"
print("before:", string)
string1 = ''

for char in string:
    if char == "i":
        char = "!"
    string1 = string1 + char

#string1 = string1[:]
#string1 = string1[-1:2:2]
#string1 = string1[2:12]
string1 = string1[3:-3]
print('after:', string1)

mydict = {1: 'red', 2: 'blue', 3: 'yellow'}
print(mydict)

string = input()
number = ['1','2','3','4','5','6','7','8','9','0']
def callname():
    try:
        for char in string:
            if char in number:
                raise ValueError
    except ValueError:
        print('Error: All characters must be letters')

callname()

input1 = input("Enter 'S' to start: ")
while input1 == 'S':
    print("Program is continue")
    input1 = input("Enter 'S' to start: ")
print("Program is finished")
