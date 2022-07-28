#BINARY TREE

#everything right is greater tgan root node, everything left is less than for sortted binary
#trees. unsorted are not this way

#I did this wrong but whatever :/ it works 

class Node():

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


    

#     def PrintTree(self):
#         print(self.val)

# root = Node(10)
# root.PrintTree()

#create binary tree class inserting method

#class BinaryTree:

    #constructor
    #def __init__(self, val):

    def insert(self, val): #FIRST THINGA DOING IN INSERT. checking if value is none, if none set equal
        #if self.val = none. if none do else. if not none say is num >. if it is, self rightnone. else self.
        #right insert

        if (self == None):

            self = Node(val)

        #if (num < self.val):

        elif (val < self.val):

            if (self.left == None):

                    self.left = Node(val)

            else:

                self.left.insert(val)   

        elif (val > self.val):

            if (self.right == None):

                self.right = Node(val)

            else: 

                self.right.insert(val)


    def printTree(self):

            if (self.left):

                self.left.printTree()

            print(self.val)

            if (self.right):

                self.right.printTree()




#INSERTING NODES

root = Node(12)

root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()



        

        #if ()




        # if (== None):

        #     val == num
        
        # if (self.val == None):

        # elif ()




        # if (self == None):

        #     if self(val > num):

        #         #self.left != None
        #         self.left.insert(num)

        #     else:

        #         self.left.insert(num)

        #     elif self(val < num):



    #insert(self(num))

    #if self.(null)

    #if self(val  > num)

        #self.left != null

        #self.left.insert(num)

#root = tree(8). Now we have root is 8, left is none and right is none

#root = BinaryTree()