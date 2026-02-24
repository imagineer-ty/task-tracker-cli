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
            "description": description,
            "status": "todo"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

#--- Delete tasks ---
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task ID not found.")
        return

    save_tasks(new_tasks) 
    print(f"task {task_id} deleted successfully")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print("Task ID not found.")

# --- List all tasks ---
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']} - Description: {task['description']}")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print("Task ID not found.")

# --- CLI argument handling ---
if len(sys.argv) < 2:
    print("Please provide a command: add, list, delete")

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

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print("Task ID must be a number.")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: update <id> <new description>")
        else:
            try:
                task_id = int(sys.argv[2])
                new_desc = sys.argv[3]
                update_task(task_id, new_desc)
            except ValueError:
                 print("Task ID must be a number.")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Please provide a task ID.")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_done(task_id)
            except ValueError:
                print("Task ID must be a number.")
    else:
        print("Unknown command. Use 'add', 'list', or 'delete'.")