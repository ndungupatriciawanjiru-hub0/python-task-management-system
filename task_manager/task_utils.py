from datetime import datetime

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    valid_title = validate_task_title(title)
    valid_desc = validate_task_description(description)
    valid_date = validate_due_date(due_date)
    
    task = {
        "title": valid_title,
        "description": valid_desc,
        "due_date": valid_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        print("Pending Tasks:")
        for i, task in enumerate(tasks):
            if not task["completed"]:
                print(f"{i}. {task['title']}: {task['description']} (Due: {task['due_date']})")
    return pending

def calculate_progress(tasks=tasks):
    if not tasks:
        progress = 0.0
    else:
        completed = sum(1 for task in tasks if task["completed"])
        progress = (completed / len(tasks)) * 100
    return progress
