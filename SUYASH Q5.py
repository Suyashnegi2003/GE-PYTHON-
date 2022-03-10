def main():
    year=int(input('\nenter year to check it is leap year or not'))
    if (year%4)==0:
       if (year%100)==0:
          if (year%400)==0:
           print('*\nIT IS A LEAP YEAR*')
          else:
              print('*\nIT IA NOT A LEAP YEAR*')
       else:
          print('*\nIT IS NOT LEAP YEAR*')
    else:
        print('*\nIT IS NOT A LEAP YEAR*')
if __name__=='__main__':
    main()
