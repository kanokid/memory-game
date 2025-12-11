from cmu_graphics import *
import random
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
def onMousePress(mouseX,mouseY):
    if mouseX < 125 and mouseX >= 0 and mouseY < 200:
        card1.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
            app.firstCardIdentifier
    elif mouseX < 250 and mouseX > 125 and mouseY < 200:
        card2.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
    elif mouseX < 375 and mouseX > 250 and mouseY < 200:
        card3.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
    elif mouseX < 500 and mouseX > 375 and mouseY < 200:
        card4.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
    elif mouseX < 125 and mouseX > 0 and mouseY > 200:
        card5.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
    elif mouseX < 250 and mouseX > 125 and mouseY > 200:
        card6.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
    elif mouseX < 375 and mouseX > 250 and mouseY > 200:
        card7.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
    elif mouseX < 500 and mouseX > 375 and mouseY > 200:
        card8.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
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
cmu_graphics.run()