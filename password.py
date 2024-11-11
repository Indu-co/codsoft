import random
import string

def generate_password(length, complexity):
    """
    Generate a random password based on length and complexity.

    Parameters:
    length (int): The desired length of the password.
    complexity (str): The complexity level ('low', 'medium', 'high').

    Returns:
    str: A random password.
    """
    if complexity == 'low':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose from 'low', 'medium', or 'high'.")
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        complexity = input("Enter the desired complexity ('low', 'medium', 'high'): ").lower()
        if length < 4:
            print("Password length should be at least 4 characters.")
            return
        
        if complexity not in ['low', 'medium', 'high']:
            print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
            return
    
        password = generate_password(length, complexity)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
