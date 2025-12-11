from cmu_graphics import *
import random
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
possibleSymbols = ['snowman', 'snowflake', 'present', 'wreath']
random.randint(0,3)
def onMousePress(mouseX,mouseY):
    if mouseX < 125 and mouseX >= 0 and mouseY < 200:
        card1.fill = None
        if app.firstCardUp == True:
            app.bothCardsUp = True
            app.firstCardUp = False
        else:
            app.firstCardUp = True
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
cmu_graphics.run()