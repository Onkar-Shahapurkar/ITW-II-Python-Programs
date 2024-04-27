import itertools

def brute_force_crack(password, characters, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            brute_password = ''.join(attempt)
            if brute_password == password:
                return brute_password

# Define the password to be cracked
password_to_crack = "onkar2814"

# Define the characters to be used in the brute force attempt
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define the maximum length of the brute force attempt
max_length = 10

# Attempt to crack the password
cracked_password = brute_force_crack(password_to_crack, characters, max_length)

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Failed to crack the password.")
