from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return title.strip()

def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Task description cannot be empty.")
    return description.strip()

def validate_due_date(due_date):
    if len(due_date.strip()) == 0:
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except (ValueError, TypeError):
        raise ValueError("Due date must be in YYYY-MM-DD format.")
