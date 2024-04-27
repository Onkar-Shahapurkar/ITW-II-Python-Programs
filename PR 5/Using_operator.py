def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


half_dsy_1 = {70 : "Janhavi", 71 : "Akshita", 72: "Dhiraj", 73: "Ambika"}
half_dsy_2 = {74: "Ajay", 75: "Mayuri", 76: "Ayush", 77: "Onkar"}
dsy = Merge(half_dsy_1, half_dsy_2)
print(dsy)
