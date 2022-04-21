#Tanishq Madhusudan and Ryan Harwood
import turtle
import tkinter
from turtle import *
from tkinter import *
turtle.setup(600,600)
wn = turtle.Screen()
wn.bgcolor('orange')
wn.title('Tic Tac Toe')
r = turtle.Turtle()
r.hideturtle()


# global variables
xP = turtle.Turtle()
oP = turtle.Turtle()
pieces = [' ',' ',' ',
          ' ',' ',' ',
          ' ',' ',' ']
wwinner = False
nextTurn = 'X'
square = -1
xP.hideturtle()
oP.hideturtle()
oP.speed('fastest')
xP.speed('fastest')
amtplayers = 2


def drawO(a,b):
    oP.penup()
    oP.goto(a,b-75)
    oP.pendown()
    oP.circle(80)

def drawX(a,b):
    xP.penup()
    xP.goto(a,b)
    xP.pendown()
    xP.goto(a+80,b+80)
    xP.goto(a-80,b-80)
    xP.goto(a,b)
    xP.goto(a-80,b+80)
    xP.goto(a+80,b-80)

def clicked(x,y):
    global nextTurn, pieces
    if (x < -100) and (y > 100):
        a = -200
        b = 200
        square = 0
    elif (x < 100) and (y > 100):
        a = 0
        b = 200
        square = 1
    elif (x < 300) and (y > 100):
        a = 200
        b = 200
        square = 2
    elif (x < -100) and (y > -100):
        a = -200
        b =  0
        square = 3
    elif (x < 100) and (y > -100):
        a = 0
        b = 0
        square = 4
    elif (x < 300) and (y > -100):
        a = 200
        b = 0
        square = 5
    elif (x < -100) and (y > -300):
        a = -200
        b = -200
        square = 6
    elif (x < 100) and (y > -300):
        a = 0
        b = -200
        square = 7
    elif (x < 300) and (y > -300):
        a = 200
        b = -200
        square = 8
    checkDrawPiece(square,a,b)


def checkDrawPiece(square,a,b):
    global nextTurn,pieces
    if pieces[square] == ' ':
        if nextTurn == 'X':
            pieces[square] = nextTurn
            drawX(a,b)
            checkWinner('X','O')
        elif nextTurn == 'O':
            pieces[square] = nextTurn
            drawO(a,b)
            checkWinner('O','X')
    else:
        tkinter.messagebox.showwarning('Warning','Place already taken')
        
def main():
    global nextTurn,amtplayers
    xP.pensize(2)
    
    board = tkinter.simpledialog.askstring("Input", "Pick background color.")

    amtplayers = tkinter.simpledialog.askinteger("Input", "How many players?(1/2)")
    chooseTurn()
    
    wn.bgcolor(board)
    r.pensize(2)
    r.speed('fastest')
    oP.pensize(2)


    # Board Setup
    r.penup()
    r.goto(-100,300)
    r.pendown()
    r.goto(-100,-300)
    r.goto(100,-300)
    r.goto(100,300)
    r.penup()
    r.goto(-300,-100)
    r.pendown()
    r.goto(300,-100)
    r.penup()
    r.goto(-300,100)
    r.pendown()
    r.goto(300,100)
    onscreenclick(clicked)
    mainloop()
def clearScreen():
    global pieces, nextTurn, wwinner
    pieces = [' ',' ',' ',
          ' ',' ',' ',
          ' ',' ',' ']
    xP.clear()
    oP.clear()
    wwinner = False
    chooseTurn()
    
    
    
def checkWinner(w,l):
    global pieces, nextTurn, wwinner, amtplayers
    winner = False
    if (pieces[0] == w and pieces[1] == w and pieces[2] == w) or (pieces[3] == w and pieces[4] == w and pieces[5] == w) or (pieces[6] == w and pieces[7] == w and pieces[8] == w) or (pieces[0] == w and pieces[3] == w and pieces[6] == w) or (pieces[1] == w and pieces[4] == w and pieces[7] == w) or (pieces[2] == w and pieces[5] == w and pieces[8] == w) or(pieces[0] == w and pieces[4] == w and pieces[8] == w) or (pieces[2] == w and pieces[4] == w and pieces[6] == w):
        tkinter.messagebox.showinfo('Python',w + ' wins')
        thing = tkinter.messagebox.askyesno('Python','Would you like to play again?')
        wwinner = True
        winner = True
        if  thing == True:
            clearScreen()
        if  thing == False:
            turtle.bye()
    if winner == False:
        nextTurn = l
        if l == 'X' and amtplayers == 1:
            AI()
    if wwinner == False and ' ' not in pieces:
        thingy = tkinter.messagebox.askyesno('Python','Tie! Would you like to play again?')
        if thingy == True:
            clearScreen()
        elif thingy == False:
            turtle.bye()
def chooseTurn():
    global nextTurn
    answer = tkinter.simpledialog.askstring("Input", "Who would like to go first? X/O")
    nextTurn = answer
    if answer == 'X' and amtplayers == 1:
        AI()

def AI():
    global wwinner,pieces
    possibleMoves = [x for x, letter in enumerate(pieces) if letter == ' '] # Create a list of possible moves
    move = 0

    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
            move = selectRandom(edgesOpen)

    if 4 in possibleMoves:
        move = 4

    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
            
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = pieces[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let)== True:
                move = i


    if move == 0:
        a = -200
        b = 200
    if move == 1:
        a = 0
        b = 200
    if move == 2:
        a = 200
        b = 200
    if move == 3:
        a = -200
        b = 0
    if move == 4:
        a = 0
        b = 0
    if move == 5:
        a = 200
        b = 0
    if move == 6:
        a = -200
        b = -200
    if move == 7:
        a = 0
        b = -200
    if move == 8:
        a = 200
        b = -200
    clicked(a,b)

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the bottom
    (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
    (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
    (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal

main()