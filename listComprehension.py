import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def newList():
    a = random.sample(range(100), 5) #This generates the Random number list
    b = random.sample(range(100), 5)
    result= [m for m,n in zip(a,b) if m == n]
    return result

print(newList())

#https://www.practicepython.org/solution/2014/04/16/10-list-overlap-comprehensions-solutions.html