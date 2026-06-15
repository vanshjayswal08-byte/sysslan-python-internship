def search_number_in_grid():
    """Search for a number in 3x3 grid with user input and position display."""
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print(" Number Search in Grid")
    try:
        num = int(input("Enter number to search (1-9): "))
        
        found = False
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == num:
                    print(f"Number {num} found at position: Row {i+1}, Column {j+1}")
                    found = True
                    break
            if found:
                break
                
        if not found:
            print(f" Number {num} not found in the grid.")
            
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    search_number_in_grid()