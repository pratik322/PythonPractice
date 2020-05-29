def fibonacciSeries():
    new_list = []
    user_input = int(input("Enter the Number: "))
    new_list.append(1)
    new_list.append(1)
    #number_list = list(range(0, user_input + 2))
    #print(number_list)
    for i in range(0, user_input):
        new_list.append(new_list[i]+ new_list[i+1])

    return new_list

print(fibonacciSeries())

