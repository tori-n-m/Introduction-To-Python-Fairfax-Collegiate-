arr = [3, 7, 2, 10]
arrTwo = [2, 1, 9, 6, 7]

size1 = len(arr)
size2 = len(arrTwo)

#combo = arr1, arrTwo1

mode = 0
modeFreq = 0

for x in range (0, size1):
    freq = 0 

    for y in range (0, size2):

        if (arr[y] == arr[x]):

            freq += 1

        if (modeFreq <= freq):

            mode = arr[x]
            modeFreq = freq

print(mode)

arr1[1, 2, 3, 4, 5, 6, 7]
arr2 = [5, 6, 7, 8, 9, 10]
arr3 = []

size = len(arr1)
size2 = len(arr2)

for x in range (0, size1):

    for y in range (0, size2):

        if(arr1[x] == arr2[y]):
            arr3.append(arr1[x])
        print(arr3)




