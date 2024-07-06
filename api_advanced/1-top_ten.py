#!/usr/bin/python3
""" Get the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        try:
            posts = json_data['data']['children']
            for i in range(10):
                print(posts[i]['data']['title'])
        except (IndexError, KeyError, TypeError) as e:
            print(f"Error parsing data: {e}")
    else:
        print(None)
