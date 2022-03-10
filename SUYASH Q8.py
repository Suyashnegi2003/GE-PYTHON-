def main():
  n=int(input('enter no.:'))
  x=0
  y=1
  z=0
  while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
if __name__=='__main__':
    main()
