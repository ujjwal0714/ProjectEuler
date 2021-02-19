# Problem 48

s=0  # sum of the powers.
for i in range(1,1001):
   s+=i**i
s=str(s)

solution=int(s[len(s)-10:len(s)])  # retrieving last ten digits of s.
print(solution)

