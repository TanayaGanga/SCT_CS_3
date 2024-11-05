import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    # Check each criterion and note missing ones
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    number_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Build a list of missing criteria
    missing_criteria = []
    if not length_criteria:
        missing_criteria.append("at least 8 characters")
    if not uppercase_criteria:
        missing_criteria.append("an uppercase letter")
    if not lowercase_criteria:
        missing_criteria.append("a lowercase letter")
    if not number_criteria:
        missing_criteria.append("a number")
    if not special_char_criteria:
        missing_criteria.append("a special character")
    
    # If any criteria are missing, show the list of missing items
    if missing_criteria:
        missing_message = "Your password is missing:\n" + "\n".join(missing_criteria)
        return missing_message
    
    # If all criteria are met, return strength level
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

def on_submit():
    password = entry.get()
    strength_or_message = assess_password_strength(password)
    
    # Create a new window to display the result with larger font
    result_window = tk.Toplevel(root)
    result_window.title("Password Strength Result")
    result_label = tk.Label(result_window, text=strength_or_message, font=("Helvetica", 14, "bold"))
    result_label.pack(pady=10, padx=10)

# Setting up the main GUI window
root = tk.Tk()
root.title("Password Strength Tool")

# Increase font size for label and entry box
label = tk.Label(root, text="Enter your password:", font=("Helvetica", 14))
label.pack(pady=5)

entry = tk.Entry(root, show="*", font=("Helvetica", 14), width=30)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Check Strength", command=on_submit, font=("Helvetica", 14))
submit_button.pack(pady=10)

root.mainloop()
