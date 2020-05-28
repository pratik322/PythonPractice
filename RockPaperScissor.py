def rockPaperScissor():
    player1_input = str(input("Enter your Choice Player1: "))
    while not player1_input:
        player1_input = str(input("Enter your Choice again Player1: "))



    player2_input = str(input("Enter your Choice Player2: "))
    while not player2_input:
        player1_input = str(input("Enter your Choice again Player2: "))

    if player1_input.lower() == "rock" and player2_input.lower() == "scissors":
        print ("Player 1 wins...")
        wantToContinue()
    elif player1_input.lower() == "rock" and player2_input.lower() == "paper":
        return ("Player 2 wins...")
    elif player1_input.lower() == "scissors" and player2_input.lower() == "paper":
        return ("Player 1 wins...")
    elif player1_input.lower() == "scissors" and player2_input.lower() == "rock":
        return ("Player 2 wins...")
    elif player1_input.lower() == "paper" and player2_input.lower() == "rock":
        return ("Player 1 wins...")
    elif player1_input.lower() == "paper" and player2_input.lower() == "scissors":
        return ("Player 2 wins...")
    else:
        return ("TIE...")

def wantToContinue():
    cont = input('Type "yes" to continue: ' )
    while cont != "yes":
        quit = input('Type "yes" to continue: ' )
    rockPaperScissor()


print(rockPaperScissor())