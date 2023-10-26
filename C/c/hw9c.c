// Israk Ayasin
// A program to reverse a word or a sentence using dynamic memory allocation for a stack

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
char command[100]; // String to store user input
int count = 1; // Variable to keep track of the size of the stack

printf("Enter a phrase: ");
fgets(command, sizeof(command), stdin); // Get user input
int size = strlen(command); // Get the length of the user input

char *stack = (char *) malloc(sizeof(char) * count); // Allocate memory for the stack
for(int i = 0; i < size; i++) { // Iterate through each character of the user input
    ++count; // Increase the size of the stack by one
    stack = realloc(stack, sizeof(char) * count); // Reallocate memory for the stack
    stack[i] = command[i]; // Push the current character to the top of the stack
}

for(int i = size; i >= 0; i--) { // Iterate through each character of the user input in reverse order
    char ch = *(stack + i - 1); // Pop the top character from the stack
    printf("%c", ch); // Print the popped character to the console
    --count; // Decrease the size of the stack by one
    stack = realloc(stack, sizeof(char) * count); // Reallocate memory for the stack
}
printf("\n");

free(stack); // Free the memory used by the stack
stack = NULL; // Set the pointer to the stack to NULL
return 0;
}



