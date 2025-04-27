
def average(a:float , b:float):
    
    """Returns the average of two numbers."""
    
    return (a + b) / 2

def main():
   avg1 = average(10,20)
   avg2 = average(40,50)
   final = average(avg1, avg2)
  
   print("\navg1: " ,  avg1) 
   print("\navg2: " ,  avg2) 
   print("\nfinal: " , final)


if __name__ == '__main__':
    main()