# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:50:16 2021

@author: Vitamin-C

This project begins an introduction to python data visualisation and generation.
"""

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth = 5, color = 'black')


# Set chart title and label axes
plt.title("Square Numbers", fontsize = 24, fontname = 'arial')
plt.xlabel("Value", fontsize = 14, fontname = 'arial')
plt.ylabel('Square of Value', fontsize = 14, fontname = 'arial')

# Set size of tick labels
plt.tick_params(axis = 'both', labelsize = 14)

# So define parameters of current plot similar to MATLAB gca definitions

plt.show()

# Some correction for the assumption of x-values starting from 0
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5, color = 'black')


# Set chart title and label axes
plt.title("Square Numbers", fontsize = 24, fontname = 'arial')
plt.xlabel("Value", fontsize = 14, fontname = 'arial')
plt.ylabel('Square of Value', fontsize = 14, fontname = 'arial')

# Set size of tick labels
plt.tick_params(axis = 'both', labelsize = 14)

# So define parameters of current plot similar to MATLAB gca definitions

plt.show()

# Let us look at scatter plot
import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)

# Set chart title and axis labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

# Further Scatter Plotting

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s = 100)

# Set chart title and axis labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

# Scatter of 1000 points

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s = 40)

# Set chart title and axis labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range of each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()

# We can assign a variable colour
plt.scatter(x_values, y_values, edgecolor = 'none', s = 40)

plt.scatter(x_values, y_values, c = 'red', edgecolor = 'none', s = 40)

plt.scatter(x_values, y_values, color = (0, 0, 0.8), edgecolor = 'none', s = 40)

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)
# Set chart title and axis labels
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range of each axis.
plt.axis([0, 1100, 0, 1100000])
gca = plt.gcf() # so gcf remains the same

plt.show() 
# Two methods to auto-save, we can name gcf as above
# Or we can replace plt.show(), which creates a new empty axis after
# with plt.savefig() arg

# saving similar to saveas
gca.savefig('squares_plot.png', bbox_inches = 'tight') # We save our named plot, prevents saving a potentially empty plot

