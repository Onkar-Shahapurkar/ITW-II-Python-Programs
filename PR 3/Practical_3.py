name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
print(name_list)

# List in Python
list_sample = []
print("Blank List: ")
print(list_sample)

list_sample = [60, 89, 45]
print("List of numbers: ")
print(list_sample)

list_sample = ["Omi", "Ambika", "Dhiraj", "Akshita"]
print("List Items: ")
print(list_sample[2])
print(list_sample[1])

# Accessing Elememts from List
list_sample = ["Omi", "Ambika", "Dhiraj", "Akshita"]
print("Accessing a element from the list:")
print(list_sample[1])
print(list_sample[3])

#Join two list
name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
list2 = [7.67, 8.29, 7.75, 6.75]
joined_list = name_list + list2
print("Joined List: ", joined_list)

# Append a List to the existing list
name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
list2 = [7.67, 8.29, 7.75, 6.75]
for x in list2:
    name_list.append(x)
print("Appended List: ", name_list)

# Use of the extend method
name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
list2 = [7.67, 8.29, 7.75, 6.75]
name_list.extend(list2)
print("Extended List: ", name_list)

# Slicing of a Python List
institute = ['V', 'I', 'S', 'H', 'W', 'A', 'K', 'A', 'R', 'M', 'A']
print("\n", institute[1:6])
print(institute[4:])
print(institute[:])

# Repeat elements of list using append method
name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
print("The original list is: ", name_list)
num = 56
print("The input number to append to list is: ", num)
name_list.append(num)
print("List appended with the number is :", name_list)

# Repeat elements of list using extend method
name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
print("The original list is: ", name_list)
newList = [45, 89, 23]
print("The input list to append elements from is:", newList)
name_list.extend(newList)
print("The output list is:", name_list)

# Using * operator
name_list = ["Omi", "Ambika", "Dhiraj", "Akshita"]
print("The original list is: ", name_list)
count = 3
print("Number of Times to repeat the elements:", count)
op_list = name_list * 3
print("The output list is:", op_list)

# List Comprehension
numbers = [5, 9, 7, 3, 6, 16, 35, 54, 45, 13, 12, 87, 56, 31, 97, 65, 87, 54, 5]
even = [i for i in numbers if i % 2 == 0]
print(even)