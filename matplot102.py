# Plotting and Styling Individual Points with scatter()

# Sometimes, it’s useful to plot and style individual points based on certain characteristics.

# To plot a single point, use the scatter() method. 
# Pass the single (x, y) values of the point of interest to scatter() to plot those values:

import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)
plt.show()

# Make the plot more interesting

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200) #s sets size of the dot

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

 # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# Plotting a series of points with scatter

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

 # Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()