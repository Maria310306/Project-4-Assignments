import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters to form the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask user for the password length and number of passwords to generate
password_length = int(input("Enter the length of the password: "))
num_passwords = int(input("Enter the number of passwords to generate: "))

# Generate and display the specified number of passwords
print("\nGenerated Passwords:")
for _ in range(num_passwords):
    print(generate_password(password_length))
