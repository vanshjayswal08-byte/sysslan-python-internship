import re
from typing import Tuple

def validate_email(email: str) -> Tuple[bool, str]:
    """Validate email address using basic rules with detailed feedback."""
    if not email or not email.strip():
        return False, "Email cannot be empty!"
    
    # Basic regex pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email.strip()):
        return True, f"Valid Email: {email.strip()}"
    else:
        return False, "Invalid email format. Use format like 'user@example.com'"


def main():
    print("Email Address Validator")
    print("=" * 40)
    
    email = input("Enter your email address: ").strip()
    
    is_valid, message = validate_email(email)
    
    if is_valid:
        print(f"{message}")
    else:
        print(f" {message}")


if __name__ == "__main__":
    main()