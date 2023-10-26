# File: ayasin_hw5b.py
# Author: Israk Ayasin
# Date: 10/13/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# Rolling game
# Collaboration:
# Manualle, Tobias

import random
def main():
    i=random.randint(1,6)
    total=0
    while i!=1 and total<20:
        print("Roll:",i)
        total+=i
        i=random.randint(1,6)
    if i==1:
        print("Roll: 1")
        total=0
    print("Turn total:",total)
    print("-------------------------------------------------------------------------------------------")

main()