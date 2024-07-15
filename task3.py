import string
import random

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        if password:
            print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
