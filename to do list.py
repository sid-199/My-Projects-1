# Simple To-Do List Manager

import json
import os

def load_task():
    if os.path.exists("Tasks.json"):
        with open ("Tasks.json","r") as file:
            return json.load(file)
        
    return[]                        # returns empty list if no Tasks.json exists 

def save_task(tasks):
    with open ("Tasks.json","w") as file:
        json.dump(tasks,file,indent=2)

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_task(tasks)
    print(f"✅ '{task}' added successfully!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_num - 1)
            save_task(tasks)
            print(f"❌ '{removed}' removed successfully!")
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    tasks = load_task()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
