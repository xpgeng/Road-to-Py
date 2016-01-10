# -*- coding:utf-8 -*-
"""
2016.1.10

self is a alias of the real object

"""

class Book:
    x = 0
    
    def __init__(self):
        print "I'm a book."

    def readtimes(self): 
        self.x = self.x + 1
        print "This book was read %s times." %self.x 


complexity = Book()
complexity.readtimes()
complexity.readtimes()
complexity.readtimes()
print complexity.x
print dir(complexity) # show the operations that the object can perform


y = "hello world"

#print dir(y)
print y.split()




