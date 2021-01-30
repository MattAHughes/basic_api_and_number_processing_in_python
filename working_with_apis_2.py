# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 04:12:30 2021

@author: Vitamin-C
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter

# Make an API call to the top stories of hacker news
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: ", r.status_code)

# Process the information about each story submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a api call for each article
    article_url = ('https://hacker-news.firebaseio.com/v0/item/' +
                   str(submission_id) + '.json')
    submission_r = requests.get(article_url)
    print('Submission status code: ', submission_r.status_code)
    response_dict = submission_r.json()
    
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0) # This is hedging on the case of no descendents existing in some cases, so uses a get format
        }
    submission_dicts.append(submission_dict)

# We want to use itemgetter to sort using the number of comments
submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse = True)

for submission_dict in submission_dicts:
    print("\nTitle: ", submission_dict['title'])
    print("Discussion Link: ", submission_dict['link'])
    print("Comments: ", submission_dict['comments'])

# Let us visualise the data here
specifics, titles = [], []
for submission_dict in submission_dicts:
    number_comments = submission_dict['comments']
    url_link = submission_dict['link']
    art_specifics = {
        'value': number_comments,
        'xlink': url_link
        }
    specifics.append(art_specifics)
    
    title_submission = submission_dict['title']
    titles.append(title_submission)

# Plot the data using pygal
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

chart.title = 'Most Commented Discussions on Hacker News'
chart.x_labels = titles

chart.add('', specifics)
chart.render_to_file('hacker_news_pygal.svg')
