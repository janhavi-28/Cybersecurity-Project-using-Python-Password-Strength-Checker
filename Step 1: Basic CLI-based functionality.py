import re

def check_password_strength(password):
    # Define the criteria for password strength
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    # Count how many criteria are met
    strength_score = sum(criteria.values())
    
    # Determine strength feedback
    if strength_score <= 2:
        strength = "Weak"
    elif strength_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    # Print feedback
    print("\nPassword Analysis:")
    print(f"Length >= 8: {'✓' if criteria['length'] else '✗'}")
    print(f"Contains Uppercase: {'✓' if criteria['uppercase'] else '✗'}")
    print(f"Contains Lowercase: {'✓' if criteria['lowercase'] else '✗'}")
    print(f"Contains Digit: {'✓' if criteria['digit'] else '✗'}")
    print(f"Contains Special Character: {'✓' if criteria['special_char'] else '✗'}")
    print(f"\nPassword Strength: {strength}")

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter a password to check its strength: ")
    check_password_strength(user_password)
