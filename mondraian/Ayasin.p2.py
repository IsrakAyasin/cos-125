# File: ayasin_p1.py
# Author: Israk Ayasin
# Date: 12/09/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# Creating mondarian style drawing
# Collaboration: none

# The base case doesn't work. Rectangle keeps spliting again and again
# Maybe my spliting poits are off
from mondraian.graphics import *
import random

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
    if size<90:
        return False
    rand=random.randint(90,round(size*1.5))
    if rand<size or size>400:
        return True
    else:
        return False

def splitpoint(size):
    lower=round(size*.31)
    higher=round(size*.68)
    rand=random.randint(lower,higher)
    return rand
    
def main(x1,y1,x2,y2):
    if ((y2-y1)<90 and (x2-x1)<90) or ((not splitOrNot(y2-y1)) and (not splitOrNot(x2-x1))) or ((y2-y1)<90 and (not splitOrNot(x2-x1))) or ((x2-x1)<90 and (not splitOrNot(y2-y1))):
        rect = Rectangle(Point(x1, y1), Point(x2, y2))
        rect.setFill(color())
        rect.draw(win)
        return
    else:
        if splitOrNot(y2-y1) and splitOrNot(x2-x1):
            if random.random() < 0.5:
                # split the rectangle horizontally
                split_point = splitpoint(y2-y1)
                main(x1, y1, x2, split_point)
                main(x1, split_point, x2, y2)
            else:
                # split the rectangle vertically
                split_point = splitpoint(x2-x1)
                main(x1, y1, split_point, y2)
                main(split_point, y1, x2, y2)
        elif splitOrNot(x2-x1):
            # split the rectangle vertically
            split_point = splitpoint(x2-x1)
            main(x1, y1, split_point, y2)
            main(split_point, y1, x2, y2)
        elif splitOrNot(y2-y1):
            # split the rectangle horizontally
            split_point = splitpoint(y2-y1)
            main(x1, y1, x2, split_point)
            main(x1, split_point, x2, y2)
        
win = GraphWin("Rectangle", 800, 600)   
main(0, 0, 800, 600)
win.getMouse()
win.close()