def inList():                                                                                                                                                                                                    
    num = input("Enter input :   ").split()
    n = list(num)
    for i in n:
        if not i.isdigit():
            print('not no.')
            break
        else:
            print('all are number')
            r = list(map (int,input('Enter input again :  ').split()))
            oddNo = 0
            for i in r:
                if (i % 2) != 0:
                    oddNo += 1
            print('Total odd no in the list is:', oddNo)
            break
    for i in n:
        if i.isalpha():
            print('The largest string is:   ', max(n))
# for reversing the input string
            h = n[-1::-1]
            print("The reverse of input list is  ",h)
# to find if the entered element is present in the input string
            found=input('Enter the element:  ')
            def findEle():
                for i in num:
                    if i == found:
                        print('Element found')
                        break
            findEle()
# to remove an element from the input string
            def delEle():
                k = found
                str = []
                for i in num:
                    if i != k:
                        str.append(i)
                print ('Element',k,'" Deleted ')
# to print updated list
                print('Updated list',str)
            delEle()
            break
inList()
