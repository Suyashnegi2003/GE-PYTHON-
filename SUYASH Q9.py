def main():
    n = int(input("Enter a positive integer:"))
    r, s =0, 0
    while(n>0):
        rem = n % 10
        r = (r*10) + rem
        n = n//10
    print('Reverse of a number =', r)
    while (r>0) :
        a = r % 10
        s+=a
        r=r//10
    print('Sum of the reversed number =',s)
if __name__=='__main__':
    main()
