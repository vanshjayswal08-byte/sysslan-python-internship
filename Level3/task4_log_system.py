from datetime import datetime
import os

def log_activity(message: str, log_file="logs/activity.log"):
    """Create a timestamped log entry."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f" Logged: {message}")

def view_logs(log_file="logs/activity.log"):
    """View all log entries."""
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            print(f"\n Log History ({log_file})")
            print("=" * 60)
            print(f.read())
    except FileNotFoundError:
        print(" No logs found yet.")

def main():
    print("📋 Activity Log System")
    print("=" * 50)
    
    while True:
        print("\n1. Log Activity")
        print("2. View Logs")
        print("3. Exit")
        
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            msg = input("Enter activity message: ")
            log_activity(msg)
        elif choice == "2":
            view_logs()
        elif choice == "3":
            log_activity("Session ended")
            print(" Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()