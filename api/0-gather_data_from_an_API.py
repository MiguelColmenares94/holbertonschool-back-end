#!/usr/bin/python3
"""
Script that use
https://jsonplaceholder.typicode.com/guide/
to get information
"""
import requests
from sys import argv, stderr, exit


def main():
    if len(argv) < 2:
        print("Usage: {} ID".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    url_name = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_name = requests.get(url_name)

    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
    else:
        print("Error fetching TODO list")

    if response_name.status_code == 200:
        employee_data = response_name.json()
        if "name" in employee_data:
            employee_name = employee_data.get("name")
    else:
        print("Error fetching employee name")

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
