import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    """Generate a random password based on specified preferences."""
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not any((uppercase, lowercase, digits, symbols)):
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    try:
        password = generate_password(length, uppercase, lowercase, digits, symbols)
        print("Your generated password is:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
