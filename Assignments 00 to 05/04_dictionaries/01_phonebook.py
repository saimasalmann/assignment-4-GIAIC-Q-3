def make_phone_book():
    """Create a phone book dictionary with names and phone numbers."""
    phonebook = {}
    while True:
        name = input("Enter name: ")
        if name == "":
            break

        phone_number = input("Enter a number: ")
        phonebook[name] = phone_number

    return phonebook

def print_phone_book(phonebook):
    for name in phonebook:
        print(f"\n\033[1;34m{name}\033[0m  has the number \033[1;33m{phonebook[name]}\033[0m.")


def look_up_number(phonebook):
    """Look up a number in the phone book."""
    name = input("Enter name to look up: ")
    if name in phonebook:
        print(f"\n\033[1;34m{name}\033[0m  has the number \033[1;33m{phonebook[name]}\033[0m.")
    else:
        print(f"\n\033[1;31m{name}\033[0m not found in the phone book.")


def main():
    """Main function to run the phone book program."""
    
    
    print("\n\033[1;32mWelcome to the Phone Book Program\033[0m")

    phonebook = make_phone_book()
    print_phone_book(phonebook)
    look_up_number(phonebook)

if __name__ == "__main__":
    main()    