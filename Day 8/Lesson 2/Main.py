#two classes node class and linked list class

#null value in linked list means link list has ended

#FIRST focus on constructors. SECOND work on node class

#NODE CLASS: we have a node. node is something that holds a value. ALSO holds a pointer. points to
#the next value. first node of a linked list is the head. NEXT VALUE is set/equal to null/none. STEP
# ONE:Should be Able to take in a value. STEP TWO the next value to null.

#LINKED LIST CLASS. head automatically set to null because no null. if add a new variable. linked list has
#a collection of nodes. SET HEAD = NONE. self.head = none 

#L1 = LINKEDlIST(). an empty head is created. SET THE HEAD- L1.head = node(8). 8 POINTS TO NULL
#L1.head.nextValue = Node(7). 

#LINKED LIST IS ONLY CREATING THE HEAD, NODE HAS THE VALUE IS POINT. ALL HEAD CONSTRUCTORS IN LINKED 
#LIST SHOULD BE NONE

#initial value should be equal to 10

#

class Node(object): #node class should be setting the value of what the node is and setting the pointer
    #initializing next node as null

    def __init__ (self, val = None):

        self.val = val
        self.nextVal = None

        #next node should be here. next node is equal to the null value

        #next keyword is important

    #def idkWhatImDoing(self):

        #self.val = val
        #self.nextVal = nextVal
        #val = 7 #VALUES
        #extVal = None #POINTER

class LinkedList(object):

    #method at beginnning in linked list taking it itself taking in number method should be taking in new node
    #and setting that number in the head. 7 should be the new head and 10 should be the new value

    def iStillDontKnowWhatImDoing(self):

        nextVal = self.head
        self.head = None


    def __init__(self):

        self.head = None

    def printLinkedList(self):

        printHeadVal = self.head
        
        #WHILE VAL != NULL
        while (printHeadVal != None):

            print(printHeadVal.val)
            printHeadVal = printHeadVal.nextVal

L1 = LinkedList()

L1.head = Node(8)

L1.head.nextVal = Node(7)




#???L1.head.nextValue = Node(7)

L1.printLinkedList()









    
