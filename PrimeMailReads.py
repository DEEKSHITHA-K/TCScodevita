def SieveOfEratosthenes(n):
    primes = 0
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1):
        if prime[p]:
            #print (p,end=' ') 
            primes+=1
            # print(primes)
    return primes
# driver program
# if __name__=='__main__':

# print(SieveOfEratosthenes(10))
n = int(input())
count = 1
noOfPrimes = SieveOfEratosthenes(n)
noOfNonPrimes = n - noOfPrimes
while(noOfNonPrimes >= 2):
    temp = noOfNonPrimes
    noOfPrimes = SieveOfEratosthenes(temp)
    noOfNonPrimes = temp - noOfPrimes 
    count+=1
    
print(count+1)
