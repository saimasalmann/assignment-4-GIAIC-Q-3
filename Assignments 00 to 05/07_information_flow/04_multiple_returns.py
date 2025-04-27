def get_user_info():
    first_name = input("\nEnter your first name: ")
    last_name = input("Enter your last name: ")
    email_address = input("Enter your email address: ")
    return first_name, last_name, email_address


def main():
    user_data = get_user_info()
    print("\nUser Data: ",user_data)


if __name__ == "__main__":
    main()