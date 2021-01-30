# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:12:13 2021

@author: Vitamin-C
"""

import matplotlib.pyplot as plt

# Generate cubed values

values = list(range(1, 5001))
cubes = [x**3 for x in values]

# Plot a scatter graph of cubed values

plt.scatter(values, cubes, c = cubes, cmap = plt.cm.PuRd)

# Note the method of changing fontname has been tested and is effective.

plt.xlabel('Value', fontsize = 14, fontname = 'Comic Sans MS')
plt.ylabel('Cubed Value', fontsize = 14, fontname = 'Comic Sans MS')
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.savefig('cubed_values.png', bbox_inches = 'tight')

