
def sum(a , b) :
    return a+b

print("The Result is = ", sum (12,79))

#function define

def scalesanimals() :
 print("Lizard")
scalesanimals()

#function with parameter

def feathersanimals(name) : 
    print(name)

feathersanimals("peacock")
feathersanimals("parrot")
feathersanimals("Ostrich")


def myname(fname,lastname):
  print(fname + " " + lastname)  

myname("Sharjina","Afrin")

#function with parameter one or more

def moreparameter(*fishname):
 print(fishname[3]) 
moreparameter("hilsha","salmon","Tuna","Catfish","Goldie")

#for loop in function

def my_function(fruits):
  for i in fruits:
    print(i)

    
fruits = ["apple", "banana", "cherry"]

my_function(fruits)