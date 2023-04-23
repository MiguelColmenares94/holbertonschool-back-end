#!/usr/bin/python3
"""
Script that use
https://jsonplaceholder.typicode.com/guide/
to get information and export it as csv
"""
import json
import requests
from sys import argv, stderr, exit


def main():
    if len(argv) < 2:
        print("Usage: {} ID".format(argv[0]), file=stderr)
        exit(1)

    employee_id = int(argv[1])
    url_to = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response_todo = requests.get(url_to)
    url_username = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_username = requests.get(url_username)

    if response_todo.status_code == 200:
        todos = response_todo.json()
    else:
        print("Error fetching TODO list")

    if response_username.status_code == 200:
        employee_data = response_username.json()
        if "username" in employee_data:
            employee_username = employee_data.get("username")
    else:
        print("Error fetching employee username")

    tasks_list = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_username
            }
            for todo in todos
        ]

    json_data = json.dumps({employee_id: tasks_list})
    with open(f"{employee_id}.json", "w") as f:
        f.write(json_data)

    print("Data exported to {}".format(f.name))


if __name__ == "__main__":
    main()
