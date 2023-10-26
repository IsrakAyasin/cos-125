# File: ayasin_hw6.py
# Author: Israk Ayasin
# Date: 10/27/2022
# Section: 1004-1
# E-mail: israk.ayasin@maine.edu
# Description:
# Creating Matrix
# Collaboration:
# Manuella, Tobias
import random

def main():
    num_vertices=int(input("NUMBER OF VERTICES:"))
    probability_num=float(input("PROBABILITY OF AN EDGE BETWEEN VERTICES:"))
    return num_vertices,probability_num
x,y=main()
def GenerateAdjMatrix(vertices, probability):
    common_list=[]
    matrix=[]
    for i in range(vertices):
        column=[]
        for j in range(vertices):
            random_num=random.random()
            if ([j,i] not in common_list) and random_num<probability and i!=j:
                column.append(1)
                common_list.append([i,j])
            else:
                column.append(0)
        matrix.append(column)
    return matrix


def CreateAdjList(matrix):
    AdjList=[]
    count1=0
    for i in matrix:
        subString=""
        count2=0
        subString=subString+str(count1)+":"
        for j in i:
            if(j==1):
                subString=subString+str(count2)
            count2+=1
        count1+=1
        AdjList.append(subString)
    return AdjList

def PrintAdMatrix():
    print("\nADJACENCY MATRIX:\n")
    matrix=GenerateAdjMatrix(x,y)
    row_header=[]
    for i in range(len(matrix)):
        row_header.append(i)
    matrix = [row_header]+matrix
    column_header=[" "]+row_header
    new_matrix=[[column_header[i]]+matrix[i]for i in range(len(matrix))]
    for i in new_matrix:
        for j in i:
            print(j,end=" ")
        print()
PrintAdMatrix()

def PrintAdjList():
    print("\nADJACENCY LIST:\n")
    for i in CreateAdjList(GenerateAdjMatrix(x,y)):
        for j in i:
            print(j,end=" ")
        print()
PrintAdjList()
