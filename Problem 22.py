# projecteuler.com: Problem 22

# --- --- ---
# accesing data from text file.
import csv

file=open("names.txt")  # file address: https://projecteuler.net/project/resources/p022_names.txt
f=csv.reader(file)

for i in f:
    l=i  # l is the list of names.

# --- --- ---
# sorting of l
m=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
n=[i.upper() for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

for i in l:
    v1=n.index(i[0])
    m[v1].append(i)

o=[]
for i in m:
    i.sort()
    o.append(i)

p=[]
for i in o:
    for j in i:
        p.append(j)  # p is the sorted list.

l=p

# --- --- ---
# problem solving.
def name_score(x):
    s=0
    for i in x:
        s+=n.index(i)+1
    return((l.index(x)+1)*s)

summ=0
for i in l:
    summ+=name_score(i)

print(summ)  # solution.

# --- --- ---
