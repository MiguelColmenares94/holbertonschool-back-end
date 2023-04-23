#!/usr/bin/python3
"""
Script that use
https://jsonplaceholder.typicode.com/guide/
to get information and export it as csv
"""
import csv
import requests
from sys import argv, stderr, exit


def main():
    if len(argv) < 2:
        print("Usage: {} ID".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    url_to = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response_todo = requests.get(url_to)
    url_username = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_username = requests.get(url_username)

    if response_todo.status_code == 200:
        todos = response_todo.json()
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
    else:
        print("Error fetching TODO list")

    if response_username.status_code == 200:
        employee_data = response_username.json()
        if "username" in employee_data:
            employee_username = employee_data.get("username")
    else:
        print("Error fetching employee username")

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, mode='w') as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        # writer.writeheader()

        for task in todos:
            writer.writerow({
                "USER_ID": '{}'.format(employee_id),
                "USERNAME": '{}'.format(employee_username),
                "TASK_COMPLETED_STATUS": '{}'.format(task.get("completed")),
                "TASK_TITLE": '{}'.format(task.get("title"))
            })

    print("Data exported to {}".format(csv_file))


if __name__ == "__main__":
    main()
