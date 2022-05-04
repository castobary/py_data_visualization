# Python’s csv module in the standard library parses the lines in a CSV file and
# allows us to quickly extract the values we’re interested in. 
# Let’s start by examining the first line of the file, which contains a series of headers for the data. 

import csv

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
   reader = csv.reader(f)
   header_row = next(reader)
  
   for index, column_header in enumerate(header_row):
      print(index, column_header)
      

# The enumerate() function returns both the index of each item and the value
# of each item as you loop through a list ➊.