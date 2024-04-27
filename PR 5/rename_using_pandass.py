import pandas as pd

student = {
 "name": "Omi",
 "age": 20,
 "address": "Solapur, India"
}
print(student)

df = pd.DataFrame(student, index=[0, 1, 2])
df.rename(columns={"address": "Address"}, inplace=True)
print(df.to_dict())