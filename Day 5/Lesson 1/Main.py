arr = [3, 8, 9, 7]

size = len(arr)
    
for x in range (0, size-1):

    arr[x + 1], arr[x] = arr[x], arr[x + 1]  

print(arr)




arr = [6,8,4,5,2,9]

def bubbleSort(arr):

    size = len(arr)

    for x in range (0,size):

        for y in range (0, size - x - 1):


                    temp = arr[y]
                    arr[y] = arr[y+1]
                    arr[y+1] = temp
                    

    return(arr)

bubbleSort(arr)
print(arr)



def selectionSort(arr):

    size = len(arr)

    for x in range (0,size):

        for y in range (0, size + x / size):

            if(arr[x] > arr[x + 1]):

                    temp = arr[y]
                    arr[y] = arr[y+1]
                    arr[y+1] = temp

    return(arr)

print(arr)

#SELECTION SORT ACTUAL ANSWER

def selectionSort(arr):

    size = len(arr)

    for x in range(0, size -1):

        #finds the minimum
        min = arr[x]
        index = 0

        for y in range (0 + x, size):

            if(min > arr[y]):

                min = arr[y]
                index = y

        temp = arr[x]      

        arr[x] = min

        arr[index] = temp  





