
#val1 = arr[0] + arr[1] + arr [2] + arr[3] + arr[4]
#val2 = arr[5] +arr[6] + arr[7] + arr[8]
#val3 = arr[9] + arr[10] + arr[11] + arr[12] + arr[13] + arr[14] + arr[15]

#median = (val1 + val2 + val3) / 15

def findMedian(a, n):
 
    
    sorted(a)
 
    
    if n % 2 != 0:
        return float(a[n // 2])
     
    return float((a[int((n-1)/2)] +
                  a[int(n / 2)])/2.0)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
 
n = len(a)
print("Median =", findMedian(a, n))

#MODE

arr = [0, 1, 2, 2, 3, 4]

size = len(arr)
modeFreq = 0
freq = 0
for x in range (0, size):
    mode = 0
    for y in range (0, size):
        #check if the values are congruent
        if (arr[x] == arr[y]):
            freq = freq +1
    #updates mode freq

    if(freq > 0):
        #freq = arr[x]
        modeFreq += 1

    if (freq == modeFreq):

        freq = arr[x]

    


print("Mode = ", mode)

ar = [1, 2, 2, 3, 4]

size = len(arr)
mode = 0
modeFreq = 0

#FINDING MODE ACTUAL ANSWER

for x in range (0, size):
    freq = 0 

    for y in range (0, size):

        if (arr[y] == arr[x]):

            freq += 1

        if (modeFreq <= freq):

            mode = arr[x]
            modeFreq = freq

print(mode)








