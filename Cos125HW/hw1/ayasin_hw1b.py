# File: ayasin_hw1d.py
# Author: Israk Ayasin
# Date: 9/14/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# buying ice cream for 3 people
# Collaboration:
# I didn't collaborate with anyone
def buying_icecream():
    price=int(input("How much is this ice cream bar?"))
    total_cost=round(3*(price+price*.055),2)
    print("I would like three bars. Here is $" + str(total_cost))
    print("Thank you")

buying_icecream()