#######################
# LAB 7 Solution
# zsh
# Fall22
#######################

# Task 1
print("\nTASK 1\n")
fh = open('lab7_data.txt',encoding="utf")
contents = fh.read()
print(contents)
fh.close()

# Task 2
print("\nTASK 2\n")
fh = open('lab7_data.txt',encoding="utf")
for line in fh:
    line = line.strip().split(';')
    if line[1]=="Germany":
        print(line[0],line[2])
fh.close()

# Task 3
print("\nTASK 3\n")
fh = open('lab7_data.txt',encoding="utf")

counts = []
for line in fh:
    line = line.strip().split(';')

    found = False
    for c in counts:
        if c[0]==line[1]:
            c[1]+=1
            found = True
    if not found:
        counts.append([line[1],1])

for c in counts:
    print(f"{c[0]}: {c[1]}")

fh.close()

# Task 4
print("\nTASK 4\nDoes not print anything\n")

fh = open('lab7_data.txt',encoding="utf")
contents = fh.read()
fh.close()

contents = contents.replace(',','')

fh = open('lab7_data_clean.txt','w',encoding="utf")
fh.write(contents)
fh.close()


# Task 5
print("\nTASK 5\nDoes not print anything\n")
fin = open('lab7_data_clean.txt',encoding="utf")
fout =open('lab7_millionplus.txt','w',encoding="utf")
for line in fin:
    line2 = line.strip().split(';')
    if int(line2[2]) > 1000000:
        fout.write(line)
fin.close()
fout.close()


# Task 6
print("\nTASK 6\nDoes not print anything\n")
fh = open('lab7_data.txt',encoding="utf")
contents = fh.read()
fh.close()

contents = "CITY;COUNTRY;POPULATION\n"+contents

fh = open('lab7_data.txt','w',encoding="utf")
fh.write(contents)
fh.close()


# Task 7

print("\nTASK 7\nDoes not print anything\n")

data =  [
    "Duisburg;Germany;495,152",
    "Toulouse;France;493,465",
    "Gdańsk;Poland;486,271",
    "Bratislava;Slovakia;475,044",
    "Murcia;Spain;460,349",
    "Tallinn;Estonia;437,811",
    "Palma de Mallorca;Spain;419,366"
]

fh = open('lab7_data.txt','a',encoding="utf")
for d in data:
    fh.write(d+'\n')
fh.close()