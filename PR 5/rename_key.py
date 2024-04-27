# Equal operator with del keyword
sample_dictionary = {
    70: "Janhavi",
    71: "Akshita",
    72: "Dhiraj",
    73: "Ambika",
    74: "Ajay",
    75: "Mayuri",
    76: "Ayush",
    77: "Onkar"
}
sample_dictionary[78] = sample_dictionary[76]
del sample_dictionary[76]
print(sample_dictionary)

#rename using poop method
sample_dictionary = {
    70: "Janhavi",
    71: "Akshita",
    72: "Dhiraj",
    73: "Ambika",
    74: "Ajay",
    75: "Mayuri",
    76: "Ayush",
    77: "Onkar"
}
sample_dictionary[78] = sample_dictionary.pop(76)
print(sample_dictionary)