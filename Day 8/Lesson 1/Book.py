from textwrap import fill


#make 1 class called book. books hould take in in __init__ self, title, author, price. two methods called
#read(self) buy(self). prints title and author of a book. buy returns the price. genre returns the genre

#subclass is mystery book. method genre(self)

#other subclass is picture book. method genre(self)

class Book(object):
    
    def __init__(self, title, author, price):

        self.title = title
        self.author = author
        self.price = price

    def read(self):

        print(self.title)
        print(self.author)

    def buy(self):

        return self.price

class MysteryBook(Book):

    def genre(self):

        return print("This book's genre is mystery")

class PictureBook(Book):

    def genre(self):

        return print("this book's genre is picture")

#subclass should take in a book and genre is just itself

testMysteryBook = MysteryBook('idk mystery books', "e", "$60.00")
#testMysteryBook.printInfo()

testPictureBook = PictureBook('flat stanley idk', "no idea", "$15.00")
#testPictureBook.printInfo()

testMysteryBook.genre()

testPictureBook.genre()


