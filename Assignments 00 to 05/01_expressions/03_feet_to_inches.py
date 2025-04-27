def feet_to_inches():
    feet:float  = float(input("Please enter the number of inches! "))
    inches:float = feet * 12
    print(f"{feet} feet = {inches} inches")

if __name__ == "__main__":
    feet_to_inches()