from codecs import utf_8_encode
from operator import truediv
print("task-1")
file=open("lab7_data.txt","r",encoding="utf")
read=file.read()
print(read)
file.close()


print("task-2")
file=open("lab7_data.txt","r",encoding="utf")
for i in file:
    i=i.split(";")
    if i[1]=="Germany":
        print(i[0],i[2])
file.close()


print("task-3")
file=open("lab7_data.txt","r",encoding="utf")
used=[]
for i in file:
    i=i.strip().split(";")
    
    found=False
    for j in used:
        if j[0]==i[1]:
            j[1]+=1
            found=True
    if not found:
        used.append([i[1],1])
for k in used:
    print(f"{k[0]}: {k[1]}")
file.close()


print("\ntask4\n")
file=open("lab7_data.txt",encoding="utf")
read=file.read()
file.close
read=read.replace(",","")


write=open("lab7_data_clean.txt","w",encoding="utf")
write.write(read)
write.close()


print("\ntask5\n")
file=open("lab7_data_clean.txt",encoding="utf")
writ=open("test.txt","w",encoding="utf")
for ign in file:
    i1=ign.strip().split(";")
    if int(i1[2])>1000000:
        writ.write(str(ign))
file.close()
writ.close()

print("\ntask6\n")
file=open("lab7_data.txt","r",encoding="utf")
read=file.read()
file.close
read=("City;Country;Population\n"+read)
wrt=open("lab7_data.txt","w",encoding="utf")
#wrt.write(read)
wrt.close()

print("\ntask7\n")
data=[
"Duisburg;Germany;495,152",
"Toulouse;France;493,465",
"Gdańsk;Poland;486,271",
"Bratislava;Slovakia;475,044",
"Murcia;Spain;460,349",
"Tallinn;Estonia;437,811",
"Palma de Mallorca;Spain;419,366"]

file=open("lab7_data.txt","a",encoding="utf")

for i in data:
    file.write(i+"\n")
file.close()