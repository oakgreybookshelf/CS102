import random

def print_file(file_name):
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
 
    for element in numbers_record:
        print(element.rstrip('\n'))
    
    numbers.close()
    
  
def print_n(file_name, num):   
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
    
    for i in range(num):
        print(numbers_record[i].rstrip('\n'))
        
    numbers.close()
    
def print_record_numbers(file_name):
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
 
    for i in range(len(numbers_record)):
        
        print(i+1, numbers_record[i].rstrip('\n'))
    
    numbers.close()
    
def count_records(file_name):
    numbers = open(file_name, 'r')
    count = 0
    numbers_record = numbers.readlines()
    for i in range(len(numbers_record)):
        count = count + 1
    return count
    numbers.close()
    
    
def write_random(file_name, integers):
    numbers = open(file_name, 'a+')
    numbers_record = numbers.readlines()
    
    for i in range(integers):
        record = random.randint(1, 500)
        numbers.write(str(record) +"\n")
        
    numbers.close()
        
        
        
def read_sum(file_name):
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
    
    sum1 = 0
    
    for num in numbers_record:
        sum1 += int(num.strip())

    return sum1
    numbers.close()
    
    
        
def main():
    print_file('numbers.txt')
    
    print()
    
   
    file_name = input("Enter file name: ")
    number = int(input("Enter number of records: "))
    print_n(file_name, number)
    
    print()
    file_name = input("Enter file name: ")
    print_record_numbers(file_name)
    
    print()
    file_name = input("Enter file name: ")
    count = count_records(file_name)
    print(count)
    
    print()
    file_name = input("Enter file name: ")
    integers = int(input("Enter an integer: "))
    
    nums = write_random(file_name, integers)
    
    print()
    
    file_name = input("Enter file name: ")
    sum1 = read_sum(file_name)
    print(sum1)
    
    
    
main()
def print_file(file_name):
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
 
    for element in numbers_record:
        print(element.rstrip('\n'))
    
    numbers.close()
    
  
def print_n(file_name, num):   
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
    
    for i in range(num):
        print(numbers_record[i].rstrip('\n'))
        
    numbers.close()
    
def print_record_numbers(file_name):
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
 
    for i in range(len(numbers_record)):
        
        print(i+1, numbers_record[i].rstrip('\n'))
    
    numbers.close()
    
def count_records(file_name):
    numbers = open(file_name, 'r')
    count = 0
    numbers_record = numbers.readlines()
    for i in range(len(numbers_record)):
        count = count + 1
    return count
    numbers.close()
    
    
def write_random(file_name, integers):
    numbers = open(file_name, 'a+')
    numbers_record = numbers.readlines()
    
    for i in range(integers):
        record = random.randint(1, 500)
        numbers.write(str(record) +"\n")
        
    numbers.close()
        
        
        
def read_sum(file_name):
    numbers = open(file_name, 'r')
    numbers_record = numbers.readlines()
    
    sum1 = 0
    
    for num in numbers_record:
        sum1 += int(num.strip())

    return sum1
    numbers.close()
    
    
        
def main():
    print_file('numbers.txt')
    
    print()
    
   
    file_name = input("Enter file name: ")
    number = int(input("Enter number of records: "))
    print_n(file_name, number)
    
    print()
    file_name = input("Enter file name: ")
    print_record_numbers(file_name)
    
    print()
    file_name = input("Enter file name: ")
    count = count_records(file_name)
    print(count)
    
    print()
    file_name = input("Enter file name: ")
    integers = int(input("Enter an integer: "))
    
    nums = write_random(file_name, integers)
    
    print()
    
    file_name = input("Enter file name: ")
    sum1 = read_sum(file_name)
    print(sum1)
    
    
    
main()

def write_ages(file_name):
    names_ages = open(file_name, 'a+')
    name_age_file = names_ages.readline()
    
    more = "Y"
    
    while more == "Y":
        name = input("Enter name: ")
        age = input("Enter age: ")
        names_ages.write(str(name) + ',' + (age)  + '\n')
         
        more = input("Do you want to continue? Y/N: ")
    names_ages.close()
    
    
def read_ages(file_name):
    name = open(file_name, 'r')
    name_record = name.readlines()
    print("Names:    Ages:")
    
    for element in name_record:
        element_list = element.split(',')
        print(element_list[0], '\t', element_list[1].rstrip('\n'))
              
    name.close()
    

def average_num_words(file_name):
    lyrics = open(file_name, 'r')
    lyrics_record = lyrics.readline()
    total = 0
    num_records = 0
    while lyrics_record != "":
        fields = lyrics_record.split()
        total += len(fields)
        num_records += 1
        lyrics_record = lyrics.readline()

    average = total / num_records
    lyrics.close()
    return average
    
    
def payments():
    payment_file = open('payments.txt', 'r')
    payment_record = payment_file.readline()

    name = ""
    total = 0
    
    user_num = input("Enter user number: ")
    while payment_record != "":
        payment_list = payment_record.split('|')
     
       
        if user_num == payment_list[1]:
            total = float(payment_list[3]) + total
            name = payment_list[2]
    
        payment_record = payment_file.readline()
    
    payment_file.close()
    
    if total == 0:
        print("Customer didn't make any payments")
        
    else:
        
        
        print("Customer #   Name          Total Payment")
        print(user_num, '\t', '     ', name, '\t', '   ', '$',total, sep="")
    
def main():
    file_name = input("Enter file name: ")
    write_ages(file_name)
    
    print()
    
    file_name = input("Enter file name: ")
    read_ages(file_name)
    
    print()
    
    file_name = input("Enter file name: ")
    average = average_num_words(file_name)
    print(average)
    
    print()
    
    payments()


main()
