# Collaboration:
# I didn't collaborate with anyone
import sys
def numbers():
    i=""
    number=-sys.maxsize - 1
    while i!="end":
        i=input("Enter a number (or ‘end’ to end):")
        if i!="end":
            i=int(i)
            if i>number:
                number=i
    print("Highest number is:",number)

numbers()