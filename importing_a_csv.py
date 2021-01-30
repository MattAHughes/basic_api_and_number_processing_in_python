# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 01:28:44 2021

@author: Vitamin-C
"""

import csv

from matplotlib import pyplot as plt
from datetime import datetime
# Remember to import os and os.chdir to cd with csv in it if haven't

filename = 'sitka_weather_2014.csv'
error_checking_filename = 'death_valley_2014.csv'

# This is the final version that includes error checking robust to missing values

with open(error_checking_filename) as f:
    reader = csv.reader(f)
    # this effectively separates the header
    header_row = next(reader)
    
    dates, highs, lows = [], [], [] # We can define multiple empty strings in the same block
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print(current_date, 'missing data')
        else:        
            dates.append(current_date) 
            lows.append(low)
            highs.append(high)

# Plot the data
fig = plt.figure(dpi = 300, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# Format the plot
plt.title('Daily high and low temperatures of 2014\nDeath Valley, CA', fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
fig.savefig('dvalley_highs_lows_degf_2014')


# Version without error checking

# with open(filename) as f:
#     reader = csv.reader(f)
#     # this effectively separates the header
#     header_row = next(reader)
    
#     dates, highs, lows = [], [], [] # We can define multiple empty strings in the same block
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
        
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
        
#         low = int(row[3])
#         lows.append(low)
        
# # Plot the data
# fig = plt.figure(dpi = 300, figsize = (10, 6))
# plt.plot(dates, highs, c = 'red', alpha = 0.5)
# plt.plot(dates, lows, c='blue', alpha = 0.5)
# plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

# # Format the plot
# plt.title('Daily high and low temperatures of 2014', fontsize = 24)
# plt.xlabel('', fontsize = 16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontsize = 16)
# plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

# plt.show()
# fig.savefig('sitka_highs_lows_degf_2014')


# Archaeic versions for incremental testing sit below.

#filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
   
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)

# Above showed that high temperatures are stored in column index 1

# Get the high temperatures and the dates from the file

# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     # this effectively separates the header
#     header_row = next(reader)
    
#     dates, highs = [], [] # We can define multiple empty strings in the same block
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
        
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
        
# # Plot the data
# fig = plt.figure(dpi = 300, figsize = (10, 6))
# plt.plot(dates, highs, c = 'red')

# # Format the plot
# plt.title('Daily high temperatures of July 2014', fontsize = 24)
# plt.xlabel('', fontsize = 16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontsize = 16)
# plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

# plt.show()

# # Let us extend this to an entire years csv data in the same format

# filename = 'sitka_weather_2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     # this effectively separates the header
#     header_row = next(reader)
    
#     dates, highs = [], [] # We can define multiple empty strings in the same block
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
        
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
        
# # Plot the data
# fig = plt.figure(dpi = 300, figsize = (10, 6))
# plt.plot(dates, highs, c = 'red')

# # Format the plot
# plt.title('Daily high temperatures of 2014', fontsize = 24)
# plt.xlabel('', fontsize = 16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontsize = 16)
# plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

# plt.show()

# # This analysis can be extended through the addition of low temperatures

# filename = 'sitka_weather_2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     # this effectively separates the header
#     header_row = next(reader)
    
#     dates, highs, lows = [], [], [] # We can define multiple empty strings in the same block
#     for row in reader:
#         high = int(row[1])
#         highs.append(high)
        
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
        
#         low = int(row[3])
#         lows.append(low)
        
# # Plot the data
# fig = plt.figure(dpi = 300, figsize = (10, 6))
# plt.plot(dates, highs, c = 'red')
# plt.plot(dates, lows, c='blue')

# # Format the plot
# plt.title('Daily high and low temperatures of 2014', fontsize = 24)
# plt.xlabel('', fontsize = 16)
# fig.autofmt_xdate()
# plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontsize = 16)
# plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

# plt.show()

# We can add blocks of shading to areas of interest relatively simply


