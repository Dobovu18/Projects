"""
Simulating who wins a game of Racquet ball between two opponents
Players' skill is represented by probabilities, which is the likelihood they win a rally.
"""

from random import *

class Player():
    """
    A racquet ball player has:
        --A Name
        --A Skill level (probability of winning from serve)
        --An Associated rally score
        --Number of games won
    """
    def __init__(self, name):
        self.name = name
        self.skill = 0.0
        self.score = 0 #This is the number of rallies won (in a game)
        self.wins = 0 #This is the number of games won
    
    #Setters:

    def setName(self, name): self.name = name
    
    def setSkill(self, skill):
        #Skill must be between 0 and 100
        if(skill >= 0.0 and skill <= 100.0):
            self.skill = skill
    
    def addScore(self):
        self.score += 1
    
    def addWin(self):
        self.wins += 1

    def resetScore(self):
        self.score = 0

    def resetWins(self):
        self.wins = 0

    #Getters:

    def getName(self): return self.name
    
    def getSkill(self): return self.skill

    def getScore(self): return self.score

    def getWins(self): return self.wins

def main():
    introText() #Prints out the instruction and introduction to the program
    n, plyr1, plyr2 = getInputs() #Get inputs recieves all information needed for simulation
    simulateGames(n, plyr1, plyr2) #simulates n games between players 1 and 2
    display(plyr1, plyr2) 

def introText():
    #Provides instructions and information on using the program
    print("""
    Welcome to the Racquetball simulator.
    
    This program takes two racquetball players and simulates a number
    of games of them playing against each other.

    Each player's skill level affects how likely they are to win.
    The player's skill level is the change (as a percentage) that they 
    win a rally where they are serving.
    """)

def getInputs():
    name1, name2 = input("Please input the names of the two players, seperated by a comma: ").split(",")
    player1, player2 = Player(name1), Player(name2)
    skill1, skill2 = eval(input("Please input %s's and %s's skill levels respectively (a score out of 100): " %(player1.getName(), player2.getName())))
    player1.setSkill(skill1)
    player2.setSkill(skill2)
    numberOfGames = int(eval(input("Enter the number of games you want simulated: ")))
    return numberOfGames, player1, player2

def simulateGames(numberOfGames, player1, player2):
    for i in range(numberOfGames):
        score1, score2 = simulate(player1, player2) #simulating n games is the same as simulating 1 game n times
        if score1 < score2: player2.addWin() #Player with most score wins the game
        elif score2 < score1: player1.addWin()
    return player1.getWins(), player2.getWins()

def simulate(player1, player2):
    
    numberOfRallies = 15 #Number of rallies per game
    player1.resetScore() #Player (rally) scores must reset when a new game begins
    player2.resetScore()
    plyrServing = player1
    if random() < 0.5: plyrServing = player2 #Randomly choosing a player to serve
    while gameOn(player1, player2):
        #Skill level is the likelihood the player wins the rally they serve for
        if (plyrServing.getSkill() / 100) > random():
            plyrServing.addScore()
        else: #If player loses, servers are swapped.
            if plyrServing == player1: plyrServing = player2
            else: plyrServing = player1
    return player1.getScore(), player2.getScore()

def gameOn(player1, player2):
    #A game finishes when a player reaches a score of 15
    if player1.getScore() == 15 or player2.getScore() == 15: return False
    else: return True

def display(player1, player2):
    print("""
    %s wins: %d
    %s wins: %d
    """ %(player1.getName(), player1.getWins(), player2.getName(), player2.getWins()))

main()

"""
Possible further/related projects:
    --Racquetball tournament simulator:
        >Takes n, the number of rounds, and 2^n players and their skill levels
        >Outputs the winners of each stage of the tournament
    --Other sports simulators:
        >E.g Tennis, football, boxing
"""