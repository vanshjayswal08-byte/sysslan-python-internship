import random
import string

def generate_password(length: int = 12) -> str:
    """Generate a secure random password with letters and numbers."""
    if length < 6:
        length = 6  # Minimum length
    
    # Character sets
    letters = string.ascii_letters
    numbers = string.digits
    # symbols = string.punctuation  # Optional: can be added later
    
    # Ensure at least one of each
    password = [
        random.choice(letters),
        random.choice(numbers)
    ]
    
    # Fill the rest
    all_chars = letters + numbers
    password.extend(random.choice(all_chars) for _ in range(length - 2))
    
    # Shuffle for better randomness
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Random Password Generator")
    print("="*40)
    
    try:
        length = int(input("Enter password length (min 6): ") or "12")
        password = generate_password(length)
        
        print(f"\n Generated Password: {password}")
        print(f"Length: {len(password)} characters")
        print("\n Tip: Save this password securely!")
        
    except ValueError:
        print("Please enter a valid number for length.")

if __name__ == "__main__":
    main()