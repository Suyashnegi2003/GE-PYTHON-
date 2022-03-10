def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
            print(arr)
def main():
    arr=[]
    n=int(input('enter no. of elemenets:'))
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    print('final arr to use insertion sort is:',arr)
    insertion(arr)
    print('sorted sum is',arr)
if _name=='main_':
    main()
