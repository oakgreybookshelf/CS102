#Brittny and Elsie

def times_time():
    num = ""
    product = ""
    answer = ""
    
    try:
        
        num = int(input("Enter an integer: "))
        product = num * 10
        
        return "The product is" + " " + str(product)
    
    except ValueError:
        return "Invalid input, please enter an integer"


def validate():

    try:
        for i in range(3):
            x = int(input('Enter a number: '))
            y = int(input('Enter a second number: '))
            print(x, '/', y, '=', x/y)
    except ValueError:
        print("Invaid input, please enter an integer")
               
    except ValueError:
        print("Invaid input, please enter an integer")
      
    except ZeroDivisionError:
        print("Invalid input, enter a non zero value")
                  
       
    
def payments():
    file_name = input("Enter file name: ")

    try:
        payment_file = open(file_name, 'r')
    except FileNotFoundError:
        print("Error: The file", file_name, "does not exist")
        return

    try:
        payment_record = payment_file.readline()
        name = ""
        total = 0

        user_num = input("Enter user number: ")

        while payment_record != "":
            try:
                payment_list = payment_record.strip().split('|')

                if user_num == payment_list[1]:
                    try:
                        amount = float(payment_list[3])
                        total = total + amount
                        name = payment_list[2]
                    except ValueError:
                        print("Error: Invalid payment amount", payment_list[3], "for customer", user_num)
                        payment_file.close()
                        return

            except IndexError:
                print("Error: Record is missing fields (maybe '|'?):\n", payment_record.strip())
                payment_file.close()
                return

            payment_record = payment_file.readline()

        payment_file.close()

        if total == 0:
            print("Customer didn't make any payments")
        else:
            print("Customer #   Name        Total Payment")
            print(user_num, '\t', '     ', name, '\t', '$', total, sep="")

    except Exception as excpt:
        print("An unexpected error occurred:", excpt)

    
def main():
    num1 = times_time()
    print(num1)
    
    print()
    
    validate()
    
    print()
    payments()


main()