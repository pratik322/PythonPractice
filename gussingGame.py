import random
'''
def guess():
    while True:
        random_number = random.randint(1,9)
        u1 = input("Guess the Number: ")
        if int(u1) < random_number:
            return("You guessed too low...")
            continue
        elif int(u1) > random_number:
            return("You guessed too High...")
            continue
        elif int(u1) == random_number:
            return("You guessed it Correct...")
            continue
        elif u1 == "exit":
            break

print(guess())
'''
a = 0
while True:
    random_number = random.randint(1,9)
    u1 = input("Guess the Number: ")
    if u1 == "exit":
        break
    if int(u1) < random_number:
            print("You guessed too low...")
            a = a+1
            continue
    elif int(u1) > random_number:
        print("You guessed too High...")
        a = a+1
        continue
    elif int(u1) == random_number:
        print("You guessed it Correct...")
        a = a+1
        continue
print("You have taken %s number of guess" %a)