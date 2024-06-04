def test_task_methods():
    # Create a Task instance
    task = Task("Write report", "2024-06-15", "High")
    
    # Test mark_completed method
    task.mark_completed()
    assert task.completed == True, "Test mark_completed Failed"
    print("Test mark_completed Passed")

    # Test update_description method
    task.update_description("Write annual report")
    assert task.description == "Write annual report", "Test update_description Failed"
    print("Test update_description Passed")

    # Test update_due_date method
    task.update_due_date("2024-06-20")
    assert task.due_date == "2024-06-20", "Test update_due_date Failed"
    print("Test update_due_date Passed")

    # Test update_priority method
    task.update_priority("Medium")
    assert task.priority == "Medium", "Test update_priority Failed"
    print("Test update_priority Passed")

    # Test __str__ method
    assert str(task) == "Task(description=Write annual report, due_date=2024-06-20, priority=Medium, completed=True)", "Test __str__ Failed"
    print("Test __str__ Passed")


def test_task_manager_methods():
    task_manager = TaskManager()

    # Test add_task method
    task_manager.add_task("Write report", "2024-06-15", "High")
    assert len(task_manager.tasks) == 1, "Test add_task Failed"
    print("Test add_task Passed")

    # Test remove_task method
    task_manager.remove_task(0)
    assert len(task_manager.tasks) == 0, "Test remove_task Failed"
    print("Test remove_task Passed")

    # Add tasks for further testing
    task_manager.add_task("Write report", "2024-06-15", "High")
    task_manager.add_task("Buy groceries", "2024-06-05", "Medium")

    # Test mark_task_completed method
    task_manager.mark_task_completed(0)
    assert task_manager.tasks[0].completed == True, "Test mark_task_completed Failed"
    print("Test mark_task_completed Passed")

    # Test update_task_description method
    task_manager.update_task_description(0, "Write annual report")
    assert task_manager.tasks[0].description == "Write annual report", "Test update_task_description Failed"
    print("Test update_task_description Passed")

    # Test update_task_due_date method
    task_manager.update_task_due_date(0, "2024-06-20")
    assert task_manager.tasks[0].due_date == "2024-06-20", "Test update_task_due_date Failed"
    print("Test update_task_due_date Passed")

    # Test update_task_priority method
    task_manager.update_task_priority(0, "Low")
    assert task_manager.tasks[0].priority == "Low", "Test update_task_priority Failed"
    print("Test update_task_priority Passed")

    # Test display_all_tasks method
    print("Display All Tasks:")
    task_manager.display_all_tasks()
    
    # Test display_pending_tasks method
    print("Display Pending Tasks:")
    task_manager.display_pending_tasks()
    
    # Test display_completed_tasks method
    print("Display Completed Tasks:")
    task_manager.display_completed_tasks()

    # Test save_tasks_to_file and load_tasks_from_file methods
    task_manager.save_tasks_to_file("tasks.txt")
    task_manager.tasks = []  # Clear current tasks
    task_manager.load_tasks_from_file("tasks.txt")
    assert len(task_manager.tasks) == 2, "Test save/load_tasks_to/from_file Failed"
    assert task_manager.tasks[0].description == "Write annual report", "Test save/load_tasks_to/from_file Failed"
    assert task_manager.tasks[1].description == "Buy groceries", "Test save/load_tasks_to/from_file Failed"
    print("Test save/load_tasks_to/from_file Passed")

    # Test sort_tasks_by_due_date method
    task_manager.sort_tasks_by_due_date()
    assert task_manager.tasks[0].due_date == "2024-06-05", "Test sort_tasks_by_due_date Failed"
    print("Test sort_tasks_by_due_date Passed")

    # Test sort_tasks_by_priority method
    task_manager.sort_tasks_by_priority()
    assert task_manager.tasks[0].priority == "Medium", "Test sort_tasks_by_priority Failed"
    print("Test sort_tasks_by_priority Passed")


if __name__ == "__main__":
    test_task_methods()
    test_task_manager_methods()
    print("All tests completed.")
