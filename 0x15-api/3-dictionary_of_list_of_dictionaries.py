#!/usr/bin/python3
"""Fetching resources from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Get details to convert to JSON format
    output = {}

    for user in user_data:
        user_id = user['id']
        username = user['username']

        todos_url = "{}/{}/todos".format(user_url, user_id)
        tasks = requests.get(todos_url).json()

        tasks_list = [{
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed"),
        } for task in tasks]

        output[str(user_id)] = tasks_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(output, file)
