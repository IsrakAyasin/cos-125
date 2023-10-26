# File: ayasin_hw4a.py
# Author: Israk Ayasin
# Date: 10/13/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
#Getting average, maximum attendence, minumum attendence, total attendence
# Collaboration:
# I didn't collaborate with anyone

def main():
    park_name_list=[]
    visitor_number_list=[]
    for i in range(5):
        tem=input("What is one of your favorite Maine parks?")
        park_name_list.append(tem)
        visitor_number_list.append(int(input(f"How many thousand people visit {tem} in a year?")))

    def attendMax():
        largest=visitor_number_list[0]
        count=0
        for i in visitor_number_list:
            count+=1
            if i>largest:
                largest=i
        index=visitor_number_list.index(largest)
        print("The park with the most visitors is",park_name_list[index],"with",largest,"thousand")
    attendMax()

    def attendMin():
        min=visitor_number_list[0]
        for i in visitor_number_list:
            if i <min:
                min=i
        index=visitor_number_list.index(min)
        print("The park with the fewest visitors is",park_name_list[index],"with",min,"thousand")
    attendMin()

    def attendTotal():
        total=0
        for i in visitor_number_list:
            total+=i
        print("The total number of visitors at those parks is",total,"thousand.")      
    attendTotal()
    def attendAvg():
        total=0
        for i in visitor_number_list:
            total+=i
        print("The average number of visitors per park is",total/len(visitor_number_list),"thousand")
    attendAvg()
main()
