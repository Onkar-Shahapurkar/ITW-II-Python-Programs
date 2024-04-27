my_sample_set3 = {1, 2, 3, 4, 5, 6, 7, 8}
my_sample_set4 = {4}

# Checking relation between my_sample_set3 and my_sample_set4
if my_sample_set3 > my_sample_set4:
    print("my_sample_set3 is superset of my_sample_set4")
elif my_sample_set3 < my_sample_set4:
    print("my_sample_set3 is subset of my_sample_set4")
else:
    print("my_sample_set3 is same as my_sample_set4")


# displaying relation between my_sample_set4 and my_sample_set3
if my_sample_set4 < my_sample_set3:
    print("my_sample_set4 is subset of my_sample_set3")
    print("\n")