#Defination 

def getNumber(helpText = "Get the Number"):
    return int(input(helpText))


def primenumber():
    result = getNumber("Enter any number: ")
    number_range = list(range(2,result))
    count = 0
    for i in number_range:
        if result % i == 0:
            count = count + 1
    if count == 0:
        return("The Number is Prime")
    else:
        return("The Number is NOT Prime")

print(primenumber())