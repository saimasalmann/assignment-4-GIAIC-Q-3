def greet(name:str):
    return (f"Greetings {name} ! 🤠")


def main():
    name = input("\n\033[1;32mwhat's your name?\033[0m ")
    print(greet(name))


if __name__ == "__main__":
    main()    