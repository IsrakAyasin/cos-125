/*
 * COMPLETE THIS CODE SKELETON TO PRINT ARRAY ELEMENTS.
 * You were given an int array and three different kinds of pointers.
 * Your task is to print the array elements (from the original array) using different array notations
 * Different array notations are:
 *
 //int myList[10]; // an array
 //int *myList; // a pointer
 //int *myList[10]; // an array of pointers
 //int (*myList)[10]; // a pointer to an array
 *
 */

#include<stdio.h>
#include<stdlib.h>

// iArray is an array pointer - a pointer pointing to the whole array
void print_array_pointer(int (*iArray)[])
{
    	printf("\n############ print_array_pointer ###############\n");
    	//for (int i = 0; i < 10; i++)
    
}

// iArray is an array of pointers (each element is a pointer to an array element)
void print_pointer_array(int **iArray)
{
    	printf("\n############ print_array_of_pointers ###############\n");
    	//for (int i = 0; i < 10; i++)
    
}

// iArray is a pointer to the original array
void print_pointer_notation(int *iArray)
{
    	printf("\n############ print_pointer_notation ###############\n");
    	for (int i = 0; i < 10; i++)
    		printf("%d", *(iArray+i));
}

// iArray: original array
void print_array_notation(int iArray[])
{

    	printf("\n############ print_array_notation ###############\n");
    	for (int i = 0; i < 10; i++)
    		printf("%d", iArray[i]);
}

int main()
{

    	int myList[10] = {0}; // an array
    	int *ip_myList; // a pointer
    	int *ip_arr_myList[10]; // an array of pointers
    	int (*arr_p_myList)[10]; // a pointer to an array
   	 
    	// fill the array
    	for (int i = 0; i < 10; i++) {
        	myList[i] = rand() % 10;
    	}
    
    	// COMPLETE HERE
	print_array_notation(myList);
    	print_pointer_notation(myList);
    
    	printf("\n");
    	return 0;
}
