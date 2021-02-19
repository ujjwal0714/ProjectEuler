# Problem 99

import csv,math

file=open("readme.txt")  # file address: https://projecteuler.net/project/resources/p099_base_exp.txt 
read=csv.reader(file)

l=[]
v=[l.append(i) for i in read]  # makes l a list of elements obtained from file.

# used concept: if a^b>c^d, then b*log(a)>c*log(d).
m=[]
for i in range(len(l)):
    a,b=int(l[i][0]),int(l[i][1])
    p=b*math.log(a)
    m.append(p)
    
solution=m.index(max(m))+1  # line number is to be returned
print(solution)

