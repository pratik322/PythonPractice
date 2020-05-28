def divisors():
    number = int(input("Enter the Number: "))
    listRange = list(range(1,number+1)) #This is amazing like how you can create the Range, I was doing range(2,100) in this if the user will give more than 100 the solution will fail that is why this is used which will give the range until the number is provided.
    my_list = []
    for a in listRange:
        if number % a ==0:
            my_list.append(a)
    return my_list

print(divisors())
