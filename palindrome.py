import numpy as np


def palindrome_hash(a):
    return hash(a) ^ hash(a[::-1]) 

N = 20

c = np.zeros(1<<N,dtype=object)
a=0

for s in open('words.dat'):
    s = s.rstrip()
    sp = s[::-1]
    if(s==sp): 
        print s,"==",s
        a+=1
    else:
        if(not isinstance(c[palindrome_hash(s)%(1<<N)],list)):
            c[palindrome_hash(s)%(1<<N)]=[]
        if(sp in c[palindrome_hash(s)%(1<<N)]):
            print s,"==",
            print sp
            a+=2
            c[palindrome_hash(s)%(1<<N)].remove(sp) 
        else:
            c[palindrome_hash(s)%(1<<N)].append(s) 

#print max(map(len,filter(lambda c:isinstance(c,list),c)))
print a
