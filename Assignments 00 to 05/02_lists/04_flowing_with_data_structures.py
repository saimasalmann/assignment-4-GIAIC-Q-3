def make_three_copies(my_list,data):
    """Make five copies of the list and return them."""
    for i in range(5):
        my_list.append(data)


def main():
    message :str = input("Please enter a message to be copied: ")
    my_list :list[str] = []
    print(f" my_list before: {my_list}")
    make_three_copies(my_list,message)
    print(f" my_list after: {my_list}")


if __name__ == "__main__":
    main()