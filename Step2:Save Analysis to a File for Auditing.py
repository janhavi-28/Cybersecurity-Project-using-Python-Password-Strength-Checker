import re
from datetime import datetime

def check_password_strength(password):
    # Define the criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    
    # Calculate strength
    strength_score = sum(criteria.values())
    if strength_score <= 2:
        strength = "Weak"
    elif strength_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    # Log to a file
    with open("password_audit_log.txt", "a") as file:
        file.write(f"Date/Time: {datetime.now()}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Strength: {strength}\n")
        file.write(f"Criteria Met: {criteria}\n")
        file.write("\n")
    
    return strength

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter a password: ")
    strength = check_password_strength(user_password)
    print(f"Password Strength: {strength}")
    print("Results logged to 'password_audit_log.txt'")
