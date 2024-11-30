import re
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to check password strength
def check_password_strength():
    password = password_entry.get()
    
    if not password:
        messagebox.showwarning("Input Error", "Password cannot be empty!")
        return
    
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
    feedback += "\nPassword Analysis:\n"
    feedback += f"Length >= 8: {'✓' if criteria['length'] else '✗'}\n"
    feedback += f"Contains Uppercase: {'✓' if criteria['uppercase'] else '✗'}\n"
    feedback += f"Contains Lowercase: {'✓' if criteria['lowercase'] else '✗'}\n"
    feedback += f"Contains Digit: {'✓' if criteria['digit'] else '✗'}\n"
    feedback += f"Contains Special Character: {'✓' if criteria['special_char'] else '✗'}\n"
    
    if suggestions:
        feedback += "\nSuggestions to Improve Your Password:\n" + "\n".join(suggestions)
    else:
        feedback += "\nYour password is strong!"
    
    # Show feedback in GUI
    result_label.config(text=feedback)
    
    # Log results to a file
    log_password_analysis(password, strength, feedback)

# Function to log results to a file
def log_password_analysis(password, strength, feedback):
    with open("password_audit_log.txt", "a") as file:
        file.write(f"Date/Time: {datetime.now()}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Strength: {strength}\n")
        file.write("Analysis:\n")
        file.write(feedback + "\n")
        file.write("=" * 50 + "\n")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")

# GUI elements
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, show="*", width=40, font=("Arial", 12))
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10), justify="left", wraplength=450)
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
