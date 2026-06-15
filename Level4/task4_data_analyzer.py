# task4_data_analyzer.py
def analyze_numbers(filename: str = "numbers.txt"):
    """Read numbers from file and show statistical analysis."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            numbers = []
            for line in f:
                for num in line.split():
                    try:
                        numbers.append(float(num))
                    except ValueError:
                        continue  # Skip non-numeric values
        
        if not numbers:
            print("❌ No valid numbers found in file.")
            return
        
        print("📈 Numerical Data Analysis")
        print("=" * 50)
        print(f"Total Numbers : {len(numbers)}")
        print(f"Sum           : {sum(numbers):.2f}")
        print(f"Average       : {sum(numbers)/len(numbers):.2f}")
        print(f"Maximum       : {max(numbers):.2f}")
        print(f"Minimum       : {min(numbers):.2f}")
        
        # Save summary
        with open("analysis_summary.txt", 'w', encoding='utf-8') as f:
            f.write(f"Analysis Report - {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"Total: {len(numbers)}\n")
            f.write(f"Sum: {sum(numbers):.2f}\n")
            f.write(f"Average: {sum(numbers)/len(numbers):.2f}\n")
            f.write(f"Max: {max(numbers):.2f}\n")
            f.write(f"Min: {min(numbers):.2f}\n")
        
        print("💾 Summary saved to 'analysis_summary.txt'")
    
    except FileNotFoundError:
        print(f"📝 Creating sample '{filename}'...")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("45 78 92 33 67 89 55 91 76 84")
        analyze_numbers(filename)

if __name__ == "__main__":
    from datetime import datetime
    print("🔢 Data Analyzer from File")
    print("=" * 50)
    analyze_numbers()