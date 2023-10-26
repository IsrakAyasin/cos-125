# File: ayasin_hw4a.py
# Author: Israk Ayasin
# Date: 10/13/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# Making slogan
# Collaboration:
# Manualle, Tobias
import random
def main():
    names=["Hulk", "Spock", "Ted Lasso"," Aaron Burr", "The Cowardly Lion", "Cinderella", "Black Panther", "Merida", "Uhuru", "Freya", "Frodo", "Megan Rapinoe"]
    verbs=["Leading", "Serving", "Building", "Creating", "Putting", "Fighting", "Taking", "Cleaning up", "Protecting", "Putting", "Smashing", "Working", "Coaching", "Kicking"]
    direct_objects=["the future", "our community", "jobs", "education", "corruption", "action", "families", "change", "progress", "government", "results", "our enemies"]
    adverb_phrases=["with integrity", "for you", "first", "safe", "for the future", "for a change", "for Maine", "with experience", "with vision"]

    slogan_number=int(input("How many slogans would you like?"))

    for i in range(slogan_number):
        print(random.choice(names)+":",random.choice(verbs),random.choice(direct_objects),random.choice(adverb_phrases))

main()