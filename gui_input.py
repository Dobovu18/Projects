"""
Here I work on GUI inputs, from the keyboard and mouse.
"""

from graphics import *

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    #pass #is a placeholder for code, it does nothing
    
    #First I create a textbox
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        #while we are typing (until we press enter) the commands in handleKey aren't relevant
        #As we are stuck in this while loop until we press enter
        key = win.getKey()
        if key == "Return": break #Exist typing mode if enter is pressed

    entry.undraw() #We remove the text box
    typed = entry.getText() #We get the text from the textbox
    Text(pt, typed).draw(win) #We then draw a text label containing the typed text from textbox

    win.checkMouse()


def main():
    win = GraphWin("Click and Type", 500, 500)
    while True:
        key = win.checkKey()
        
        if key == "q": break #pressing q exist the loop
        if key: handleKey(key, win) #"if key:" is short for 'if key != ""'
        
        pt = win.checkMouse()
        if pt: handleClick(pt, win)
    
    win.close()

main()