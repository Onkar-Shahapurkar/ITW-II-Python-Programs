print("Hello, Myself Onkar Shahapurkar and I belong to India")

#Strings in Python
string_sample = 'Welcome, Programmers to the World of Python'
print("\nString with the use of Single Quotes: ")
print(string_sample)

string_sample = "Myself Omi"
print("String with the use of Double Quotes: ")
print(string_sample)

string_sample = '''I'm a student and I live in a world of "joy"'''
print("String with the use of Triple Quotes: ")
print(string_sample)

string_sample = '''This 
is 
     Pune
  City'''
print("Creating a multiline String: ")
print(string_sample)

#Accessing Characters in Python String
string_sample = "Onkar Shahapurkar"
print("\nInitial String: ")
print(string_sample)

print("First character of String is: ")
print(string_sample[0])

print("Printing random character of String: ")
print(string_sample[4:-3])

print("Last character of String is: ")
print(string_sample[-1])

#Reversing a Python
print("\nReversing This String: ")
text1 = "evitcefeD si enohPtramS sihT"
print(text1[::-1])
text = "This SmartPhone is Defective"
print(text[::-1])

#String Slicing
print("\n")
name = "OnkarIsGoodBoy"
print(name[2])
print(name[-2])  # known as negative slicing, -1 corresponds to (length-1) index that is last index

print(name[1:4])
print(name[:3])  # By Default start from index 0
print(name[2:])  # By Default end at last index
print(name[:])   # by Default start from index 0 and end at the last element

#String Methods
story = "onkar has completed his Diploma Degree in Information Technology,By miracle and his constant Hard work" \
        " he ranked 2nd"
print("The length of the is :", len(story))
print(story.upper())
print(story.lower)
print(story.title())
print("Does story ends with % ? :", story.endswith("%"))
print("There are ", story.count(" "), "whitespaces in the String")
print(story.capitalize())  # Capitalize the first letter of the string
# returns the index of the first occurrence of the specified word
print("Index of first occurred 'Technology' :", story.find("Technology"))
print(story.replace("94", "94.56"))
