# task4_unique_check.py
def check_unique_numbers():
    """Check if all numbers in grid are unique with detailed analysis."""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Uniqueness Check")
    print("="*25)
    
    # Flatten the grid
    all_numbers = [num for row in grid for num in row]
    
    # Check uniqueness
    if len(all_numbers) == len(set(all_numbers)):
        print(" All numbers in the grid are UNIQUE!")
        print(f"Total numbers: {len(all_numbers)}")
    else:
        print("Duplicate numbers found!")
        
    # Bonus: Show frequency
    from collections import Counter
    freq = Counter(all_numbers)
    print("\nNumber Frequency:")
    for num, count in sorted(freq.items()):
        status = "✅" if count == 1 else "❌"
        print(f"{status} Number {num}: {count} time(s)")

if __name__ == "__main__":
    check_unique_numbers()