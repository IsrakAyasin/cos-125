# File: ayasin_hw5b.py
# Author: Israk Ayasin
# Date: 10/13/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# name song
# Collaboration:
# Manualla, Tobias
def main():
    name=input("Name to use:")
    while name!="quit":
        if name[0] not in "AIUOEaiuoe":
            pName=name[1:]
        else:
            pName=name
        if name[0]in"Bb":
            print(name+",", name+",", "bo-"+pName,"\nBanana-fana fo-f"+pName+"\nFee-fi-mo-m"+pName+"\n"+name+"!")
        elif name[0]in"Ff":
            print(name+",", name+",", "bo-b"+pName,"\nBanana-fana fo-"+pName+"\nFee-fi-mo-m"+pName+"\n"+name+"!" )
        elif name[0]in"Mm":
            print(name+",", name+",", "bo-b"+pName,"\nBanana-fana fo-f"+pName+"\nFee-fi-mo-"+pName+"\n"+name+"!" )
        else:
            print(name+",", name+",", "bo-b"+pName,"\nBanana-fana fo-f"+pName+"\nFee-fi-mo-m"+pName+"\n"+name+"!" )
        name=input("Name to use:")
    print("OK. Goodbye!")

main()