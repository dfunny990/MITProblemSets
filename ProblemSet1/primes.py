primes = [2,3]
current = 5
count = 2
while count < 1000:
    isPrime = True
    for p in primes:
        if current % p == 0:
            isPrime = False 
            #Ideally you would skip out of the loo pat this point, but I don't know a lot of python, so......?
    if isPrime:
        primes.append(current)
        count+=1
    current += 2
print (primes[len(primes)-1])
