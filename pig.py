import random
import sys
	
import argparse
 
 
parser = argparse.ArgumentParser()
 
parser.add_argument( "--numPlayers", help = "Number of Players")
 
args = parser.parse_args()
 
num_of_players = args.numPlayers

class MainGame():
    def __init__(self, player1, player2, die):
        self.turn_score = 0
        self.die = Die()
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player2.name = "Player 2"
        self.player1.name = "Player 1"

        pig_roll = random.randint(1, 2)
        if pig_roll == 1:
            self.current_player = self.player1
            print('Player 1 will start the game')
        elif pig_roll == 2:
            self.current_player = self.player2
            print('Player 2 will start the game')
        self.turn()

    def another_turn(self):
        self.turn_score = 0
        if self.player1.score >= 100:
            print('Player 1 won the game with score:', self.player1.score)
            self.finish_game()
            game_start()
        elif self.player2.score >= 100:
            print('Player 2 won the game with score:', self.player2.score)
            self.finish_game()
            game_start()
        else:
            if self.current_player == self.player1:
                self.current_player = self.player2
            elif self.current_player == self.player2:
                self.current_player = self.player1
            print('Next turn, Current player : ', self.current_player.name)
            self.turn()

    def turn(self):
        self.die.roll()
        if (self.die.value == 1):
            print('You Rolled a 1! No points added, your turn is over.')
            print('Player 1 Score:', self.player1.score)
            print('Player 2 Score:', self.player2.score)
            self.turn_score = 0
            self.another_turn()
        else:
            self.turn_score = self.turn_score + self.die.value
            print('You rolled a:', self.die.value)
            print('Current Value is:', self.turn_score)
            print('Player 1 Score:', self.player1.score)
            print('Player 2 Score:', self.player2.score)
            self.current_player.decide()
            if (self.current_player.hold == True and self.current_player.roll == False):
                self.current_player.score = self.current_player.score + self.turn_score
                self.another_turn()
            elif (self.current_player.hold == False and self.current_player.roll == True):
                self.turn()

    def finish_game(self):
        self.player1 = None
        self.player2 = None
        self.die = None
        self.turn_score = None

class Die():
    def __init__(self):
        self.value = int()
        seed = 0

    def roll(self):
        self.value = random.randint(1, 6)

class Player():
    def __init__(self):
        self.turn = False
        self.hold = False
        self.roll = True
        self.score = 0
        self.name = None

    def decide(self):
        decision = input('Type H for Hold and R for Roll: ')
        if decision.upper() == 'R':
            self.hold = False
            self.roll = True
        elif decision.upper() == 'H':
            self.hold = True
            self.roll = False
        else:
            print('Invalid input!')
            self.decide()




MainGame(Player(), Player(), Die())
