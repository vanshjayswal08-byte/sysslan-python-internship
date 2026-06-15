# task2_file_storage.py
import json
import os
from datetime import datetime

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

def save_to_file(records, filename="data/records.json"):
    """Save records to JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(records, f, indent=4, ensure_ascii=False)
        print(f"✅ Records successfully saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def load_from_file(filename="data/records.json"):
    """Load records from JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"📁 {filename} not found. Starting fresh.")
        return []
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return []

def main():
    print("💾 File-Based Record Storage System")
    print("=" * 55)
    
    # Import RecordManager from task1
    try:
        from task1_record_management import RecordManager
    except ImportError:
        print("❌ task1_record_management.py not found in same folder!")
        return
    
    manager = RecordManager()
    manager.records = load_from_file()
    
    # Add sample records if empty
    if not manager.records:
        print("Adding sample records...")
        manager.add_record("Aarav Sharma", 22, "aarav@example.com", "Mumbai")
        manager.add_record("Priya Patel", 20, "priya@example.com", "Delhi")
    
    # Save records
    save_to_file([rec for rec in manager.records])
    
    # Display records
    manager.view_records()

if __name__ == "__main__":
    main()