# projecteuler.net/problem=2

# --- --- ---
a=1
b=1
s=0
while a<4000000:
    if a%2==0:
        s+=a  # summing up fibonacci terms.
    a,b=a+b,a  # generating fibonacci sequence
print(s)  # solution

# --- --- ---
