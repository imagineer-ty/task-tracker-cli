Task Tracker CLI (Python)

A simple command-line interface (CLI) application to manage tasks using a JSON file for storage. This project is designed for beginners to practice working with file systems, command-line arguments, and basic program structure.

Features

Add new tasks

List all tasks

Update task descriptions

Delete tasks

Mark tasks as done

Persistent storage using a local JSON file

Requirements

Python 3.x

No external libraries required

Setup

Clone or download the repository.

Navigate to the project directory.

Ensure Python is installed:

python --version
Usage

Run the program using:

python task_cli.py <command> [arguments]
Commands
Add a Task
python task_cli.py add "Buy groceries"

Output:

Task added successfully (ID: 1)
List All Tasks
python task_cli.py list

Output:

ID: 1 - Description: Buy groceries - Status: todo
Update a Task
python task_cli.py update 1 "Buy groceries and cook dinner"
Delete a Task
python task_cli.py delete 1
Mark Task as Done
python task_cli.py mark-done 1
Data Storage

Tasks are stored in a local file named:

tasks.json

Each task contains:

id

description

status

Example:

[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo"
    }
]
Project Structure
task-tracker-cli/
 ├─ task_cli.py
 ├─ tasks.json
 └─ README.md
Learning Objectives

This project helps practice:

Command-line argument parsing

File input/output

JSON handling

Python functions and control flow

Error handling

Possible Improvements

Add task priority

Add due dates

Add in-progress status

Sort and filter tasks

Export tasks
