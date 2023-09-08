def fibo(x):
    """This function returns a fibonacci number with the index of x"""
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return (fibo(x-1))+(fibo(x-2))
    
x=13
print("The "+str(x)+"th Fibonacci number is "+str(fibo(x)))