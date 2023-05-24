#!/usr/bin/python3
"""This module gathers data from an API"""
import json
import requests

if __name__ == "__main__":

    # Make requests in parallel to reduce overhead
    session = requests.Session()
    response_todos = session.get("https://jsonplaceholder.typicode.com/todos")
    response_users = session.get("https://jsonplaceholder.typicode.com/users")

    # Check if the requests were successful (status code 200)
    if response_todos.status_code != 200 or response_users.status_code != 200:
        print("Failed to fetch data.")
        print(f"TODOS response status code: {response_todos.status_code}")
        print(f"Users response status code: {response_users.status_code}")
        exit(1)

    todos = response_todos.json()
    users = response_users.json()

    todo_all_employees = {}
    for user in users:
        user_id = user.get("id")
        todo_all_employees[user_id] = []

    for todo in todos:
        user_id = todo.get("userId")
        if user_id in todo_all_employees:
            user = [user for user in users if user["id"] == user_id][0]
            todo_all_employees[user_id].append({
                "username": user.get("username"),
                "task": todo["title"],
                "completed": todo["completed"]
            })

    # Export to JSON region
    filename = "todo_all_employees.json"
    with open(filename, mode="w") as file:
        json.dump(todo_all_employees, file, indent=4)
