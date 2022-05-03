# Adding Plot Points

# Let’s increase the number of points to give us more data to work with. 
# To do so, we increase the value of num_points when we make
# a RandomWalk instance and adjust the size of each dot when drawing the plot

import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
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
  
  # This example creates a random walk with 50,000 points
  # (to mirror real- world data) and plots each point at size s=1.
  
  # Experiment with this code to see how much you can increase the number
  # of points in a walk before your system starts to slow down significantly or the plot loses its visual appeal.