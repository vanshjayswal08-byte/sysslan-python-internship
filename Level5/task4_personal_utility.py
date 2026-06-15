# task4_personal_utility.py
import os
import json
from datetime import datetime

class PersonalUtility:
    """Mini Personal Utility Dashboard combining multiple features."""
    
    def __init__(self):
        self.data_file = "personal_data.json"
        self.load_data()
    
    def load_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except:
            self.data = {"tasks": [], "notes": [], "expenses": []}
    
    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)
    
    def show_dashboard(self):
        print("\n" + "="*60)
        print("🎯 PERSONAL UTILITY DASHBOARD")
        print("="*60)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %A')}")
        print(f"Pending Tasks : {len([t for t in self.data['tasks'] if t.get('status') != 'Done'])}")
        print(f"Total Notes   : {len(self.data['notes'])}")
        print(f"Total Expense : ₹{sum(exp.get('amount', 0) for exp in self.data['expenses'])}")
        print("="*60)

if __name__ == "__main__":
    print("🛠️  Personal Utility Tool")
    print("=" * 50)
    
    utility = PersonalUtility()
    utility.show_dashboard()
    
    print("\nThis tool combines file handling, task management, and data persistence.")
    print("You can extend it further with more features!")