from mondraian.graphics import *
import random

def Rect():
    rec=Rectangle(Point(0,0), Point (splitpoint(800),600))
    print(splitpoint(800))
    return rec
    
def color():
    r=random.random()
    if r<0.09:
        return "yellow"
    elif r<0.15:
        return "blue"
    elif r<0.25:
        return "red"
    else:
        return "white"

def splitOrNot(size):
    rand=random.randrange(90,size*1.5)
    if rand<size or size>400:
        return True
    else:
        return False

def splitpoint(size):
    lower=size*.31
    higher=size*.68
    rand=random.randrange(lower,higher)
    return rand
    
def main():
    win = GraphWin("My Drawing", 800, 600)
    aRect = Rectangle(Point(0,0), Point (800,600))
    hig=Rectangle(Point(0,0), Point(800,splitpoint(500)))
    
    aRect.draw(win)
    Rect().draw(win)
    hig.draw(win)
    win.getMouse()
    win.close()
main()