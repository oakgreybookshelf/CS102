# https://learn.zybooks.com/zybook/WNECS102IT102WalzSpring2025/chapter/9/section/6
# dictionaries are case-sensitive
mydict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

allergies = {
  'Peanuts': ['Tobi', 'Sachi', 'Aimee'],
  'Seafood': ['Tobi', 'Sola', 'Estella', 'Grace'],
  'Alternatives': {
    'Jerky': ['Tobi', 'Aimee', 'Estella'],
    'Avocado': ['Sachi', 'Grace', 'Sola']
  }
}
Severity = {
    'Extreme': ['Tobi', 'Aimee'],
    'Mild': ['Sachi', 'Estelle'],
    'Minor': ['Sola', 'Grace']
  }
# add a new allergy and student
allergies['Dairy'] = 'Martha'
# check for presence
is_present = 'dairy' in allergies
print(is_present) # outputs false
print('Dairy' in allergies) # outputs true
# get value for key
print('Students with a peanut allergy:', allergies['Peanuts'])
print('Students with a peanut allergy:', allergies.get('Peanuts'))
# gets value and returns a statement if value not in dict
print('Students with a peanut allergy:', allergies.get('Soy', 'No students have this allergy'))

# GET KEY FOR VALUE ### (one value per key)
print([k for k, v in mydict.items() if v == 10])
# GET KEY FOR VALUE       .......work in progress.....
for key, value in allergies:
    if value == 'Tobi':
        print('Tobi\'s allergy is', key)
      
# prints as tuple
print(allergies.items())
#print all keys
print(allergies.keys())
# print all values
print(allergies.values())
# merges two dictionaries without saving 2nd dictionary name
allergies.update(Severity)	
print(allergies)
# printing key-value pairs
for key, value in allergies.items():  
    print(f"{key}: {value}")

# List: append
allergies['Alternatives']['Jerky'].append('Sonya')
print(allergies['Alternatives']['Jerky'])
# List: inserts Lili at index 1
allergies['Peanuts'].insert(1, 'Lili')
print(allergies['Peanuts'])
# List: remove element
allergies['Peanuts'].remove('Tobi')
print(allergies['Peanuts'])
# remove last element on the right
allergies['Peanuts'].pop()
print(allergies['Peanuts'])
# remove element at index 1
allergies['Peanuts'].pop(1)
print(allergies['Peanuts'])


abc = ['a', 'b', 'c']
# prints index of elemenet a
print(abc.index('a'))
# prints element at index 0
print(abc[0])

# del my_dict['x'] deletes the x key from dictionary and its values
# key in my_dict tests for existence of key in dictionary
# my_dict.clear() removes all elements in dictionary
# list.index() returns an index of the list
# list.count('x') counts how many times x appears in the list
# list.sort() sorts the list
# list.reverse() reverse the order of the list

