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
        print(f"To use this script the input should be: \
              python3 file_name.py employeeID", file=stderr)
        exit(1)

    employee_id = int(argv[1])
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        """employee_name = todos[0]['name']"""

    url_name = f"https://jsonplaceholder.typicode.com/users/1"
    response_name = requests.get(url_name)

    if response_name.status_code == 200:
        employee_data = response_name.json()
        if "name" in employee_data:
            employee_name = employee_data["name"]

        print(f"Employee {employee_name} is done with \
                tasks({num_completed_tasks}/{total_tasks}): ")
        for task in completed_tasks:
            print("\t", task['title'])
    else:
        print("Error fetching TODO list")


if __name__ == "__main__":
    main()
