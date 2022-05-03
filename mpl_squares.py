import matplotlib.pyplot as plt # importing pyplot module using alias

# pyplot module contains a number of functions to generate charts and plots

squares = [1, 4, 9, 16, 25] # create a list to be plotted
fig, ax = plt.subplots() #subplot() can generate one or more plots on the same figure

# fig represents the entire collection of plots that are generated
# ax represents a single plot and its the one we will use most of the time

ax.plot(squares) # plot() plots the data in a meaningful way
plt.show() # opens the matplotlib viewer to display the plot



# Changing the Label Type and Line Thickness

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3) # linewidth controls thickness of the line

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24) # set_title() method use to give plot a title
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14) # used to set axis tick marks
plt.show()

# Correcting the plot

# When you give plot() a sequence of numbers, 
# it assumes the first data point corresponds to
# an x-coordinate value of 0, but our first point corresponds
# to an x-value of 1. We can override the default
# behavior by giving plot() the input and output values used to calculate the squares:


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn') # changing plot style, a line before starting to plot
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()