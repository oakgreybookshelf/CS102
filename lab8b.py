#Brittny and Elsie

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