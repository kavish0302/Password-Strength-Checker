import re

def password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Password strength
    strength = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main
if __name__ == "__main__":
    while True:
        user_input = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the password strength checker.")
            break
        strength = password_strength(user_input)
        print(f"Password: {user_input} - Strength: {strength}")


#Examples
#Password123! , Str0ngP@ssword! - VS
#P@ssw0rd , 1234Abcd! - S
#PASSWORD , 12345678 - W
#pass , weakpassword - VW