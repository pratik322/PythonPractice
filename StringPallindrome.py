def Pallindrome():
    input_string = str(input("Enter the String: "))
    if input_string.lower()[:] == input_string.lower()[::-1]:
        return ("The String is Pallindrome")
    else:
        return ("The String is NOT Pallindrome")


print(Pallindrome())
