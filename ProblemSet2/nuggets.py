#If you find 6 in a row, you can find the next one by adding six to the first one. 
# and the one after that by adding 6 to the second, etc. 
# Knowing that, you can extrapolate, once you find 6 in a row (or whatever the smallest number is)


sizes=[6,9,20]
buyable=[6, 9, 12, 15, 18, 20]
notbuyable=[]
streak=0

x=20
while streak<6:
    isbuyable=False
    for b in buyable :
        if (x-6 == b) or (x-9 ==b) or (x-20==b):
            isbuyable=True
    if isbuyable:
        buyable.append(x)
        streak=streak+1
    else:
        notbuyable.append(x)
        streak=0
    x+=1
   
print(str(notbuyable[-1])+" "+"is the largest non-buyable number")





            