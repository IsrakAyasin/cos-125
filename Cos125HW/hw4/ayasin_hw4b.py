# File: ayasin_hw4b.py
# Author: Israk Ayasin
# Date: 10/13/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
#saying their favorite things about their favorite park
# Collaboration:
# I didn't collaborate with anyone

def main():
    park_name_list=[]
    visitor_number_list=[]
    favorite_list=[]
    tem=""
    count=-1
    while tem!="done":
        tem=input("What is one of your favorite Maine parks(or ‘done’ to end)?")
        if tem == "done":
            break
        count+=1
        park_name_list.append(tem)
        visitor_number_list.append(int(input(f"How many thousand people visit {tem} in a year?")))
        favorite_list.append(input(f"What is your favorite thing about {tem}?"))

    if count>=0:
        favorite_place=int(input(f"Which park to celebrate (between 0 and {count})?"))
        nTemp= visitor_number_list[favorite_place]-10
        print(favorite_list[favorite_place])

        while nTemp-10 > 0:
            print(favorite_list[favorite_place])
            nTemp-=10
main()
