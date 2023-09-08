def recurse (target, key):
    test=key.find(target)
    if test==-1:
        return
    else:
        #count+=1
        return recurse(target[(test+1):], key)

x="atgc"
y="atgacatgcacaagtatgcat"
count=0
recurse("atgc", "atgacatgcacaagtatgcat")
print("atgc appears in atgacatgcacaagtatgcat " +str(count)+ "times")
#print(key.find(target))
