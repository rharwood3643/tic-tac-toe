import turtle
from tkinter import messagebox

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
        messagebox.showwarning('Warning','Place already taken')
        
def main():
    r.pensize(2)
    r.speed('fastest')
    xP.pensize(2)
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
    turtle.onscreenclick(clicked)
    turtle.mainloop()
def clearScreen():
    global pieces, nextTurn
    pieces = [' ',' ',' ',
          ' ',' ',' ',
          ' ',' ',' ']
    xP.clear()
    oP.clear()
    
def checkWinner(w,l):
    global pieces, nextTurn, wwinner
    winner = False
    if (pieces[0] == w and pieces[1] == w and pieces[2] == w) or (pieces[3] == w and pieces[4] == w and pieces[5] == w) or (pieces[6] == w and pieces[7] == w and pieces[8] == w) or (pieces[0] == w and pieces[3] == w and pieces[6] == w) or (pieces[1] == w and pieces[4] == w and pieces[7] == w) or (pieces[2] == w and pieces[5] == w and pieces[8] == w) or(pieces[0] == w and pieces[4] == w and pieces[8] == w) or (pieces[2] == w and pieces[4] == w and pieces[6] == w):
        messagebox.showinfo('Python',w + ' wins')
        thing = messagebox.askyesno('Python','Would you like to play again?')
        wwinner = True
        if  thing == True:
            clearScreen()
        if  thing == False:
            turtle.bye()
            
    if winner == False:
        nextTurn = l
    if wwinner == False and ' ' not in pieces:
        thingy = messagebox.askyesno('Python','Tie! Would you like to play again?')
        if thingy == True:
            clearScreen()
        elif thingy == False:
            turtle.bye()



main()