//Israk Ayasin
//Making a stack and adding push, pop, and print functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to add an element to the end of the queue
int push(int *queue, int limit, int *size, int num){
    if(*size>=limit){ // If the current size of the queue is at the limit
        printf("overflow: %d\n",queue[0]); // Print an overflow message with the first element of the queue
        for(int i = 0; i<*size-1; i++){ // Shift all the elements of the queue one position to the left
            queue[i]=queue[i+1];  
        }
        queue[*size-1]=num; // Set the last element of the queue to the new element
        return 1;
    }
    else{ // If there is still space in the queue
        queue[*size]=num; // Add the new element to the end of the queue
        ++ *size; // Increment the size of the queue
        printf("Done\n");  
    }
    return 0;
}

// Function to print all the elements of the queue
int print(int *queue, int size){
    for(int i = 0; i<size; i++){ // Iterate through each element of the queue
        printf("%d ",queue[i]); // Print the current element to the console
    }
    return 0;
}

// Main function
int main(int argc, char *argv[]){
    char command[30]; // String to store user input
    int size=0, limit, num; // Variables to keep track of the size of the queue, the maximum size of the queue, and the number to be added to the queue
    
    if(argc==1){ // Check if the user provided a command line argument
        printf("You have to put limit too");
        return -1;
    }
    limit = atoi(argv[1]); // Convert the command line argument to an integer and set it as the maximum size of the queue
    int *queue = malloc(sizeof(int*) * limit); // Create the queue array using malloc
    
    printf("Enter command (push, print, or quit): ");
    fgets(command, sizeof(command), stdin); // Get user input
    
    while(!strstr(command,"quit")){ // Loop until the user enters "quit"
        if(strstr(command,"push")){ // If the user enters "push"
            num=atoi(command+5); // Extract the number to be added to the queue from the user input
            push(queue,limit,&size,num); // Call the push function to add the number to the queue
            printf("Enter command (push, print, or quit): ");
            fgets(command, sizeof(command), stdin); // Get user input
        }
        else if(strstr(command,"print")){ // If the user enters "print"
            print(queue, size); // Call the print function to display the elements of the queue
            printf("\nEnter command (push, print, or quit): ");
            fgets(command, sizeof(command), stdin); // Get user input
        }
        else{ // If the user enters anything else
            printf("Please use correct format\n");
            printf("\nEnter command (push, print, or quit): ");
            fgets(command, sizeof(command), stdin); // Get user input
        }
    }
    free(queue); // Free the memory used by the queue array
    queue = NULL; // Set the pointer to the queue array to NULL
    printf("Successfully exited");
    return 0;
}
