# Collaboration:
# I didn't collaborate with anyone
def main():
    first_input=int(input("What is your first number "))
    second_input=int(input("What is your second number "))

    while first_input>=0 and second_input>=0:
        if first_input==0 or second_input==0:
            print("Hmmm. Nothing to see here.")
        else:
            for i in range(1,first_input+1):
                for j in range(1,second_input+1):
                    print(i*j,end=" ")
                print("")
        first_input=int(input("What is your first number"))
        second_input=int(input("What is your second number"))
    print("Goodbye")
main()

