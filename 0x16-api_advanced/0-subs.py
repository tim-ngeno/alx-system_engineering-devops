#!/usr/bin/python3
"""Fetch data from the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'MyRedditScraper/1.0'}

    # Send a GET request to the API
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    subscribers = data['data']['subscribers']
    return subscribers
