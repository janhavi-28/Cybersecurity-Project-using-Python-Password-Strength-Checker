import re

def check_password_strength(password):
    # Define criteria
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
    
    # Suggestions for improvement
    suggestions = []
    if not criteria["length"]:
        suggestions.append("Increase the password length to at least 8 characters.")
    if not criteria["uppercase"]:
        suggestions.append("Add at least one uppercase letter.")
    if not criteria["lowercase"]:
        suggestions.append("Add at least one lowercase letter.")
    if not criteria["digit"]:
        suggestions.append("Include at least one numeric digit.")
    if not criteria["special_char"]:
        suggestions.append("Use at least one special character (e.g., !@#$%^&*).")
    
    # Feedback
    feedback = f"Password Strength: {strength}\n"
    if suggestions:
        feedback += "\nSuggestions to Improve Your Password:\n" + "\n".join(suggestions)
    else:
        feedback += "\nYour password is strong!"
    
    print(feedback)

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter a password: ")
    check_password_strength(user_password)
