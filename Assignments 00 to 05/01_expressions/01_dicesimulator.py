
# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()