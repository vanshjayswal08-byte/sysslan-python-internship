from datetime import datetime

def read_file_safely(filename: str):
    """Read and display file content line by line with proper error handling."""
    line_num = 0  # Initialize to avoid unbound variable error
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"\n Content of '{filename}':")
            print("=" * 60)
            
            for line_num, line in enumerate(file, 1):
                print(f"{line_num:4d}: {line.rstrip()}")
            
            print("=" * 60)
            print(f" Total lines read: {line_num}")
    
    except FileNotFoundError:
        print(f" Error: File '{filename}' not found.")
    except PermissionError:
        print(f" Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f" Unexpected error: {e}")

def main():
    print(" Safe File Reader")
    print("=" * 40)
    
    filename = input("Enter filename to read (e.g., sample.txt): ").strip()
    if not filename:
        filename = "sample.txt"
    
    # Create sample file if it doesn't exist
    if not os.path.exists(filename):
        print(f" Creating sample file: {filename}")
        os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Hello Intern!\n")
            f.write("Welcome to Sysslan IT Solutions Python Internship.\n")
            f.write(f"Today's Date: {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("Task 3 - Safe File Reading Completed.\n")
    
    read_file_safely(filename)

if __name__ == "__main__":
    import os
    main()