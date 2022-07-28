#def factor(x):

    #if x == 1:
        #return 1

def binarySearch(arr, searchVal):
    low = 0
    high = len(arr) - 1
    mid = 0

    #find a recursive method to check for a number

    while low <= high: 

        mid = (high + low) // 2

        if arr[mid] < searchVal:
            low = mid + 1

        
        elif arr[mid] > searchVal:
            high = mid - 1

        
        else:
            return mid

    return -1


arr = [ 2, 3, 4, 10, 40 ]
searchVal = 4

# Function call
result = binarySearch(arr, searchVal)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")



#


#HIS ANSWER ALSO IDK WHY BUT IT WAS WORKING WITH MY METHOD AND HE SAID IT WAS CORRECT BUT NOW ITS NOT
#SO IDK


def binarySearch(arr, target):

    high = len(arr) - 1
    low = 0

    while(high >= low):

        mid = int(low + high) // 2

        if(arr[mid == target]):

            return

        elif():

            high == mid - 1

        #else:






            


