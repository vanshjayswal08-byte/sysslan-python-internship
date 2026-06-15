# task2_student_report_generator.py
import json
from datetime import datetime

def generate_student_report():
    """Generate professional student performance report."""
    students = [
        {"name": "Aarav Sharma", "marks": [85, 92, 78, 95]},
        {"name": "Priya Patel", "marks": [88, 76, 91, 82]},
        {"name": "Rohan Mehta", "marks": [95, 89, 94, 87]},
        {"name": "Sneha Gupta", "marks": [72, 85, 68, 90]}
    ]
    
    print("📊 Student Performance Report")
    print("=" * 60)
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    report_data = []
    
    for student in students:
        total = sum(student['marks'])
        avg = total / len(student['marks'])
        grade = "A+" if avg >= 90 else "A" if avg >= 80 else "B" if avg >= 70 else "C"
        
        print(f"Student     : {student['name']}")
        print(f"Marks       : {student['marks']}")
        print(f"Total       : {total}")
        print(f"Average     : {avg:.2f}")
        print(f"Grade       : {grade}")
        print("-" * 40)
        
        report_data.append({
            "name": student['name'],
            "total": total,
            "average": round(avg, 2),
            "grade": grade
        })
    
    # Save report
    with open("student_report.json", 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4)
    print("💾 Report saved as 'student_report.json'")

if __name__ == "__main__":
    generate_student_report()