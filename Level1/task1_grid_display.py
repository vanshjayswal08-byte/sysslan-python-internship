def display_number_grid():
    """Display a beautiful 3x3 number grid with proper formatting."""
    print("3x3 Number Grid\n" + "="*20)
    
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    for row in grid:
        print("  " + " | ".join(f"{num:2d}" for num in row))
        if row != grid[-1]:  # Don't print separator after last row
            print("  " + "-"*11)
    
    print("="*20)

if __name__ == "__main__":
    display_number_grid()