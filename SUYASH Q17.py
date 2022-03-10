
def check_duplicate(l):
    l2={}
    for i in l:
        if i in l2:
            l2[i]+=l
        else:
            l2[i]=l
        for i in l:
            if l2[i]>l:
                print('True',i,l2[i])
def main():
    n=int(input('enter no. of elements:'))
    l=[]
    for i in range(n):
        ele=int(input())
        l.append(ele)
print('original list',l)
check_duplicate
if __name__=='__main__':
    main()
