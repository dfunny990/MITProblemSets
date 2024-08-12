
import math

def power(a, b) :
    return a**b


if __name__ == '__main__':
    x = int(input("Please enter a value for x:"))

    y = int(input("Please enter a value for y:"))
    xy = power(x,y)
    

    print ("x**y = " + str(xy))
    print ("log(x) = "+ str(math.log2(x)))

