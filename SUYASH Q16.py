t1=(1,2,3,4,5,6,7,8,9,10)
t1a=t1[:5]
t1b=t1[5:]
print(t1a)
print(t1b)
print()

#(B)
                            
t1=(1,2,3,4,5,6,7,8,9,10)
n=list(t1)
list1=list()
for i in n:
    if i in n:
        if i%2==0:
            list1.append(i)
    p=tuple(list1)
print('tuple:',p)
print()

#(C)
                            
t1=(1,2,3,4,5,6,7,8,9,10)
t2=(11,13,15)
a=list(t1)
b=list(t2)
c=(a+b)
print(c)

#(D)
                            
t1=(1,2,3,4,5,6,7,8,9,10)
max(t1)
min(t2)
print('max no. is',max(t1))
print('min no. is',min(t1))
