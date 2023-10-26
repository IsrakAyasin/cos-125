# Collaboration:
# I didn't collaborate with anyone

def recycle_bottle():
    print("Hello, I will give recycling advice.")
    use=int(input("How many bottles/cans did you use today?"))
    recycle=int(input("How many did you recycle? "))
    sum=use-recycle
    print("You used "+str(sum)+" more bottles than you recycled.")
    if sum==0:
        print("Good job recycling all your cans/bottles!")
    elif sum>0:
        print("You should recycle more. It's good for the environment")
    else:
        print("Good job you are Awesome! keep doing it")
    print("Remember to visit Boardman 138 for help or community.")
    
recycle_bottle()