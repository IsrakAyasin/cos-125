#If statement will work
cash = 1.5
if int ( cash )*2.0 != int ( cash *2.0):
    print ( " The devil is in the details . " )

#will print(It is mild)
temp = 40
if temp < 40:
    print ( " It is cold . " )
elif temp < 70:
    print ( " It is mild . " )
elif temp < 90:
    print ( " It is hot . " )
else :
    print ( " It is unbearable . " )


#correct version
i = 1
total=0
while i <= 10:
    total = total + i
    i = i + 1
    
print ( total )