
def main():
    print("\n\033[1;32mWelcome to the fruit shop!\033[0m\n")
    fruits = {
        'apple': 250,
        'mango': 300,
        'pomegranate': 400,
        'grapes': 350,
        'guava': 180,

    }    
    total_cost = 0 
    for fruit_name in fruits:
        price = fruits[fruit_name]
    
        try:
            amount_to_buy = int(input(f"How many {fruit_name} do you want to buy?  "))
        except ValueError:
            print("\033[1;31mOops! Plaase enter a valid number like 1,2,3 or 0 if u don't wanna buy it .\033[0m")
            
    total_cost += (price * amount_to_buy)
    print(f"\n\033[1;34mYour total is Rs. {total_cost}\033[0m")

if __name__ == '__main__':
    main()