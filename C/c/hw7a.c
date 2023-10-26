// Israk Ayasin
// This a C program to generate and save 200 random integers in an array and get highest and lowest value and index
#include <stdio.h>
#include <stdlib.h>

int find_lowest(int list[]) {
    // initialize the lowest index
    int lowest = 0;
    for(int i=0; i<200; i++){
        // compare the current value with the lowest value
        if(list[i]<list[lowest]){
            lowest=i;
        }
    }
    // print the index and value of the lowest number
    printf("Lowest number %d is at index %d",list[lowest],lowest);
    return -1;
}

int find_highest(int list[]) {
     // initialize the highest index
    int highest = 0;
    for(int i=0; i<200; i++){
         // compare the current value with the highest value
        if(list[i]>list[highest]){
            highest=i;}
    }
    // print the index and value of the highest number
    printf("\nhighest number %d is at index %d\n",list[highest],highest);
    return -1;
}

int main() {
    // declare an array of size 200
    int list[200];
    // generate and save 200 random integers between 0 and 999 in the array
    for(int i=0; i<200; i++){
        list[i]=rand()%999;}
       
    find_lowest(list);
    find_highest(list);
    return 0;
}
