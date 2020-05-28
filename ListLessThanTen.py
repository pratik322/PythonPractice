#Challenge 1 -

""""
def listlessthanTEN():
    my_list = []
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for a in list1:
        if a < 5:
            my_list.append(a)
    return my_list



print(listlessthanTEN())
"""
#Challenge 2 - Write in one line
#list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
''''

print([v for v in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if v < 5])



'''

#Challenge 3 '

def myNumber():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_list = []
    my_number = int(input("Enter the Number: "))
    for w in a:
        if w < my_number:
            new_list.append(w)
    return new_list

print(myNumber())