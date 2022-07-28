arr = [4, 7, 2, 1, 9, 5]

size = len(arr)
    
for x in range (0, size-1):

    for y in range (0, size-1):

        if (arr[y] > arr[y + 1]):

            temp = arr[x]

            arr[x] = arr[x + 1]
            arr[x + 1] = temp
  
print(arr)

for x in range (0, size-1):

    for y in range (0, size-1):

        if (arr[y] > arr[y + 1]):

            arr[x + 1], arr[x] = arr[x], arr[x + 1]  

print(arr)


def bubbleSort(arr): 

    n = len(arr) 

  

#SELECTION SORT PLEASE WORK

size = len(arr) 

for x in range(size): 

    for y in range(0, size-x-1): 

            if arr[y] > arr[y+1]: 

                arr[y], arr[y+1] = arr[y+1], arr[y]
    

print(arr)



size = len(arr) 

for x in range(size): 

    for y in range(0, size-x-1): 

            if arr[y] > arr[y+1]: 

                arr[y], arr[y+1] = arr[y+1], arr[y]





  



