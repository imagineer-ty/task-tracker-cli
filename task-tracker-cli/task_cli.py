import sys
import json
import os

TASKS_FILE = "tasks.json"

# --- Load tasks from JSON ---
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            f.write("[]")
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# --- Save tasks to JSON ---
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# --- Add a new task ---
def add_task(description):
    tasks = load_tasks()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    task = {
        "id": new_id,
        "description": description
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

# --- List all tasks ---
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']} - Description: {task['description']}")

# --- CLI argument handling ---
if len(sys.argv) < 2:
    print("Please provide a command: add or list")
else:
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description.")
        else:
            description = sys.argv[2]
            add_task(description)
    elif command == "list":
        list_tasks()
    else:
        print("Unknown command. Use 'add' or 'list'.")