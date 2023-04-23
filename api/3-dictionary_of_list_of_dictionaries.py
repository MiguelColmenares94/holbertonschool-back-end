#!usr/bin/python2
"""
Get data from an API and export it to a JSON file
"""
import json
import requests


def main():
    # fetch user IDs for all employees
    url_users = "https://jsonplaceholder.typicode.com/users"
    response_users = requests.get(url_users)

    if response_users.status_code == 200:
        users = response_users.json()
        employee_ids = [user.get("id") for user in users]
    else:
        print("Error fetching employee IDs")

    # fetch through employees IDs and fetch tasks and usernames
    all_tasks = {}

    for employee_id in employee_ids:
        url_to = f"https://jsonplaceholder.typi\
                    code.com/todos?userId={employee_id}"
        response_todo = requests.get(url_to)
        url_username = f"https://jsonplaceholder.typi\
                        code.com/users/{employee_id}"
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

        # after fetch create a list of dicts with task info for each employee
        tasks_list = [
            {
                "username": employee_username,
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in todos
        ]

        all_tasks[employee_id] = tasks_list

    # export to a json file
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_tasks, f, ensure_ascii=False, indent=4)

    print("Data exported to {}".format(f.name))


if __name__ == "__main__":
    main()
