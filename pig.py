import random
import os

player1Score = 0
player2Score = 0
turn = 1

def takeTurn():
    global player1Score
    global player2Score
    global turn
    roll = 'y'
    turnScore = 0
    while roll == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print('You rolled a:', die1, 'and:', die2 )
        if die1 == 1 and die2 == 1:
            print("You rolled a pair of 1s your turn is over")
            input("Press Enter to continue")
            roll = 'n'
            turnScore = -1
        elif die1 == 1 or die2 == 1:
            print("You rolled a 1 your turn is over")
            input("Press Enter to continue")
            roll = 'n'
            turnScore = 0
        else:
            turnScore = turnScore + die1 + die2
            print("Your score so far is:", turnScore)
            roll = input("Roll again? (y/n)").lower()
    if turn == 1:
        turn = 2
        if turnScore == -1:
            player1Score == 0
        else:
            player1Score = player1Score + turnScore
    elif turn == 2:
        turn = 1
        if turnScore == -1:
            player2Score == 0
        else:
            player2Score = player2Score + turnScore
    os.system('cls')

def gameTurns():
    global player1Score
    global player2Score
    global turn
    while player1Score < 100 and player2Score < 100:
        print("The current score is:")
        print("Player 1:", player1Score)
        print("Player 2:", player2Score)
        print("Player,", turn, "it is your turn")
        input("Press Enter to continue")
        takeTurn()
    if player1Score >= 100:
        print("Player 1 Wins!")
    elif player2Score >= 100:
        print("Player 1 Wins!")

def Screen():
    print("Pig")

def rules():
    print("This is the game of Pig")
    input("Press Enter to continue")

Screen()
r = input("Do you need to see the rules? y/n") n
if r == 'y':
    rules()
play = 'y'
while play == 'y':
    gameTurns()
    play = input("Do you want to play again? y/n")
print("Goodbye")

