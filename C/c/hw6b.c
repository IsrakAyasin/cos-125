//Israk Ayasin
//This program output the Fibonacci sequence up to a given number by a user
#include <stdio.h>
int main()
{
    //these variables saves user input, nexterm, first number and second number
    int n, i, t1 = 0, t2 = 1, nextTerm;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    if (n <= 0){
        printf("Invalid input – please try a positive integer.");
        return 0;}
        
    printf("Fibonacci Series: ");
    //going through a for loop and adding first and second number each time
    for (i = 1; i <= n; ++i)
    {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        //break if next term goes over the user input
        if (nextTerm > n)
            break;
    }
    //prints the last value
    printf("%d", t1);
    return 0;
}