def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

def main():
    print(in_range(5, 1, 10))  # True
    print(in_range(0, 1, 10))  # False


if __name__ == "__main__":  
    main()    
