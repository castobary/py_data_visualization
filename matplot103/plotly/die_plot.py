# Creating a histogram

from plotly.graph_objs import Bar, Layout

from plotly import offline

from die import Die

# Create a D6

die = Die()

# Make some rolls and store the result in a list

results = []

for roll_num in range(1000): # Rolling the die 1000 times
    result = die.roll()
    results.append(result)
    
# Analyze results

frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the results.

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 
              'layout': my_layout}, 
             filename='d6.html')

# To make a histogram, we need a bar for each of the possible results. We
# store these in a list called x_values, which starts at 1 and ends at the number of
# sides on the die ➊(32). Plotly doesn’t accept the results of the range() function directly,
# so we need to convert the range to a list explicitly using the list() function. 
# The Plotly class Bar() represents a data set that will be formatted as
# a bar chart ➋ (33). This class needs a list of x-values, and a list of y-values. 

# The class must be wrapped in square brackets, because a data set can have multiple elements.
# Each axis can be configured in a number of ways, and each configuration option
# is stored as an entry in a dictionary. At this point, we’re just setting
# the title of each axis ➌ (35). The Layout() class returns an object that
# specifies the layout and configuration of the graph as a whole ➍ (38). Here we set the title of
# the graph and pass the x- and y-axis configuration dictionaries as well.
# To generate the plot, we call the offline.plot() function ➎ (41). 

# This function needs a dictionary containing the data and layout objects,
# and it also accepts a name for the file where the graph will be saved. 
# We store the output in a file called d6.html.