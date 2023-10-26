# Collaboration:
# I didn't collaborate with anyone
def main():
    monsters = [ "Squirtle","Venonat","Eevee", "Cherim","Bronzong","Bergmite"]
    for i in range(len(monsters)):
        print(i,":",monsters[i])
    if len(monsters)%2!=0:
        print("My favorite is",monsters[len(monsters)//2])
    else:
        print("My favorite is",monsters[int(len(monsters)/2)-1])

main()


