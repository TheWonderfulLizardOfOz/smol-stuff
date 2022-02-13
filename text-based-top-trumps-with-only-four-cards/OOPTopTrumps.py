import random

class Card():
    def __init__(self, cardName, attack, defense):
        self.cardName = cardName
        self.attack = attack
        self.defense = defense

    def outputCard(self):
        print("Card Name: {}\nAttack: {}\nDefense: {}\n".format(self.cardName, self.attack, self.defense))

class Game():
    def __init__(self, cardList):
        self.cardList = cardList
        self.computerCards = []
        self.playerCards = []
        self.drawPile = []

    def dealCards(self):
        random.shuffle(self.cardList)
        for i in range(len(self.cardList)):
            if i % 2 == 0:
                self.playerCards.append(self.cardList[i])
            else:
                self.computerCards.append(self.cardList[i])

    def compareCards(self, stat, computerCard, playerCard):
        if stat == "Attack":
            computerValue = computerCard.attack
            playerValue = playerCard.attack
        else:
            computerValue = computerCard.defense
            playerValue = computerCard.defense

        print("Your {}: {}\nComputer {}: {}".format(stat, playerValue, stat, computerValue))
        if playerValue > computerValue:
            print("You win round")
            self.playerWin(computerCard)
            return "player"
        elif computerValue > playerValue:
            print("Computer wins round")
            self.computerWin(playerCard)
            return "computer"
        else:
            print("This round was a draw")
            self.draw(computerCard, playerCard)
            return None

    def playerWin(self, computerCard):
        self.playerCards.append(self.playerCards.pop(0))
        self.playerCards.append(computerCard)
        self.computerCards.pop(0)
        for card in self.drawPile:
            self.playerCards.append(card)
        for i in range(len(self.drawPile)):
            self.drawPile.pop(0)

    def computerWin(self, playerCard):
        self.computerCards.append(self.computerCards.pop(0))
        self.computerCards.append(playerCard)
        self.playerCards.pop(0)
        for card in self.drawPile:
            self.computerCards.append(card)
        for i in range(len(self.drawPile)):
            self.drawPile.pop(0)

    def draw(self, computerCard, playerCard):
        self.computerCards.pop(0)
        self.playerCards.pop(0)
        self.drawPile.append(playerCard)
        self.drawPile.append(computerCard)

    def checkWin(self):
        if len(self.computerCards) == 0 and len(self.playerCards) != 0:
            print("You win the game! :)")
            return True
        elif len(self.computerCards) != 0 and len(self.playerCards) == 0:
            print("You lose the game! :(")
            return True
        elif len(self.computerCards) == 0 and len(self.playerCards) == 0:
            print("Draw, all cards are in the draw pile.")
            return True
        else:
            return False

    def computerSelectStat(self, computerCard):
        if computerCard.attack > computerCard.defense:
            return "Attack"
        else:
            return "Defense"

    def playerSelectStat(self):
        print("Select stat (Attack or Defense)")
        while True:
            userInput = input("Enter value: ")
            userInput = userInput.title()
            userInput = userInput.strip()
            if userInput == "Attack" or userInput == "Defense":
                return userInput
            else:
                print("Invalid input, please enter Attack or Defense")

card1 = Card("card1", 7, 5)
card2 = Card("card2", 5, 8)
card3 = Card("card3", 3, 10)
card4 = Card("card4", 10, 4)

cardList = [card1, card2, card3, card4]

game = Game(cardList)
game.dealCards()
#players = ["player", "computer"]
#random.shuffle(players)
#currentTurn = players[0]
#if the beginning player is computer the computer might win because of luck
currentTurn = "player"
while game.checkWin() == False:
    print("Remaining cards: {}".format(len(game.playerCards)))
    playerCard = game.playerCards[0]
    computerCard = game.computerCards[0]
    playerCard.outputCard()
    if currentTurn == "player":
        stat = game.playerSelectStat()
    else:
        stat = game.computerSelectStat(computerCard)
        print("Computer chose {}.".format(stat))
    prevTurn = currentTurn
    input("Press enter to reveal.")
    print("")
    currentTurn = game.compareCards(stat, computerCard, playerCard)
    if currentTurn == None:
        if prevTurn == "player":
            currentTurn = "computer"
        else:
            currentTurn = "player"
    print("")