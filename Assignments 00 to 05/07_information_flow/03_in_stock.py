def num_in_stock(fruit):
    if  fruit == "apple":
        return 4
    if fruit == "banana":
        return 36
    if fruit == "orange":
        return 40
    if fruit == "kiwi":
        return 0
    return None
    

def main():
   
   while True:
   
            fruit= input("\nPlease enter the fruit. ").strip().lower()
            if fruit == "":
                continue
            
            
            if not fruit.isalpha():
                print("You didn't enter a valid fruit name (letters only) !")
                continue
              
            
            stock = num_in_stock(fruit)
            if stock == 0:
                print("Sorry, we are out of stock.")
            
            else:
                print("We have" ,stock , fruit,"/s in stock.") 
            break


if __name__ == "__main__":  
    main()           