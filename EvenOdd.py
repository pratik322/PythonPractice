def evenOdd():
    num = int(input("Enter the Number: "))
    check = int(input("Enter the Another Number: "))
    if num % 4 == 0:
        return("%s is divisible by 4" %(num))
    if num % check ==0:
        return("%s is divisible by %s" %(num,check))
    else:
        return("%s is not divisible either by 4 and %s" %(num,check))

print(evenOdd())