import secrets
import string


ascii_7passGEN = """

8888888888 8888888b.                             .d8888b.  8888888888 888b    888
      d88P 888   Y88b                           d88P  Y88b 888        8888b   888
     d88P  888    888                           888    888 888        88888b  888
    d88P   888   d88P 8888b.  .d8888b  .d8888b  888        8888888    888Y88b 888
 88888888  8888888P"     "88b 88K      88K      888  88888 888        888 Y88b888
  d88P     888       .d888888 "Y8888b. "Y8888b. 888    888 888        888  Y88888
 d88P      888       888  888      X88      X88 Y88b  d88P 888        888   Y8888
d88P       888       "Y888888  88888P'  88888P'  "Y8888P88 8888888888 888    Y888


"""

print(ascii_7passGEN)


def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    # Define character sets based on user choices
    character_sets = []
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)
    if include_lowercase:
        character_sets.append(string.ascii_lowercase)
    if include_numbers:
        character_sets.append(string.digits)
    if include_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character category must be selected.")

    # Combine selected character sets into one string
    all_characters = ''.join(character_sets)

    # Check if the password length is at least 12
    if length < 12:
        raise ValueError("Password length should be at least 12.")

    # Generate the password using the secrets module
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")
    try:
        length = int(input("Enter the password length (at least 12): "))
        include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

# Created by: 7PiNz
