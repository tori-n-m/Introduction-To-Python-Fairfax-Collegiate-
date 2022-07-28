from textwrap import fill


class Dog(object):

    def __init__(self, fill, name, gender, age):

        self.fill = fill
        self.name = name
        self.gender = gender
        self.age = age

    def printInfo(self):

        print("this doggo is: ")

class Corgi(Dog):

    def __init__(self, fill, name, gender, age):

        self.fill = fill
        self.name = name
        self.gender = gender
        self.age = age
       

    def corgiBark(self):

        self.bark = "borkbork!"
        print(self.bark)

testCorgi = Corgi('pink', "Corndog", "Male", 6)
testCorgi.printInfo()

(testCorgi.corgiBark())

class Husky(Dog):

    def __init__(self, fill, name, gender, age):

        self.fill = fill
        self.name = name
        self.gender = gender
        self.age = age

    def huskyBark(self):

        self.bark = "WOOOOOOOOOOOOOOUUUUGH!"
        print(self.bark)

testHusky = Husky('pink', "Corndog", "Male", 6)
testHusky.printInfo()

(testHusky.huskyBark())


class Chihuahua(Dog):

    def __init__(self, fill, name, gender, age):

        self.fill = fill
        self.name = name
        self.gender = gender
        self.age = age
        

    def chihuahuaBark(self):

        self.bark = "*Demonic screeches*"
        print(self.bark)

testChihuahua = Chihuahua('pink', "Corndog", "Male", 6)
testChihuahua.printInfo()

(testChihuahua.chihuahuaBark())

class Capybara(Dog):

    def __init__(self, fill, name, gender, age):

        self.fill = fill
        self.name = name
        self.gender = gender
        self.age = age
        

    def capybaraBark(self):

        self.bark = "*silence*"
        print(self.bark)

testCapybara = Capybara('pink', "Corndog", "Male", 6)
testCapybara.printInfo()

(testCapybara.capybaraBark())



