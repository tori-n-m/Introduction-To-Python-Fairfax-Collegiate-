x = 0
givenNumber = 4

for x in range(givenNumber <= x):

    x += 1
    result = givenNumber * x

print(result)

#idk what i'm doing :/
#2 hours of sleep :/
#fuck work :/

#why am i kinda traumatized from what happened two nights ago:/



#ACTUAL ANSWER

def factor(x, sum):

    if(x != 1):

        sum = sum * x

        factor(x - 1, sum)


#LINEAR SEARCH

#for loop and while loop 

def linearSearch():

    arr = [4, 7, 3, 5, 1]
    size = len(arr)

    #for x in range (0, size):

        #if (arr[x] > )

arr = [4, 7, 3, 5, 1]


def linearSearchWhile(arr, searchedVal):

    index = 0
    
    while(index < len(arr)):

        if (arr[index] == searchedVal):

            return (str(index))

        else:

            index += 1

    return ("number not in array")

linearSearch(arr, 3)
print(linearSearch(arr, 3))

#for loop way

arr = [4, 7, 3, 5, 1]

def linearSearchFor(arr, searchedVal):

    size = len(arr)

    index = 0

    for x in range(0, size):

        if (arr[index] == searchedVal):

            return (str(index))

        return

        

#while loop way

#recursive way