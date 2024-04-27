import matplotlib.pyplot as plt

year = [1972, 1982, 1992, 2002, 2012]
e_india = [100.6, 158.61, 305.54, 394.96, 724.79]
e_bangladesh = [10.5, 25.21, 58.65, 119.27, 274.87]

plt.plot(year, e_india, color='purple',
         label='Bhutan')
plt.plot(year, e_bangladesh, color='yellow',
         label='Afghanistan')

# naming of x-axis and y-axis
plt.xlabel('Years')
plt.ylabel('Power consumption in kWh')

# naming the title of the plot
plt.title('Energy consumption per capital of Bhutan and Afghanistan')
plt.legend()
plt.show()