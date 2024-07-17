def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})
 # Function to mark a task as completed
def mark_completed(todo_list, task_index):

    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
 # Function to display the to-do list
def display_todo_list(todo_list):
    print("To-Do List:")
    for index, task in enumerate(todo_list):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['task']} [{status}]")
 # Main program
if __name__ == "__main__":
    todo_list = []
    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display To-Do List")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(todo_list, task_name)
        elif choice == '2':
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            mark_completed(todo_list, task_index)
        elif choice == '3':
            display_todo_list(todo_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")