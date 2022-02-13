import random
cardDict = {"card1": {"Attack": 7, "Defense": 5}, "card2": {"Attack": 5, "Defense": 8},
         "card3": {"Attack": 3, "Defense": 10}, "card4": {"Attack": 10, "Defense": 4}}

computerCards = []
playerCards = []
drawPile = []

def dealCards():
    cardList = [card for card in cardDict]
    random.shuffle(cardList)
    for i in range(len(cardList)):
        if i%2 == 0:
            playerCards.append(cardList[i])
        else:
            computerCards.append(cardList[i])

def computerSelectStat(currentCard):
    currentCardDict = cardDict[currentCard]
    attack = currentCardDict["Attack"]
    defense = currentCardDict["Defense"]
    if attack > defense:
        return "Attack"
    else:
        return "Defense"

def playerSelect():
    print("Select stat (Attack or Defense)")
    while True:
        userInput = input("Enter value: ")
        userInput = userInput.title()
        userInput = userInput.strip()
        if userInput == "Attack" or userInput == "Defense":
            return userInput
        else:
            print("Invalid input, please enter Attack or Defense")

def compareCards(stat, computerCard, playerCard):
    computerCardValues = cardDict[computerCard]
    computerValue = computerCardValues[stat]

    playerCardValues = cardDict[playerCard]
    playerValue = playerCardValues[stat]

    print("Your {}: {}\nComputer {}: {}".format(stat, playerValue, stat, computerValue))
    if playerValue > computerValue:
        print("You win round")
        playerWin(computerCard)
        return "player"
    elif computerValue > playerValue:
        print("Computer wins round")
        computerWin(playerCard)
        return "computer"
    else:
        print("This round was a draw")
        draw(computerCard, playerCard)
        return None

def playerWin(computerCard):
    playerCards.append(playerCards.pop(0))
    playerCards.append(computerCard)
    computerCards.pop(0)
    for card in drawPile:
        playerCards.append(card)
    for i in range(len(drawPile)):
        drawPile.pop(0)

def computerWin(playerCard):
    computerCards.append(computerCards.pop(0))
    computerCards.append(playerCard)
    playerCards.pop(0)
    for card in drawPile:
        computerCards.append(card)
    for i in range(len(drawPile)):
        drawPile.pop(0)

def draw(computerCard, playerCard):
    computerCards.pop(0)
    playerCards.pop(0)
    drawPile.append(playerCard)
    drawPile.append(computerCard)

def checkWin():
    if len(computerCards) == 0 and len(playerCards) != 0:
        print("You win the game! :)")
        return True
    elif len(computerCards) != 0 and len(playerCards) == 0:
        print("You lose the game! :(")
        return True
    elif len(computerCards) == 0 and len(playerCards) == 0:
        print("Draw, all cards are in the draw pile.")
        return True
    else:
        return False

def outputCard():
    cardName = playerCards[0]
    cardDetails = cardDict[cardName]
    print("Card Name: {}\nAttack: {}\nDefense: {}\n".format(cardName, cardDetails["Attack"], cardDetails["Defense"]))

dealCards()
#players = ["player", "computer"]
#random.shuffle(players)
#currentTurn = players[0]
#if the beginning player is computer the computer might win because of luck
currentTurn = "player"
while checkWin() == False:
    print("Remaining cards: {}".format(len(playerCards)))
    playerCard = playerCards[0]
    computerCard = computerCards[0]
    outputCard()
    if currentTurn == "player":
        stat = playerSelect()
    else:
        stat = computerSelectStat(computerCard)
        print("Computer chose {}.".format(stat))
    prevTurn = currentTurn
    input("Press enter to reveal.")
    print("")
    currentTurn = compareCards(stat, computerCard, playerCard)
    if currentTurn == None:
        if prevTurn == "player":
            currentTurn = "computer"
        else:
            currentTurn = "player"
    print("")