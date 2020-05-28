#Import Date and TIme
import datetime
import sys



def characterInput():

#Get the Year
    year = datetime.date.today().year

    #Get the Name
    try:
        name = str(input("Enter your name: "))

        while not name:
            name = input("Enter your name: ")

    except ValueError:
        print ("Not in Correct format")
        sys.exit(1)

    #Get the age

    try:
        age = int(input ("Enter your age: "))

        while not name:
            name = input("Enter your age: ")

    except ValueError:
        print ("Not in Correct format")
        sys.exit(1)

    #Get the Years to Turn 100

    Hyears = 100 - int(age)

    #Add the year

    year += Hyears

    #Different print of the years

    return ("Hi %s, At year %s, you will turn to 100" %(name,year))


print(characterInput())