def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def main():
    n=int(input('enter a no.:'))
    print('factorial of a no. is:',fact(n))
if __name__=='__main__':
    main()
