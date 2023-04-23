#!/usr/bin/python3
"""
Script that use
https://jsonplaceholder.typicode.com/guide/
to get information and export it as csv
"""
import requests
from sys import argv, stderr, exit
import csv


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

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, mode='w') as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos:
            task_title = task.get("title")
            task_status = "True" if task['completed'] else "False"
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

    print("Data exported to {}".format(csv_file))


if __name__ == "__main__":
    main()
