def listends():
    result = []
    number_list = list(input("Enter the Numbers: "))
    result.append(number_list[0])
    result.append(number_list[-1])
    return result

print(listends())


########

def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]