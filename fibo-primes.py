#Return an array with the first n numbers of Fibonachi serie and another array with the primes of this.
#Also return the time spended on the operation.

import time

def isDivThree(num):
    res = 0
    snum = str(num)
    for x in snum:
        res+=int(x)
    if res%3 == 0:
        return False

def isPrime(num):
    i = 2
    snum = str(num)
    if snum[-1] == 2 or snum[-1] == 4 or snum[-1] == 5 or snum[-1] == 6 or snum[-1] == 8 or snum[-1] == 0 and len(snum) > 1:    
        return False
    isDivThree(num)
    while i < num:
        if num%i == 0:
            return False
            break
        else:
            i+=1
    return True
    
t1 = time.time()
sfib = [0, 1]
primes = []
rep = int(input("nums: "))
for x in range(rep-2):
    sfib.append(sfib[x]+sfib[x+1])
    if isPrime(sfib[x]+sfib[x+1]):
        primes.append(sfib[x]+sfib[x+1])
print(sfib)
print(primes)
t2 = time.time()
print("mins: ",int(t2-t1)/60)