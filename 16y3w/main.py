# -*- coding:utf-8 -*-
"""
2016.1.10

self is a alias of the real object

"""

class Book:
    x = 0
    name = ""
    
    def __init__(self,name): # common
        self.name = name

    def readtimes(self): 
        self.x = self.x + 1
        print "%s was read %s times." %(self.name, self.x)
    
    #def __del__(self): # seldom used
    #    print "I'm deleted...", self.x


class PyBook(Book): #inheritance
    times = 0
    

    def borrowtimes(self, borrower):
        self.readtimes()
        self.times = self.times + 1

        print "%s was borrowed %s times by %s." %(self.name, self.times, borrower)




a = Book("complexity")
a.name
a.readtimes()

b = PyBook("Core of Python")
b.name
b.borrowtimes("Sally")
b.borrowtimes("Sabie")




#print dir(complexity) # show the operations that the object can perform


#y = "hello world"

#print dir(y)
#print y.split()




