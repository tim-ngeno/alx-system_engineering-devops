#!/usr/bin/python3
"""Fetch data from the Reddit API"""

import requests


def top_ten(subreddit):
    """Returns a list of the 10 hottest posts on a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditScraper/1.0'}
    params = {'limit': 10}

    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if res.status_code != 200:
        print('None')
        return
    data = res.json().get('data')
    [print(c.get('data').get('title')) for c in data.get('children')]
