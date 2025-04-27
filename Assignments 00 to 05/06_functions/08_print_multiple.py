import time


def generate_multiple(message: str, times: int):
    """
    This function prints a message a specified number of times.
    """
    for _ in range(times):
        yield (message)


def main():
    """
    Main function to execute the program.

    """
    print("\n\033[1;35mWelcome to the Message Printer!\033[0m\n")
    message = input("Enter a message: ")
    while True:
        try:
            times = int(input("Enter the number of times to print the message: "))
            if times < 0:
                print("\n\033[1;31mPlease enter a positive integer.\033[0m")
                continue
            break
        except ValueError:
            print("\n\033[1;31mInvalid input. Please enter a valid integer.\033[0m")
    for msg in generate_multiple(message, times):
        print("\033[1;34m" + msg + "\033[0m" + "......")
        time.sleep(1)
    print("\n\033[1;32mThank you for using the message printer!\033[0m")


if __name__ == "__main__":
    main()
