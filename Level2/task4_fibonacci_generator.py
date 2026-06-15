# task4_fibonacci_generator.py
def generate_fibonacci(n: int):
    """Generate Fibonacci sequence with multiple display formats."""
    if n <= 0:
        print(" Please enter a positive number.")
        return
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    print(f" Fibonacci Sequence (First {n} terms)")
    print("="*50)
    
    # Display in single line
    print("Sequence :", ' '.join(map(str, fib[:n])))
    
    # Bonus: Show in table format
    print("\nIndex | Fibonacci Number")
    print("-" * 25)
    for i, num in enumerate(fib[:n]):
        print(f"{i:5d} | {num:15d}")

def main():
    print(" Fibonacci Sequence Generator")
    print("="*50)
    
    try:
        terms = int(input("How many terms do you want? (e.g., 10): "))
        generate_fibonacci(terms)
    except ValueError:
        print(" Please enter a valid integer!")

if __name__ == "__main__":
    main()