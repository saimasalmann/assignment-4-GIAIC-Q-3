def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("\n\033[1;32mI am excited to add this " + word + " to my vast collection of them! \033[0m")
    elif part_of_speech == 1:
        # verb
        print("\n\033[1;32mIt's so nice outside today it makes me want to " + word + "!\033[0m")
    elif part_of_speech == 2:
        # adjective
        print("\n\033[1;32mLooking out my window, the sky is big and " + word + "!\033[0m")
 

# There is no need to edit code beyond this point

def main():
    word :  str = input("\n\033[1;33mPlease type a noun, verb, or adjective:\033[0m ")
    print("\n\033[1;34mIs this a noun, verb, or adjective?\033[0m ")
    while True:
        try:
            part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
            if part_of_speech in [0, 1, 2]:
                break
            else:
                print("\033[1;31mInvalid input. Please enter 0, 1, or 2.\033[0m")
        except ValueError:
            print("\033[1;31mInvalid input. Please enter a number 0 , 1 or 2.\033[0m")
   
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
