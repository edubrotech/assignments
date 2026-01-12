## bubble sort in array
def bubble_sort(arr):
    n=len(arr)
    print('list length',n)
    for i in range(n):
        print('I Number',i)
        for j in range(0,n-i-1):
            print('J Number',j)
            print(arr[j],'Number',arr[j+1])
            if arr[j]>arr[j+1]:
                #swap
                arr[j],arr[j+1]= arr[j+1],arr[j]
                print(arr[j],'reverse number',arr[j+1])
            print(arr,'J LOOPINN end')
        print(arr,'I LOOPINN end')



    return arr


arr=[5,1,4,2,8]
print(bubble_sort(arr));