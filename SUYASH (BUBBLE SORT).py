def bubbleSort(arr):
    for i in range (len(arr)-1,0,-1):
        for j in range(i):
            print(arr)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def main():
    arr=[]
    n=int(input('enter no. of elementes:'))
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    print('final array to use bubble sort is is:',arr)
    bubbleSort(arr)
    print('sorted sum is:',arr)
if _name=='main_':
    main()
