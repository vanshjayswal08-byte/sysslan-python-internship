# task3_daily_task_manager.py
import json
from datetime import datetime
import os

TASK_FILE = "tasks/daily_tasks.json"

def load_tasks():
    os.makedirs(os.path.dirname(TASK_FILE), exist_ok=True)
    try:
        with open(TASK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({
            "id": len(tasks) + 1,
            "task": task,
            "status": "Pending",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        print("✅ Task added!")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
        return
    print("\n📋 Your Daily Tasks")
    print("=" * 60)
    for t in tasks:
        status = "✅" if t['status'] == "Completed" else "⏳"
        print(f"{t['id']:2d}. {status} {t['task']} ({t['date']})")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        tid = int(input("\nEnter task ID to mark complete: "))
        for task in tasks:
            if task['id'] == tid:
                task['status'] = "Completed"
                print(f"✅ Task {tid} marked as completed!")
                return
        print("❌ Task not found.")
    except ValueError:
        print("❌ Invalid input.")

def main():
    print("📅 Daily Task Manager")
    print("=" * 50)
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Exit")
        
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()