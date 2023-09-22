import random
import string
import pyperclip  # Import the pyperclip library

def generate_password():
    # Define the character sets for different types of characters
    special_characters = string.punctuation  # Special characters
    numbers = string.digits  # Numbers
    lowercase_letters = string.ascii_lowercase  # Lowercase letters

    # Create a list of characters to choose from
    all_characters = special_characters + numbers + lowercase_letters

    # Determine the length of the password (between 10 and 18 characters)
    password_length = random.randint(10, 18)

    # Ensure that at least one special character and one number are included
    password = [random.choice(special_characters),
                random.choice(numbers)]

    # Fill the remaining characters with random choices
    for _ in range(password_length - 2):
        password.append(random.choice(all_characters))

    # Shuffle the characters to randomize the order
    random.shuffle(password)

    # Convert the list of characters to a string
    generated_password = ''.join(password)

    return generated_password

def main():
    while True:
        # Generate a password
        password = generate_password()

        # Copy the generated password to the clipboard
        pyperclip.copy(password)

        # Display the generated password to the user
        print("Generated Password:", password)
        print("Password copied to clipboard.")

        # Ask the user if they want to generate another password
        user_input = input("Generate another password? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

if __name__ == "__main__":
    main()
