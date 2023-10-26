# File: ayasin_p1.py
# Author: Israk Ayasin
# Date: 11/21/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# finding sntimental value, all average, lowest and highest reviewed word
# Collaboration:
# Manuella, Tobias
import sys
def sentiment_score(word):
    file=open("movieReviews.txt",encoding="utf")
    count=0
    total=0

    #for loop goes through the file and gets every line of the file
    for line in file:
        line=line.lower()
        line=line.strip().split()
        #this if statement check the word in the line and if it finds it, it add the review score by the first word of line and count by one.
        if word in line:
            total+=int(line[0]) 
            count+=1
    file.close()
    return(total,count)
    
def allAverage():
    word_files=input("Enter the name of the file with the words:\n-")
    word_file=open(word_files,encoding="utf")
    allTotal=0
    count=0

    #first for loop goes through the file and gets every line of the file and second for loop goes through every word and 
    #call sentiment_score with every word and using that to find total average
    for line in word_file:
        line=line.strip().split()
        for x in line:
            total,num=sentiment_score(x)
            count+=num
            allTotal+=total
    if count>0:
        average=round((allTotal/count),2)
    else:
        average=("not found")
    if average<1.75:
        print(f"The average score of the words in {word_files} is {average}. This is a insult.")
    elif average>2.25:
        print(f"The average score of the words in {word_files} is {average}. This is a compliment.")
    else:
        print(f"The average score of the words in {word_files} is {average}. This is neither insult or compliment.") 
    word_file.close()

def low_high():
    word_files=input("Enter the name of the file with the words:\n- ")
    file=open(word_files,encoding="utf")
    lowest_score= sys.maxsize
    highest_score= sys.maxsize - 1
    lowest_word="not found"
    highest_word="not found"

    #first for loop goes through the file and gets every line of the file and second for loop goes through every word and 
    #call sentiment_score with every word 
    for line in file:
        line=line.strip().split()
        for word in line:
            total,count=sentiment_score(word)
            if count>0:
                average=round((total/count),2)
                #it will compare everage score of every word with lowest_word and highest_word and change it.  
                if average < lowest_score:
                    lowest_score = average
                    lowest_word=word
                if average > highest_score:
                    highest_score=average
                    highest_word=word
    print(f"The most positive word in {word_files} is '{highest_word}' with a score of {highest_score}")
    print(f"The most negative word in {word_files} is '{lowest_word}' with a score of {lowest_score}")
    file.close()

#main fuction will just call the other fuctions and for sentiment_score it gets total review score and count from sentiment and it just print it.
def main():
    do=(input("""
    What would you like to do?
1. Calculate the sentiment score of a single word
2. Calculate the average score of words in a file
3. Find the highest and lowest scoring words in a file.
4. Exit the program\n- """))
    if(do=="1"):
        word=(input("give me a word\n- "))
        total,count=sentiment_score(word)
        if count==0:
            print("None found")
        else:
            print(f"\"{word}\" appears {count} times")
            print(f"The average score for reviews containing \"{word}\" {round((total/count),2)}")
        main()
    elif(do=="2"):
        allAverage()
        main()
    elif(do=="3"):
        low_high()
        main()
    elif(do=="4"):
        return
    else:
        print("put a valid number")
        main()  
main()
