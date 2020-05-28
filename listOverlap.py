'''
def listOverlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for m,n in zip(a,b):
        if m == n:
            c.append(m)
    return c

print(listOverlap())

'''
#Writing the same code in one line
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([m for m,n in zip(a,b) if m == n])
'''
#Randomly generate the List:
#a = list(range(1,30))
# b = list(range(1,40))
def listOverlap():
   b = [1,3,3,3,3,3,3,3,3,3,3,3]
   a = [1, 2, 3, 4, 5, 6, 7, 8, 21]
   c = []
   for m,n in zip(a,b):
       if m == n:
           c.append(m)
   return c

print(listOverlap())
