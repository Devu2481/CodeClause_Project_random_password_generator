import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def validate_length(length):
    if not length.isdigit():
        return False
    if int(length) < 8:
        return False
    return True

# Take input from the user for the desired password length
length = input("Enter the length of the password (minimum 8 characters): ")

# Validate the input length
while not validate_length(length):
    print("Invalid length. Please enter a valid length (minimum 8 characters).")
    length = input("Enter the length of the password: ")

# Generate the password using the given length
password = generate_password(int(length))
print("Generated password:", password)
