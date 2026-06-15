from typing import List, Dict

class RecordManager:
    """Simple Record Management System using dictionaries."""
    
    def __init__(self):
        self.records: List[Dict] = []
    
    def add_record(self, name: str, age: int, email: str, city: str):
        """Add a new record."""
        record = {
            "id": len(self.records) + 1,
            "name": name.strip().title(),
            "age": age,
            "email": email.strip().lower(),
            "city": city.strip().title()
        }
        self.records.append(record)
        print(f"Record added successfully! ID: {record['id']}")
    
    def view_records(self):
        """Display all records in a nice table format."""
        if not self.records:
            print(" No records found.")
            return
        
        print("\n All Records")
        print("=" * 70)
        print(f"{'ID':<4} {'Name':<15} {'Age':<6} {'Email':<25} {'City':<15}")
        print("-" * 70)
        for rec in self.records:
            print(f"{rec['id']:<4} {rec['name']:<15} {rec['age']:<6} {rec['email']:<25} {rec['city']:<15}")
    
    def search_record(self, name: str):
        """Search record by name."""
        found = [rec for rec in self.records if name.lower() in rec['name'].lower()]
        if found:
            print(f"\n Found {len(found)} matching record(s):")
            for rec in found:
                print(rec)
        else:
            print(f" No record found for '{name}'.")

def main():
    manager = RecordManager()
    print(" Record Management System")
    print("=" * 50)
    
    while True:
        print("\n1. Add Record")
        print("2. View All Records")
        print("3. Search Record")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            email = input("Enter Email: ")
            city = input("Enter City: ")
            manager.add_record(name, age, email, city)
            
        elif choice == "2":
            manager.view_records()
            
        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_record(name)
            
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice!")

if __name__ == "__main__":
    main()