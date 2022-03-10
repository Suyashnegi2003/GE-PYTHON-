def main():
    ch=int(input('Enter 1-length , 2=max of 3 strings,3=to print , 4=number of words='))
    if ch==1:
        n=input('Enter a string:')
        l=len(n)
        print('The length of the string is=',l)
    elif ch==2:
        n1=input('Enter string 1=')
        n2=input('Enter string 2=')
        n3=input('Enter string 3=')
        print('The maximum of the 3 strings is=',max(n1,n2,n3))
    elif ch==3:
        a=input('Enter a string:')
        s=''
        a=list(a)
        for i in range(len(a)):
            if (i%2!=0):
                if a[i]==' ':
                    a[i]=' '
                else:
                    a[i]='#'
        for e in a:
            s=s+e
        print('the new string=',s)    
    elif ch==4:
         b=input('Enter a string=')
         c=0
        for ch in b:
            if ch==' ':
                c+=1
        a=c+1
        print('The number of words:',a)
    else:
        print('invalid choice') 
if __name__=='__main__':
    main()
