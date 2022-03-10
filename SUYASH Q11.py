def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True
    return prime(n)
def main():
    n=int(input('enter no.:'))
    result=prime(n)
    if result==True:
        print(n,'is a prime no.')
    else:
        print(n,'is not a prime no.')
if __name__=='__main__':
    main()
