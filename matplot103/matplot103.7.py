# Altering the Size to Fill the Screen
# A visualization is much more effective at communicating patterns
# in data if it fits nicely on the screen. To make the plotting 
# window better fit your screen, adjust the size of Matplotlib’s output, like this:

import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
     # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

  
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
      break
  
  # When creating the plot, you can pass a figsize argument to 
  # set the size of the figure. The figsize parameter takes a tuple, 
  # which tells Matplotlib the dimensions of the plotting window in inches.
  
  # Matplotlib assumes that your screen resolution is 100 pixels per inch;
  # if this code doesn’t give you an accurate plot size, adjust the numbers as necessary.
  # Or, if you know your system’s resolution, pass plt.subplots() the resolution using
  # the dpi parameter to set a plot size that makes effective use of 
  # the space available on your screen, as shown here:

# fig, ax = plt.subplots(figsize=(10, 6), dpi=128)