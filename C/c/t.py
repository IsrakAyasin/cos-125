def changeToQuestion(myStr):
    newStr =""
    for i in range(len(myStr)):
        if i%2 == 0:
            newStr = newStr + '?'
        else:
            newStr =newStr + myStr[i]
    return newStr
print(changeToQuestion("Relegation"))