sizes=(6,9,20)
buyable=(6, 9, 12, 18, 20)
notbuyable=()
streak=0

while streak<6:
    print("While Loop Started")
    for x in range(20,70):
        print("On Number"+" "+str(x))
        isbuyable=False

        if (x-6==buyable[:]) or (x-9==buyable[:]) or (x-20==buyable[:]):
            buyable=buyable+(x, )
            print(str(x)+" "+"is a buyable amount")
        if isbuyable:
            streak=streak+1
            print("current streak is"+" "+str(streak))

        else:
            streak=0





            