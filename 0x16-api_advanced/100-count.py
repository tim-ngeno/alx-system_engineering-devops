#!/usr/bin/python3
"""Fetch data from Reddit API and parse it"""

import requests
from collections import Counter


def count_words(subreddit, word_list, hot_list=None, after=None):
    """Parses article titles of a subreddit and counts keywords"""
    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditScraper/1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            hot_list.append(title)
        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, hot_list, after)
    else:
        return None

    if not after:
        keyword_counts = Counter(' '.join(hot_list).split())
        for word in word_list:
            count = keyword_counts.get(word.lower(), 0)
            if count > 0:
                print('{}: {}'.format(word.lower(), count))
