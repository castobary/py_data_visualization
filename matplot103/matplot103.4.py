#Plotting the Starting and Ending Points
#In addition to coloring points to show their position along the walk, 
# it would be useful to see where each walk begins and ends.
# To do so, we can plot the first and last points individually 
# after the main series has been plotted. 
# We’ll make the end points larger and
# color them differently to make them stand out, as shown here:

import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=15)
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100)
  
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
      break
  
  # To show the starting point, we plot point (0, 0)
  # in green in a larger size (s=100) than the rest of the points.
  # To mark the end point, we plot the last x- and y-value
  # in the walk in red with a size of 100. 
  # Make sure you insert this code just before the call to plt.show()
  # so the starting and ending points are drawn on top of all the other points.
# When you run this code, you should be able to spot exactly where each walk begins and ends. 