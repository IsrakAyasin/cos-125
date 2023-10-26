#task1A
def Hello():
    print("Hello world")
Hello()
#task1B
def HelloTo(name):
    print("Hello",name)
HelloTo("yono")
#task1C
def Distance(x1,y1,x2,y2):
    print(((x2-x1)**2+(y2-y1)**2)**.5)
Distance(3,4,2,1)



#task2A
def GetDirection():
    user_input=input("q, e, w, n, s - enter one of these")
    while user_input not in("q","e","w","n","s"):
        user_input=input("q, e, w, n, s - enter one of these")
    return user_input
#GetDirection()
#task2B
def ParsInput(direction):
    if(direction=="e"):
        direction="east"
    elif(direction=="w"):
        direction="west"
    elif(direction=="n"):
        direction="north"
    else:
        direction="south"  
    
    print("The player moves",direction)
#ParsInput(GetDirection())
#task2c
def GameLoop():
    temp=GetDirection()
    while temp!="q":
        ParsInput(temp)
        if temp not in("e","s","w","n"):
            print("Bad move. Game reset")
        else:
            print("You are in the right track")
        temp=GetDirection()
#     GameLoop()

#task3a
def AbsVal(num):
    if num<0:
        return num*-1
    else:
        return num
#AbsVal(100)

def MinsToDaysHrsMins(minutes):
    day=0
    hrs=0
    min=0
    while minutes-1440>=0:
        day+=1
        minutes-=1440
    while minutes-60>=0:
        hrs+=1
        minutes-=60
    while minutes-1>=0:
        min+=1
        minutes-=1
    print(day,"day,",hrs,"hours,",min,"mins")
#MinsToDaysHrsMins(2300)

def ConverTemp(temp,scale):
    if scale == "F":
        temp=temp*1.8+32
    else:
        temp=(temp-32)*.5556
    print(temp)
ConverTemp(32,"F")
