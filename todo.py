# To-Do List Application (CLI)
# Stores tasks in tasks.json in the same folder.
import json, os
FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i,t in enumerate(tasks,1):
        status = "✓" if t.get("done") else " "
        print(f"{i}. [{status}] {t.get('title')} - {t.get('desc','')}")

def add_task(tasks):
    title = input("Title: ").strip()
    desc = input("Description (optional): ").strip()
    tasks.append({"title": title, "desc": desc, "done": False})
    save_tasks(tasks)
    print("Added.")

def mark_done(tasks):
    list_tasks(tasks)
    try:
        i = int(input("Task number to toggle done: "))
        tasks[i-1]["done"] = not tasks[i-1].get("done", False)
        save_tasks(tasks)
        print("Updated.")
    except Exception as e:
        print("Invalid selection.", e)

def delete_task(tasks):
    list_tasks(tasks)
    try:
        i = int(input("Task number to delete: "))
        tasks.pop(i-1)
        save_tasks(tasks)
        print("Deleted.")
    except Exception as e:
        print("Invalid selection.", e)

def menu():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List - Menu")
        print("1. List tasks")
        print("2. Add task")
        print("3. Toggle done")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    menu()
