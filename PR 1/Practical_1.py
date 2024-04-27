a = 15
print("Type of a: ", type(a))
b = 6.8
print("Type of b: ", type(b))
c = 9 + 5j
print("Type of c: ", type(c))

#Dictonaries
dict = {}
dict['sample'] = "\nsample Dictionary"
dict[2] = "This is Dictionary two"
dict_with_key_values = {'name': 'Omi', 'roll': 232077, 'dept': 'Information Technology'}

print(dict['sample'])
print(dict[2])
print(dict_with_key_values)
print(dict_with_key_values.keys())
print(dict_with_key_values.values())

# Boolean Statements
age = 19
if age > 18:
    print("\nYou can vote")
else:
    print("\nYou cannot vote")

# Sets
set_sample = set()
print("\nInitial blank Set: ")
print(set_sample)

set_sample = set("Ford entered India back")
print("Set with the use of String: ")
print(set_sample)

set_sample = set(["Ford", "entered", "India", "back"])
print("Set with the use of List: ")
print(set_sample)

set_sample = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("Set with the use of Mixed Values")
print(set_sample)

# Strings in Python
string_sample = 'Electoral Registration Officer, 248 - Solapur City North'
print("String with the use of Single Quotes: ")
print(string_sample)

string_sample = "I live in my own Dreams"
print("\nString with the use of Double Quotes: ")
print(string_sample)
print(type(string_sample))

string_sample = '''I'm a student and I live in a world of "programs" '''
print("\nString with the use of Triple Quotes: ")
print(string_sample)
print(type(string_sample))

string_sample = '''hello 
 my     
     name 
    is 
    Omi'''
print("\nCreating a multiline String: ")
print(string_sample)

#List in Python
list_sample = []
print("Initial blank List: ")
print(list_sample)

list_sample = ['My_name_is_Omi']
print("\nList with the use of String: ")
print(list_sample)

list_sample = ["My", "name", "is", "Omi"]
print("\nList containing multiple values: ")
print(list_sample[0])
print(list_sample[2])

list_sample = [['Hello', 'Python'], ['Programmers']]
print("\nMulti-Dimensional List: ")
print(list_sample)

# Tuples in Python
tuple_sample = ()
print("Initial empty Tuple: ")
print(tuple_sample)

tuple_sample = ('Hello', 'Python', 'Programmers')
print("\nTuple with the use of String: ")
print(tuple_sample)

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))

tuple_sample = tuple('Omi')
print("\nTuple with the use of function: ")
print(tuple_sample)

tuple_sample = (0, 1, 2, 3)
tuple_sample_2 = ('Python', 'Programmers')
tuple_sample_3 = (tuple_sample, tuple_sample_2)
print("\nTuple with nested tuples: ")
print(tuple_sample_3)