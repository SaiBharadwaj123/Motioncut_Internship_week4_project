import string
import random
import sys

def generate_password(length, num_passwords):
    # Define the character sets for uppercase letters, lowercase letters, numbers, and special characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation

    # Combine all the character sets into one
    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters

    # Generate the passwords
    passwords = []
    for _ in range(num_passwords):
        password = ''.join(random.choice(all_characters) for _ in range(length))

        # Ensure the password contains at least one uppercase letter, one lowercase letter, one number, and one special character
        while (not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password) or not any(c in special_characters for c in password)):
            password = ''.join(random.choice(all_characters) for _ in range(length))

        passwords.append(password)

    return passwords

# Get user input for password length and number of passwords to generate
print("Minimum  Password Length: 8")
c=0
while True:
    try:
        length = int(input("\nEnter a positive integer greater than 7 to set the Password Length:\t"))
        if length < 8:
            print("\n\tPlease enter an integer greater than 7.")
            c+=1
            print("Attempt",c,"to enter a valid response.")
            if c==10:
                print("Too many failed attempts.")
                sys.exit()
        else:
            break
    except ValueError:
        print("\n\tInvalid entry. Please enter a numeric value.")

d=0
while True:
    num_passwords = input("\nHow many Passwords would you like to generate?\t")
    try:
        num_passwords = int(num_passwords)
        d=0
        if num_passwords <= 0:
            raise ValueError
        elif num_passwords > 99999:
            print("\n\tThe maximum number of passwords that can be generated is 99999.")
            d=1
        else:
            break
    except(ValueError, TypeError):
        print("\n\tInvalid Entry.\n\tPlease enter a numeric value.")
        d+=1
        if d == 3:
            print('Three consecutive invalid entries. Exiting program.')
            sys.exit()
# Generate and display the passwords
passwords = generate_password(length, num_passwords)
for i, password in enumerate(passwords):
    print(f"Password {i + 1}: {password}")