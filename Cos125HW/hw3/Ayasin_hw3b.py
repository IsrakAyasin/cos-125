# Collaboration:
# I didn't collaborate with anyone
def main():
    first_number=int(input("What's your first year:"))
    second_number=int(input("What's your second year:"))
    for i in range(first_number,second_number+1):
        if (i%4==0):
            print(i,"is a leap year!")
        else:
            print(i)

main()