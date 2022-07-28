from platform import freedesktop_os_release


arr = [1, 3, 5, 7, 9]
size = len(arr)
if (size % 2 == 0):

    # // gives the divided value as an integer

    #checks for even

    temp = size // 2
    twmp1 = arr[temp] + arr[temp - 1] / 2

    print(temp1)

else: 

    #checks for odd
    
    temp = size // 2
    print(arr[temp])

#NEW ASSIGNMENT  

arr = [1, 8, -3, 17, -5]

#use for loops and if statements. find min and max value of an array. use 
#length method for finding array  

#FAILED ATTEMPT AT PROBLEM BELOW

#size = len(arr)

#for x in range (0, len(arr)):

    #if (arr[0] > arr[1]):

    #    arr[0]

    #else:

#ACTUAL ASNWER :/

arr = [0, 1, 2, 3]

size = len(arr)

max = arr[0]
min = arr[0]

for x in range (0, size):

    if (max < arr[x]):

        max = arr[x]

    if (min > arr[x]):

        max = arr[x]

#FINDING MEAN OF ARRAY

arr = [0, 1, 2, 3, 4]

size = len(arr)
meanval1 = 0

for x in range (0, size):

    meanval1 += arr[x]

mean = meanval1 / len(arr)

print(mean)













