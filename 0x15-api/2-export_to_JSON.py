#!/usr/bin/python3
"""Fetching resources from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user_url = "{}/{}".format(url, employee_id)
    todos_url = "{}/todos".format(user_url)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if
                       task.get("completed")]

    # Get details to convert to JSON format
    user_id = user_data.get("id")
    username = user_data.get("username")

    json_content = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username,
    } for task in todos_data]

    output = {user_id: json_content}

    with open("{}.json".format(user_id), "w") as file:
        json.dump(output, file)
