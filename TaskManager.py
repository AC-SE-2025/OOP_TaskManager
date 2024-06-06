class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed"""
        pass

    def update_description(self, new_description):
        """Update the task description"""
        pass

    def update_due_date(self, new_due_date):
        """Update the task due date"""
        pass

    def update_priority(self, new_priority):
        """Update the task priority"""
        pass

    def __str__(self):
        """Return a string representation of the task"""
        return f"Task(description={self.description}, due_date={self.due_date}, priority={self.priority}, completed={self.completed})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        """Add a new task to the task list"""
        pass

    def remove_task(self, task_id):
        """Remove a task by its ID"""
        pass

    def mark_task_completed(self, task_id):
        """Mark a specific task as completed by its ID"""
        pass

    def update_task_description(self, task_id, new_description):
        """Update the description of a specific task by its ID"""
        pass

    def update_task_due_date(self, task_id, new_due_date):
        """Update the due date of a specific task by its ID"""
        pass

    def update_task_priority(self, task_id, new_priority):
        """Update the priority of a specific task by its ID"""
        pass

    def display_all_tasks(self):
        """Display all tasks"""
        if self.tasks == []:
            print("No tasks to show.")
        else:
            retunr self.tasks

    def display_pending_tasks(self):
        """Display all pending (not completed) tasks"""
        pass

    def display_completed_tasks(self):
        """Display all completed tasks"""
        pass

    def save_tasks_to_file(self, filename):
        """Save all tasks to a file"""
        pass

    def load_tasks_from_file(self, filename):
        """Load tasks from a file"""
        pass

    def sort_tasks_by_due_date(self):
        """Sort tasks by their due dates"""
        pass

    def sort_tasks_by_priority(self):
        """Sort tasks by their priority"""
        pass


# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task("Complete homework", "2024-06-10", "High")
    task_manager.add_task("Buy groceries", "2024-06-05", "Medium")
    task_manager.display_all_tasks()
