i=10
while i>=1:
    print(i)
    i=i-1
i=1
while i<=10:
    print(i)
    i=i+1

bot=input("give me a character")
while bot!=("q"):
    bot=input("give me a character")

i=1
sum=0
while i<=1000:
    if i%2!=0:
        sum=sum+i
    i=i+1

print(sum)