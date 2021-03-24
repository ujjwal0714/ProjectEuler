# projecteuler.net/problem=10
# --- --- ---
import time
t=time.time

# --- --- ---
def SieveOfEratosthenes(n):
    prime=[True for i in range(n + 1)] 
    p=2; l=[]
    while (p*p<=n): 
        if (prime[p]==True):
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1): 
        if prime[p]: 
            l.append(p)
    return(l)

# --- --- ---
t1=t()
r=sum(SieveOfEratosthenes(2000000))
t2=t()
print("result: ",r)  # solution
print("time taken in execution: ",t2-t1)

# --- --- ---
