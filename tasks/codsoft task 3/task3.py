import random

def make_pw():
    print("Create Your Password")
    
    # Ask for password size
    while True:
        try:
            pw_size = int(input("How long? (8-16 is good): "))
            if 4 <= pw_size <= 50:
                break
            print("Pick between 4 and 50")
        except:
            print("Numbers only please")
    
    # Ask what to include
    print("\nWhat should be in it?")
    has_upper = input("Big letters (A-Z)? (y/n): ").lower() == 'y'
    has_numbers = input("Numbers (0-9)? (y/n): ").lower() == 'y'
    has_symbols = input("Symbols (!@#)? (y/n): ").lower() == 'y'
    
    # Make character list
    chars = list("abcdefghijklmnopqrstuvwxyz")
    if has_upper:
        chars += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if has_numbers:
        chars += list("0123456789")
    if has_symbols:
        chars += list("!@#$%^&*")
    
    # Build password
    password = []
    for _ in range(pw_size):
        password.append(random.choice(chars))
    
    # Show result
    print("\nYour new password:")
    print(''.join(password))
    print("\nCopy it somewhere safe!")

# Run it
if __name__ == "__main__":
    make_pw()