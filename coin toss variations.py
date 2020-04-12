#print all configurations for n coin tosses [TINY 6]

def Recursion(List, Start, n):
    
    if n==0:
        print Start
        return
    
    for i in range (0,2):
        Next = Start + List[i]
        Recursion(List, Next, n-1)


List = ["H", "T"]
n = input("Input number of coin tosses: ")
Recursion(List, "", n)


print("\n"*3)

#using modules    
from itertools import product

P = product('HT', repeat=n)
for i in list(P):
    print i

