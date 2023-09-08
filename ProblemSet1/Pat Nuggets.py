sizes=[6,9,20]
buyable=[6, 9, 12, 15, 18, 20]
notbuyable=[]
streak=0

x=20
while streak<6:
    # print("While Loop Started")
    # print("On Number"+" "+str(x))
    isbuyable=False
    for b in buyable :
        if (x-6 == b) or (x-9 ==b) or (x-20==b):
            print(str(x)+" "+"is a buyable amount")
            isbuyable=True
    if isbuyable:
        buyable.append(x)
        streak=streak+1
        print("current streak is"+" "+str(streak))
    else:
        notbuyable.append(x)
        streak=0
    # if streak==6:
    #     break
    x+=1
    print(x)

    print(str(notbuyable[-1])+" "+"is the largest non-buyable number")





            