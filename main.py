from cmu_graphics import *
import random
app.width = 500
app.stepsPerSecond = 100
possibleSymbols = ['snowman', 'snowflake', 'present', 'wreath']

# ... existing code ...
app.symbols = possibleSymbols + possibleSymbols
levelWin = Sound('https://raw.githubusercontent.com/kanokid/memory-game/master/sound%20effects/win.mp3')
def playMatchingGame():
    random.shuffle(app.symbols)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[0]}.png", 10, 50, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[1]}.png", 135, 50, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[2]}.png", 260, 50, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[3]}.png", 385, 50, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[4]}.png", 10, 250, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[5]}.png", 135, 250, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[6]}.png", 260, 250, width=100, height=100)
    Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[7]}.png", 385, 250, width=100, height=100)
    app.card1 = Rect(0,0,125,200, border='black',fill='white')
    app.card2 = Rect(125,0,125,200, border='black',fill='white')
    app.card3 = Rect(250,0,125,200, border='black',fill='white')
    app.card4 = Rect(375,0,125,200, border='black',fill='white')
    app.card5 = Rect(0,200,125,200, border='black',fill='white')
    app.card6 = Rect(125,200,125,200, border='black',fill='white')
    app.card7 = Rect(250,200,125,200, border='black',fill='white')
    app.card8 = Rect(375,200,125,200, border='black',fill='white')
    app.firstCardUp = False
    app.bothCardsUp = False
    app.firstCardIdentifier = 0
    app.secondCardIdentifier = 0
    app.matchCheckTimer = 0
    app.matchedCards = []
    app.coverAllCards = Rect(0,0,500,400, fill='white', visible=False)
def onMousePress(mouseX,mouseY):
    if app.matchCheckTimer > 0:
        return
    else:
        if app.bothCardsUp == True:
            return
        else:
            if 0 <= mouseX < 125 and mouseY < 200:
                if 1 not in app.matchedCards and app.firstCardIdentifier != 1:
                    app.card1.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 1
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 1
            elif 125 < mouseX < 250 and mouseY < 200:
                if 2 not in app.matchedCards and app.firstCardIdentifier != 2:
                    app.card2.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 2
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 2
            elif 250 < mouseX < 375 and mouseY < 200:
                if 3 not in app.matchedCards and app.firstCardIdentifier != 3:
                    app.card3.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 3
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 3
            elif 375 < mouseX < 500 and mouseY < 200:
                if 4 not in app.matchedCards and app.firstCardIdentifier != 4:
                    app.card4.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 4
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 4
            elif 0 <= mouseX < 125 and mouseY > 200:
                if 5 not in app.matchedCards and app.firstCardIdentifier != 5:
                    app.card5.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 5
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 5
            elif 125 < mouseX < 250 and mouseY > 200:
                if 6 not in app.matchedCards and app.firstCardIdentifier != 6:
                    app.card6.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 6
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 6
            elif 250 < mouseX < 375 and mouseY > 200:
                if 7 not in app.matchedCards and app.firstCardIdentifier != 7:
                    app.card7.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 7
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 7
            elif 375 < mouseX < 500 and mouseY > 200:
                if 8 not in app.matchedCards and app.firstCardIdentifier != 8:
                    app.card8.fill = None
                    if app.firstCardUp == True:
                        app.bothCardsUp = True
                        app.firstCardUp = False
                        app.secondCardIdentifier = 8
                    else:
                        app.firstCardUp = True
                        app.firstCardIdentifier = 8
            if app.bothCardsUp == True:
                app.matchCheckTimer = 75

def checkIfMatch():
    if app.symbols[app.firstCardIdentifier-1]  == app.symbols[app.secondCardIdentifier-1] and app.firstCardIdentifier != 0 and app.secondCardIdentifier != 0:
        app.matchedCards.append(app.firstCardIdentifier)
        app.matchedCards.append(app.secondCardIdentifier)
        if len(app.matchedCards) == 8:
            victorySequence()
    else:
        resetNonMatchedCards()

    app.bothCardsUp = False
    app.firstCardUp = False
    app.firstCardIdentifier = 0
    app.secondCardIdentifier = 0

def resetNonMatchedCards():
    if 1 not in app.matchedCards:
        app.card1.fill = "white"
    if 2 not in app.matchedCards:
        app.card2.fill = "white"
    if 3 not in app.matchedCards:
        app.card3.fill = "white"
    if 4 not in app.matchedCards:
        app.card4.fill = "white"
    if 5 not in app.matchedCards:
        app.card5.fill = "white"
    if 6 not in app.matchedCards:
        app.card6.fill = "white"
    if 7 not in app.matchedCards:
        app.card7.fill = "white"
    if 8 not in app.matchedCards:
        app.card8.fill = "white"

app.timeUntilReset = 400
def resetAllCards():
    app.card1.fill = "white"
    app.card2.fill = "white"
    app.card3.fill = "white"
    app.card4.fill = "white"
    app.card5.fill = "white"
    app.card6.fill = "white"
    app.card7.fill = "white"
    app.card8.fill = "white"
    app.firstCardUp = False
    app.bothCardsUp = False
    app.firstCardIdentifier = 0
    app.secondCardIdentifier = 0
    app.coverAllCards.visible = False

def onStep():
    if app.matchCheckTimer > 0:
        app.matchCheckTimer -= 1
        if app.matchCheckTimer == 0:
            checkIfMatch()
            app.bothCardsUp = False

    if len(app.matchedCards) == 8:
        if app.timeUntilReset > 0:
            app.timeUntilReset -= 1
            if app.timeUntilReset == 0:
                app.matchedCards = []
                resetAllCards()
                app.timeUntilReset = 400

def victorySequence():
    print("You win!")
    Label('You win!',250,200,size=125)
    app.coverAllCards.visible = True
playMatchingGame()
#victorySequence()
cmu_graphics.run()