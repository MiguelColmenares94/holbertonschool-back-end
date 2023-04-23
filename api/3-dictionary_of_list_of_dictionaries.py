import json
import requests


def main():
    url_base = "https://jsonplaceholder.typicode.com"
    response_users = requests.get(f"{url_base}/users")

    if response_users.status_code == 200:
        users = response_users.json()
    else:
        print("Error fetching employee data")

    tasks = {}
    for user in users:
        user_id = str(user["id"])
        response_todos = requests.get(f"{url_base}/todos?userId={user_id}")
        if response_todos.status_code == 200:
            todos = response_todos.json()
        else:
            print(f"Error fetching TODO list for user {user_id}")
            continue
        tasks[user_id] = list(
            map(
                lambda todo: {
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                },
                todos
            )
        )

    with open("todo_all_employees.json", "w") as f:
        json.dump(tasks, f)

    print(f"Data exported to {f.name}")


if __name__ == "__main__":
    main()
