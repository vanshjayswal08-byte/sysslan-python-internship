def calculate_row_sums():
    """Calculate and display row sums with total sum."""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Row Sum Analysis")
    print("="*30)
    
    total_sum = 0
    for i, row in enumerate(grid, 1):
        row_sum = sum(row)
        total_sum += row_sum
        print(f"Row {i}: {row} → Sum = {row_sum}")
    
    print("-"*30)
    print(f"Grand Total Sum: {total_sum}")
    print(f"Average Row Sum: {total_sum/len(grid):.2f}")

if __name__ == "__main__":
    calculate_row_sums()