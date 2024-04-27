my_sample_set3 = {1, 2, 3, 4, 5, 6, 7, 8}
my_sample_set4 = {4}

# difference between my_sample_set3 and my_sample_set4
my_sample_set5 = my_sample_set3 - my_sample_set4
print("Elements in my_sample_set3 and not in my_sample_set4: my_sample_set5 = ", my_sample_set5)

# check if my_sample_set4 and my_sample_set5 are disjoint sets
if my_sample_set4.isdisjoint(my_sample_set5):
    print("\nmy_sample_set4 and my_sample_set5 have nothing in common\n")

# Removing all the values of my_sample_set5
my_sample_set5.clear()
print("After applying clear on sets my_sample_set5: ")
print("my_sample_set5 = ", my_sample_set5)