def rock_paper_scissor():
    import random

    print("welcome")
    ans=int(input("Choose 1 for Rock, 2 for paper, 3 scissor"))
    n1="Rock"
    n2="Paper"
    n3="Scissor"

    random_number=random.randint(0,3)

    if(ans==random_number):
        print("You both draw the same thing")
        rock_paper_scissor()
    elif((ans==1 and random_number==2)or(ans==2 and random_number==3)or(ans==3 and random_number==1)):
        print(n1+"=="+n2)
        print("Computer wins")
    else:
        print("Congrats you win")

    replay=int(input("choose 1 for replay and 2 for exit"))
    if(replay==1):
        rock_paper_scissor()
    else:
        print("Bye")


rock_paper_scissor()