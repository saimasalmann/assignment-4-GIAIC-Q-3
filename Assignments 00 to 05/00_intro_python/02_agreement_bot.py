def main():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    fav_animal = input("\nWhat is your favorite animal? ")
    print(f"My favorite animal is also a {BOLD_ITALIC}{fav_animal}!    {RESET}")

if __name__ == "__main__":
    main()
