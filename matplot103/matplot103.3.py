# Styling the Walk

# Coloring the Points
# We’ll use a colormap to show the order of the points in the walk, 
# and then remove the black outline from each dot
# so the color of the dots will be clearer.
# To color the points according to their position in the walk,
# we pass the c argument a list containing the position of each point.
# Because the points are plotted in order,
# the list just contains the numbers from 0 to 4999, as shown here:

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
  
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
      break
  
  # we use range() on line 22 to generate a list of numbers equal to
  # the number of points in the walk. Then we store them in the
  # list point_numbers, which we’ll use to set the color of each point 
  # in the walk. We pass point_numbers to the c argument,
  # use the Blues colormap, and then pass edgecolors='none' 
  # to get rid of the black outline around each point. 