# Random Walks

# A random walk is a path that has no clear direction but is determined by a series of random decisions,
# each of which is left entirely to chance. 
# You might imagine a random walk as the path a confused ant would take if it took every step in a random direction.

# Creating the RandomWalk() Class

# To create a random walk, we’ll create a RandomWalk class,
# which will make random decisions about which direction the walk should take.
# The class needs three attributes: one variable to store the number of points
# in the walk and two lists to store the x- and y-coordinate values of each point in the walk.

# We’ll only need two methods for the RandomWalk class: the __init__() method and fill_walk(),
# which will calculate the points in the walk. Let’s start with __init__() as shown here:

from random import choice 

class RandomWalk:
        """A class to generate random walks."""
        def __init__(self, num_points=5000):
          """Initialize attributes of a walk."""
          self.num_points = num_points
# All walks start at (0, 0).
          self.x_values = [0]
          self.y_values = [0]
        def fill_walk(self):
           """Calculate all the points in the walk."""
           while len(self.x_values) < self.num_points:
# Keep taking steps until the walk reaches the desired length.
           
# Decide which direction to go and how far to go in that direction. 
            x_direction = choice([1, -1]) # choose a value for x_direction, which returns either 1 for right movement or –1 for left
            x_distance = choice([0, 1, 2, 3, 4]) #tells Python how far to move in that direction (x_distance) by randomly selecting an integer between 0 and 4. 
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
# Reject moves that go nowhere. ➎ 
            if x_step == 0 and y_step == 0:
             continue
# Calculate the new position. ➏ 
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
