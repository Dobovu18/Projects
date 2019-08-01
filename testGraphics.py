from graphics import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
"""
win = GraphWin()

p = Point(50, 60)

print(p.getX())
print(p.getY())

p.draw(win)
p2 = Point(140, 100)
p2.draw(win)
"""

win2 = GraphWin('Shapes')

#Draw a blue circle centred at (100, 100) with radius 30
center = Point(100, 100)
circle = Circle(center, 30)

circle.setFill('blue')
circle.draw(win2)

#Labelling the circle
label = Text(center, "Blue Circle")
label.draw(win2)

#Drawing a square using a rectangle object
rect = Rectangle(Point(30, 30), Point(70, 70))
rect.draw(win2)

#Draw a line segment using line object
line = Line(Point(20, 30), Point(180, 165))
line.draw(win2)

#Drawing an ellipse
oval = Oval(Point(20, 150), Point(180, 199))
oval.draw(win2)

def clicker():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())
    win.close()

clicker()


def triDraw():
    #This function draws a red triangle when the user clicks on 3 points
    win = GraphWin("Draw Triangle") #open new window
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    msg = Text(Point(5, 0.5), "Click on three points") #Create instruction label
    msg.draw(win)

    #Getting the points from where the user clicks
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #drawing and creating the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("red")
    triangle.setOutline("blue")
    triangle.draw(win)

    #Finishing
    msg.setText("Click anywhere to quit.")
    win.getMouse()

triDraw()

def textInput():
    #Click in and press a key for the character to be printed there on screen
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)

textInput()

def convert_gui():
    win = GraphWin("Celsius Converter", 600, 400)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    #Draw interface
    Text(Point(1, 3), "\tCelsius Temperature:").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)

    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")

    inputText.draw(win)
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

    #wait for mouse click
    win.getMouse()

    #convert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    #display output and change button
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")

    #wait for click and then quit
    win.getMouse()
    win.close()

convert_gui()

#infileName = askopenfilename() #opens file explorer for OPENING a file
#outfileName = asksaveasfilename() #opens file explorer for SAVING a file