
def onetohundred(n,dist):
    if n <= dist:
        print('Serial is = ',n)
        onetohundred(n+1,dist)
   else:
        print('Successful')

onetohundred(1,100)     