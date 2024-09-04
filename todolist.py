todolist = []

def show_todo_list():
    if len(todolist) == 0:
        print("Your to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todolist, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a task to add: ")
    todolist.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    show_todo_list()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = todolist.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def complete_task():
    show_todo_list()
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        completed_task = todolist[task_num - 1]
        todolist[task_num - 1] = completed_task + " (Completed)"
        print(f"'{completed_task}' has been marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            show_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
