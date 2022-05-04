# Rolling Dice of different sizes

# Let’s create a six-sided die and a ten-sided die, and see what happens when we roll them 50,000 times:

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

   # Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

 # Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')


# To make a D10, we pass the argument 10 when creating the second Die instance ➊ and
# change the first loop to simulate 50,000 rolls instead of 1000.
# We change the title of the graph and update the output filename as well ➋.
# Figure 15-14 shows the resulting chart. Instead of one most likely result, there are five. 
# This happens because there’s still only one way to roll the smallest value (1 and 1)
# \and the largest value (6 and 10), but the smaller die limits the number of ways you 
# can generate the middle numbers: there are six ways to roll a 7, 8, 9, 10, and 11. 
# Therefore, these are the most common results, and you’re equally likely to roll any one of these numbers.

# Our ability to use Plotly to model the rolling of dice gives us considerable freedom
# in exploring this phenomenon. In just minutes you can simulate
# a tremendous number of rolls using a large variety of dice.