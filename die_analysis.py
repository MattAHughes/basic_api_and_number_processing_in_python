# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:29:36 2021

@author: Vitamin-C
"""
import pygal
from die import Die

# Create a d6.

d6 = Die()

# Make some rolls and store the results in a list
results = []
for roll_num in range(1000):
    result = d6.roll()
    results.append(result)

print(results)

# We can do a basic analysis of roll results
frequencies = []
for value in range(1, d6.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualise these results using pygal
hist = pygal.Bar()

hist.title = "Results of rolling a d6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

# pygal has some nice looking plots


# This can be extended to rolling 2 dice

# Create two d6's
d6_1 = Die()
d6_2 = Die()

# Make some rolls and store the results in a list
results = []
for roll_num in range(1000):
    result = d6_1.roll() + d6_2.roll()
    results.append(result)

print(results)

# We can do a basic analysis of roll results
frequencies = []
max_result = d6_1.num_sides + d6_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise these results using pygal
hist = pygal.Bar()

hist.title = "Results of rolling two d6 dice 1000 times."
hist.x_labels = list(range(1,13,1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('two_dice_visual.svg')

# This can be extended to rolling 2 dice of different sizes

# Create two dice
d6_1 = Die()
d10_1 = Die(10)

# Make some rolls and store the results in a list
results = []
for roll_num in range(50000):
    result = d6_1.roll() + d10_1.roll()
    results.append(result)

# We can do a basic analysis of roll results
frequencies = []
max_result = d6_1.num_sides + d10_1.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise these results using pygal
hist = pygal.Bar()

hist.title = "Results of rolling a d6 and a d10 50,000 times."
hist.x_labels = list(range(1, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('d6_d10_visual.svg')
