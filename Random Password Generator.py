import secrets
import string

def get_user_input():
 while True:
    try:
        Length = int(input("Enter the length of the password\n"))
        
        if Length < 8:
            print("Password must be at least 8 characters. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    include_letters = input("Do you want letters? (yes/no)\n").lower() == "yes"
    include_numbers = input("Do you want numbers? (yes/no)\n").lower() == "yes"
    include_symbols = input("Do you want symbols? (yes/no)\n").lower() == "yes"
    
    return Length, include_letters, include_numbers, include_symbols

def generate_password(length, include_letters, include_numbers, include_symbols):
   
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected for password generation.")
    
    password = ""
    for i in range(length):
        password += secrets.choice(characters)
    return password

def check_strength(password):
    score = 0
    
    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    
    if score <= 2:   return "Weak"
    elif score <= 4: return "Medium"
    else:            return "Strong"

def display_password(password):
    print(f"Your password is: {password}")

def main():
    
    while True:
        length, include_letters, include_numbers, include_symbols = get_user_input()
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        display_password(password)
        strength = check_strength(password)
        print(f"Strength: {strength}")
           
        again = input("Generate another one? (yes/no)\n").lower()
        if again != "yes":
            break
    
   
if __name__ == "__main__":
        main()
    