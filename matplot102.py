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

# Calculating Data Automatically

# Writing lists by hand can be inefficient, especially when we have many points. 
# Rather than passing our points in a list, let’s use a loop in Python to do the calculations for us.

x_values = range(1, 1001) # generating a range of values from 1 to 1000
y_values = [x**2 for x in x_values] # for loop for squaring

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])
plt.show()

#Defining Custom Colors

x_values = range(1, 1001) # generating a range of values from 1 to 1000
y_values = [x**2 for x in x_values] # for loop for squaring

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10) # specifying colorr
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])
plt.show()

# You can also define custom colors using the RGB color model. 
# To define a color, pass the c argument a tuple with three decimal 
# values (one each for red, green, and blue in that order), using values between 0 and 1.
# For example, the following line creates a plot with light-green dots:


# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.


# Using a Colormap

# A colormap is a series of colors in a gradient that moves from a starting to an ending color. 
# You use colormaps in visualizations to emphasize a pattern in the data.
# For example, you might make low values a light color and high values a darker color.

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
plt.show()

# Saving a plot automatically

# If you want your program to automatically save the plot to a file, 
# you can replace the call to plt.show() with a call to plt.savefig():

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight') 