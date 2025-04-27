
def main():
    print("\n\033[1;32mWelcome to the even number printer!\033[0m\n")
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2 , end = "  ")  # Use the 'i' value inside the for-loop
    print()
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()