# Task Management System

A simple command-line Python program that lets users add tasks, mark them as complete, view pending tasks, and track overall progress. Built as part of the Moringa School coding lab on functions, modules, and packages.

## Features

- Add a task with a title, description, and due date
- Mark a task as complete by its list index
- View all pending (incomplete) tasks
- Track progress as a percentage of completed tasks
- Validates user input (empty titles/descriptions, malformed due dates) before adding a task

## Project Structure

```
.
├── main.py
└── task_manager/
    ├── __init__.py
    ├── task_utils.py
    └── validation.py
```

- **main.py** — Menu-driven interface for interacting with the system.
- **task_manager/task_utils.py** — Core logic: `add_task`, `mark_task_as_complete`, `view_pending_tasks`, `calculate_progress`.
- **task_manager/validation.py** — Input validation: `validate_task_title`, `validate_task_description`, `validate_due_date`.

## Task Structure

Each task is stored as a dictionary:

```
{"title": "Groceries", "description": "Shop at Market Basket for food", "due_date": "2024-06-26", "completed": False}
```

## How to Run

From the project's top-level folder (the one containing `main.py`), run:

```
python3 main.py
```

Then follow the on-screen menu:

1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit

## Validation Rules

- Task title and description must not be empty.
- Due date must be in `YYYY-MM-DD` format and represent a real calendar date.
- Tasks that fail validation are not added, and an error message is printed instead.

## Author

Patricia Ndungu — Moringa School (SDF-TFR18M3)