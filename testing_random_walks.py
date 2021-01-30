# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:06:24 2021

@author: Vitamin-C
"""
# Modified random walk as a plot instead of a scatter plot

import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

# Set the figure plotting size
plt.figure(figsize = (10, 6))

# Some clarity is introduced through showing the order of the random walk
point_numbers = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth = 2, c = 'black')

# Here we turn off axes visibility
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# These are added after other features are defined so as to be on top.
plt.plot(rw.x_values[0:1], rw.y_values[0:1], c = 'green', linewidth = 50)
plt.plot(rw.x_values[-2:-1], rw.y_values[-2:-1], c = 'red', linewidth = 50)

gca = plt.gcf()
plt.show()
gca.savefig('random_walk_line_plot.png')

