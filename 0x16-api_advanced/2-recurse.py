#!/usr/bin/python3
"""Query reddit API"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list containing hot article titles for a subreddit"""
    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditScraper/1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
