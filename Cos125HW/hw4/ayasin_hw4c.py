# File: ayasin_hw4a.py
# Author: Israk Ayasin
# Date: 10/13/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
#singing songs as many times as you want and whichever topic you chose
# Collaboration:
# I didn't collaborate with anyone
def main():
    favorite_food=input("What is your favorite Maine food?")
    verse_num=int(input("How many verses?"))
    def verse(food,verse):
        for i in range(verse,0,-1):
            print(i," bottles of",food,"on the wall,",i,"bottles of",food,", Take one down, pass it around,",i-1,"bottles of",food,"on the wall.\n")
        print("Oh, no. The",food,"is all gone!")
    verse(favorite_food,verse_num)
main()