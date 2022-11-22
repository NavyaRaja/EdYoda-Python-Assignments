def Fibonacci_Series(n):   
    
    if n < 0:  
        print("Oops! Incorrect input")  
  
    elif n == 0:   
        return ("Incorrect Input")   
   
    elif n == 1:  
        return (1)  
    else:  
        return (Fibonacci_Series(n - 1) + Fibonacci_Series(n - 2))   
print("nth Element of the Fibonacci Series:", Fibonacci_Series(0))  