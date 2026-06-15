# task2_csv_reader.py
import csv
import os
from datetime import datetime

def read_csv_file(filename: str):
    """Read and display CSV data in a beautiful formatted table."""
    if not os.path.exists(filename):
        print(f"📝 Creating sample CSV: {filename}")
        os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Salary", "Joining_Date"])
            writer.writerows([
                [101, "Aarav Sharma", "Engineering", 85000, "2024-01-15"],
                [102, "Priya Patel", "Marketing", 62000, "2024-03-20"],
                [103, "Rohan Mehta", "Finance", 92000, "2023-11-10"],
                [104, "Sneha Gupta", "HR", 58000, "2024-02-05"]
            ])
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            
        print(f"\n📊 CSV Data Report - {filename}")
        print("=" * 80)
        print(f"{'ID':<4} {'Name':<18} {'Department':<15} {'Salary':<10} {'Joining Date':<15}")
        print("-" * 80)
        
        total_salary = 0
        for row in data:
            print(f"{row['ID']:<4} {row['Name']:<18} {row['Department']:<15} ₹{int(row['Salary']):<10,} {row['Joining_Date']}")
            total_salary += int(row['Salary'])
        
        print("-" * 80)
        print(f"Total Employees : {len(data)}")
        print(f"Total Salary    : ₹{total_salary:,}")
        print(f"Average Salary  : ₹{total_salary/len(data):,.0f}")
        
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

if __name__ == "__main__":
    print("📋 CSV Data Viewer")
    print("=" * 40)
    filename = input("Enter CSV filename (default: employees.csv): ").strip() or "employees.csv"
    read_csv_file(filename)