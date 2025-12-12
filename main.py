from cmu_graphics import *
import random
app.stepsPerSecond = 1
possibleSymbols = ['snowman', 'snowflake', 'present', 'wreath']
app.symbols = possibleSymbols + possibleSymbols
random.shuffle(app.symbols)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[0]}.png", 10, 50, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[1]}.png", 135, 50, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[2]}.png", 260, 50, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[3]}.png", 385, 50, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[4]}.png", 10, 250, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[5]}.png", 135, 250, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[6]}.png", 260, 250, width=100, height=100)
Image(f"https://raw.githubusercontent.com/kanokid/memory-game/master/icons/{app.symbols[7]}.png", 385, 250, width=100, height=100)
card1 = Rect(0,0,125,200, border='black',fill='white')
card2 = Rect(125,0,125,200, border='black',fill='white')
card3 = Rect(250,0,125,200, border='black',fill='white')
card4 = Rect(375,0,125,200, border='black',fill='white')
card5 = Rect(0,200,125,200, border='black',fill='white')
card6 = Rect(125,200,125,200, border='black',fill='white')
card7 = Rect(250,200,125,200, border='black',fill='white')
card8 = Rect(375,200,125,200, border='black',fill='white')
app.firstCardUp = False
app.bothCardsUp = False
app.firstCardIdentifier = 0
app.secondCardIdentifier = 0
app.matchCheckTimer = 0
app.matchedCards = []
def onMousePress(mouseX,mouseY):
    if mouseX < 125 and mouseX >= 0 and mouseY < 200:
        if 1 not in app.matchedCards:
            card1.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 1
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 1
    elif mouseX < 250 and mouseX > 125 and mouseY < 200:
        if 2 not in app.matchedCards:
            card2.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 2
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 2
    elif mouseX < 375 and mouseX > 250 and mouseY < 200:
        if 3 not in app.matchedCards:
            card3.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 3
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 3
    elif mouseX < 500 and mouseX > 375 and mouseY < 200:
        if 4 not in app.matchedCards:
            card4.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 4
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 4
    elif mouseX < 125 and mouseX > 0 and mouseY > 200:
        if 5 not in app.matchedCards:
            card5.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 5
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 5
    elif mouseX < 250 and mouseX > 125 and mouseY > 200:
        if 6 not in app.matchedCards:
            card6.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 6
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 6
    elif mouseX < 375 and mouseX > 250 and mouseY > 200:
        if 7 not in app.matchedCards:
            card7.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 7
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 7
    elif mouseX < 500 and mouseX > 375 and mouseY > 200:
        if 8 not in app.matchedCards:
            card8.fill = None
            if app.firstCardUp == True:
                app.bothCardsUp = True
                app.firstCardUp = False
                app.secondCardIdentifier = 8
            else:
                app.firstCardUp = True
                app.firstCardIdentifier = 8
    if app.bothCardsUp == True:
        app.matchCheckTimer = 2
        print ("hi")
def checkIfMatch():
    if app.symbols[app.firstCardIdentifier-1]  == app.symbols[app.secondCardIdentifier-1] and app.firstCardIdentifier != 0 and app.secondCardIdentifier != 0:
        app.matchedCards.append(app.firstCardIdentifier)
        app.matchedCards.append(app.secondCardIdentifier)
        if len(app.matchedCards) == 8:
            print("You win!")
    else:
        resetNonMatchedCards()
def resetAllCards():
    card1.fill = "white"
    card2.fill = "white"
    card3.fill = "white"
    card4.fill = "white"
    card5.fill = "white"
    card6.fill = "white"
    card7.fill = "white"
    card8.fill = "white"
    app.firstCardUp = False
    app.bothCardsUp = False
    app.firstCardIdentifier = 0
    app.secondCardIdentifier = 0
def onStep():
    if app.matchCheckTimer > 0:
        app.matchCheckTimer -= 1
        if app.matchCheckTimer == 0:
            checkIfMatch()
            app.bothCardsUp = False
cmu_graphics.run()