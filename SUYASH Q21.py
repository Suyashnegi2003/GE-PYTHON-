def binarySearchAppr (arr,start, end, x):
    if end >= start:
        mid =start + (end- start)//2
    # If element is present at the middle
        if arr[mid] == x:
            return mid
   # If element is smaller than mid
        elif arr[mid] > x:
            return binarySearchAppr(arr, start, mid-1, x)
   # Else the element greator than mid
        else:
            return binarySearchAppr(arr, mid+1, end, x)
    else:
   # Element is not found in the array
      return -1
arr = [2,3,4,10,40]
x =10
result = binarySearchAppr(arr, 0, len(arr)-1, x)
if result != -1:
   print ("Element is present at index "+str(result))
else:
    print ("Element is not present in array")

#LINEAR SEARCH
                            
def search(arr,x):    
    for i in range(len(arr)):
        if arr[i]==x:
            return i        
         return -1
def main():
    n=int(input('enter no. of elements to be inserted:'))
    arr=[]
    for i in range(n):
        ele=int(input('enter elements:'))
        arr.append(ele)
    print(arr)
    x=int(input('enter value to be searched:'))
    result=search(arr,x)
    print(x,'found at index',result)
if __name__=='__main__':
    main()
