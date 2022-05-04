# Rolling Two Dice


from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two Dice

die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results

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
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
    

# After creating two instances of Die, we roll the dice and calculate the sum
# of the two dice for each roll ➊ (19). The largest possible result (12) is the sum of
# the largest number on both dice, which we store in max_result ➋(26). 
# The smallest possible result (2) is the sum of the smallest number 
# on both dice. When we analyze the results, we count the number of results for each value between 2
# and max_result ➌ (28). (We could have used range(2, 13), but this would
# work only for two D6 dice. When modeling real-world situations,
# it’s best to write code that can easily model a variety of situations.
# This code allows us to simulate rolling a pair of dice with any number of sides.)


# When creating the chart, we include the dtick key in the x_axis_config
# dictionary ➍(36). This setting controls the spacing between tick marks on the x- axis.
# Now that we have more bars on the histogram, Plotly’s default settings will 
# only label some of the bars. The 'dtick': 1 setting tells Plotly to label every 
# tick mark. We also update the title of the chart and change the output filename as well.

# This graph shows the approximate results you’re likely to get when you roll a pair
# of D6 dice. As you can see, you’re least likely to roll a 2 or a 12 and most likely 
# to roll a 7. This happens because there are six ways to roll a 7, namely:
# 1 and 6, 2 and 5, 3 and 4, 4 and 3, 5 and 2, or 6 and 1