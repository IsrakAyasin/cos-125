# This file contains the code you will test.
# DO NOT SCROLL DOWN UNTIL YOU FINISH WRITING THE TESTS.



































































































import random



# Divide on Less than
def DivideOnLessThan(a, b):
    if b <= a:
        return a / b
    else:
        return 0.0

# Ask yes or no
def AskYesOrNo():
    rtn = None
    while rtn==None:
        c = input("Yes or No? ")
        c = c.lower()
        if c[0]=='y':
            rtn = True
        elif c[0]=='n':
            rtn = False
    return rtn

# ListSearch
def SearchListInReverse(alist, item):
    rtn = None
    for i in range(len(alist)-1, 0, -1):
        if item==alist[i]:
            rtn = i
    return rtn




# SplitStringAtPunctuation
def SplitStringAtPunctuation(astring):
    punct=".?!"
    rtn = []
    s = 0
    e = 0
    while e < len(astring):
        if astring[e] not in punct:
            e+=1
        else:
            rtn.append(astring[s:e])
            s = e = e+1
    return rtn



# ChoiceDiscrete
def ChoiceDiscrete(alist, problist):

    # Create the prob distribution
    pl = []
    total = 0
    for x in problist:
        x=x*x
        total+=(x)
        pl.append(total)
        
    randnum = random.uniform(0,total)

    # Find the first index in pl that is greater
    # than the random number.
    index = 0
    while index < len(pl) and pl[index] <= randnum:
        index+=1

    return alist[index]
    
    
