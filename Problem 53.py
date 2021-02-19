# Problem 53

import math
m=math.factorial

def nCr(n,r):
   return(m(n)//(m(r)*m(n-r)))
   
million=10**6
count=0
for i in range(1,101):
   x=0
   while x!=i:
      if nCr(i,x)>million:
         count+=1
      x+=1

print(count)  # solution

