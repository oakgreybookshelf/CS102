#Brittny and Elsie


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