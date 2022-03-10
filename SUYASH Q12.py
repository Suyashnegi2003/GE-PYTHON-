def main():
    a=input('enter a string:')
    b=a[-1::-1]
    if(a==b):
        print('palindrome string')
    else:
        print('not palindrome')
if __name__=='__main__':
    main()
