# Generating Multiple Random Walks

# Every random walk is different, and it’s fun to explore
# the various patterns that can be generated. One way to use
# the preceding code to make multiple walks without having
# to run the program several times is to wrap it in a while loop

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
    ax.scatter(rw.x_values, rw.y_values, s=15)
  
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
      break