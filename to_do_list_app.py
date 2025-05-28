import os


def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task, status = line.strip().split('|')
                tasks.append({'task': task, 'done': status == 'done'})
    return tasks

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for t in tasks:
            status = 'done' if t['done'] else 'not done'
            file.write(f"{t['task']}|{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        status = "✓" if t['done'] else "✗"
        print(f"{i+1}. [{status}] {t['task']}")
    print()

def add_task(tasks):
    task = input("Enter your new task: ")
    tasks.append({'task': task, 'done': False})
    print("Task added.\n")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['done'] = True
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Removed task: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a number.\n")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("---- TO-DO LIST ----")
        print("1. Show all tasks")
        print("2. Add new task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Save and exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks, filename)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
main()
