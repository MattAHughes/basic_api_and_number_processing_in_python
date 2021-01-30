# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 03:57:44 2021

@author: Vitamin-C
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import matplotlib.pyplot as plt

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) # 200 indicates a success

# Store the API response as a variable
response_dict = r.json()

# Process the results
print(response_dict.keys())

# Now start working with the repository
# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) # 200 indicates a success

# Store the API response as a variable
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# Explore some repository information
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# # Examine the first repository
# repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
    
# # Let us dive deeper into the first repository
# repo_dict = repo_dicts[0]

# print("\nSelected information about the first repository: ")
# print("Name: ", repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# We want to gain a snapshot of multiple repositories
# print("\nSelected information about each repository: ")
# for repo_dict in repo_dicts:
#     print("\nName: ", repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])

# Let us visualise some data
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
# Make a visualisation with pygal
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_pygal.svg')

# Make a visualisation with pyplot, which in this case displays relatively poorly compared to pygal
bar = plt.figure(figsize = (20, 12))
plt.xticks(rotation = -20)
plt.bar(names, stars)
plt.title('Most-Starred Python Projects on GitHub')
gca = plt.gcf()
gca.savefig('python_repos_pyplot.svg')

# This is a rather deeper pygal version that allows the addition of clickable links
# Pygal has useful features for embedding, whereas matplotlib seems
# Better for many 
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or "",# This saves missing descriptions from being handled poorly
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
    
# Make a visualisation with pygal
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_pygal.svg')


# Let us do the same for MATLAB as we have for Python
# Make an API call with the argument matlab and store the response
url = 'https://api.github.com/search/repositories?q=language:matlab&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) # 200 indicates a success

# Store the API response as a variable
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# Explore some repository information
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# Plot the results with pygal and pyplot
bar2 = plt.figure(figsize = (20, 12))
plt.xticks(rotation = -20)
plt.bar(names, stars)
plt.title('Most-Starred Matlab Projects on GitHub')
gca = plt.gcf()
gca.savefig('matlab_repos_pyplot.svg')

# This is a rather deeper pygal version that allows the addition of clickable links
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or "",# This saves missing descriptions from being handled poorly
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
    
# Make a visualisation with pygal
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Matlab Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('matlab_repos_pygal.svg')
