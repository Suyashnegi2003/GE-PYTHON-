def selectSort(arr):
    for i in range(len(arr)):
        print(arr)
        minValue=min(arr[i:])
        minInd=arr.index(minValue)
        arr[i],arr[minInd]=arr[minInd],arr[i]
def main():
    arr=[]
    n=int(input('enter no. of elements:'))
    for i in range (n):
        ele=int(input())
        arr.append(ele)
    print('final arr to use selection sort is:',arr)
    selectSort(arr)
    print('sorted sum is:',arr)
if _name=='main_':
    main()
