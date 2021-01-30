# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:40:24 2021

@author: Vitamin-C
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk and plot it.
rw = RandomWalk()
rw.fill_walk()

# Some clarity is introduced through showing the order of the random walk
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s = 15, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none')
plt.xlabel('x-values', fontsize = 14, fontname = 'Arial')
plt.ylabel('y-values', fontsize = 14, fontname = 'Arial')
gca = plt.gcf()
plt.show()
gca.savefig('random_walk.png')


# This could be easily made into a random walk generator in a while loop.
# This version can be run to additionally show the start and end points

rw = RandomWalk()
rw.fill_walk()

# Some clarity is introduced through showing the order of the random walk
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s = 15, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none')
plt.xlabel('x-values', fontsize = 14, fontname = 'Arial')
plt.ylabel('y-values', fontsize = 14, fontname = 'Arial')

# These are added after other features are defined so as to be on top.
plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

gca = plt.gcf()
plt.show()


# Rather than working with such arbitrary axes, we can turn them off

rw = RandomWalk()
rw.fill_walk()

# Some clarity is introduced through showing the order of the random walk
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s = 15, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none')

# Here we turn off axes visibility
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# These are added after other features are defined so as to be on top.
plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

gca = plt.gcf()
plt.show()
gca.savefig('random_walk_no_axes.png')


# Here is a version with more than 5000 steps

rw = RandomWalk(50000)
rw.fill_walk()

# Some clarity is introduced through showing the order of the random walk
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s = 2, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none')

# Here we turn off axes visibility
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# These are added after other features are defined so as to be on top.
plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

gca = plt.gcf()
plt.show()
gca.savefig('random_walk_50000_steps.png')


# Here is a version that fiddles with figure size
# This can make the saved figures size rather more useful

rw = RandomWalk()
rw.fill_walk()

# Set the figure plotting size
plt.figure(figsize = (10, 6))

# Some clarity is introduced through showing the order of the random walk
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, s = 2, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none')

# Here we turn off axes visibility
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# These are added after other features are defined so as to be on top.
plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

gca = plt.gcf()
plt.show()
gca.savefig('random_walk_varied_figsize.png')