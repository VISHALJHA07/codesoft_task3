import secrets
import string

# Define a list of characters to include in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Get user input for desired password length
password_length = int(input("Enter the desired length of your password: "))

# Generate a password using secrets.choice() for better security
password = ''.join(secrets.choice(characters) for i in range(password_length))

# Print the generated password
print("Your generated password is:", password)
