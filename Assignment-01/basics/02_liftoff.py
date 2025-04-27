import time

def main():
    for i in range(10, 0, -1):
        print(i , end = " " ,flush = True)
        time.sleep(1)
    print("Liftoff!")
        
if __name__ == "__main__":
    main()          