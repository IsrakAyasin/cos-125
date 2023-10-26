# Collaboration:
# I didn't collaborate with anyone

def attendance():
    print("Hello, I will calculate the lab attendance average.")
    lab0=int(input("What was the attendance at Lab 0?"))
    lab1=int(input("What was the attendance at Lab 1?"))
    lab2=int(input("What was the attendance at Lab 2?"))
    lab3=int(input("What was the attendance at Lab 3?"))
    
    average=(lab0+lab1+lab2+lab3)/4

    print("The average attendance in the first four labs was "+str(average))
    if lab0>20:
        print("Warning! The first lab meeting looks like it exceeded the room capacity!")
    if lab1>20:
        print("Warning! The second lab meeting looks like it exceeded the room capacity!")
    if lab2>20:
        print("Warning! The third lab meeting looks like it exceeded the room capacity!")
    if lab3>20:
        print("Warning! The last lab meeting looks like it exceeded the room capacity!")
attendance()
    