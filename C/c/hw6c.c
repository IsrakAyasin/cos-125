//Israk Ayasin

#include <stdio.h>

int printNaturalNumbers(int n);
int printReverseNaturalNumbers(int n);
int printEvenNumbers(int n);
int printOddNumbers(int n);
int sumNaturalNumbers(int n);

int main()
{
//variables needed to save user input and sum
    int n, sum;
    printf("Enter an integer larger than 10: ");
    scanf("%d", &n);
    if (n <= 10)
    {
        printf("Invalid input – please try an integer larger than 10.");
        return 0;
    }
    printf("Natural numbers from 1 to %d: %d\n", n, printNaturalNumbers(n));
    printf("Natural numbers from %d to 1: %d\n", n, printReverseNaturalNumbers(n));
    printf("Even numbers between 1 and %d: %d\n", n, printEvenNumbers(n));
    printf("Odd numbers between 1 and %d: %d\n", n, printOddNumbers(n));
    sum = sumNaturalNumbers(n);
    printf("Sum of natural numbers between 1 and %d: %d", n, sum);
    return 0;
}

//this function just prints all the numbers
int printNaturalNumbers(int n)
{
    int i;
    for (i = 1; i <= n; ++i)
    {
        printf("%d ", i);
    }
    return 0;
}

//this function print in reverse
int printReverseNaturalNumbers(int n)
{
    int i;
    for (i = n; i >= 1; --i)
    {
        printf("%d ", i);
    }
    return 0;
}

//this function only prints even numbers
int printEvenNumbers(int n)
{
    int i;
    for (i = 2; i <= n; i += 2)
    {
        printf("%d ", i);
    }
    return 0;
}

//this function only prints odd numbers
int printOddNumbers(int n)
{
    int i;
    for (i = 1; i <= n; i += 2)
    {
        printf("%d ", i);
    }
    return 0;
}

//this function only returns the sum
int sumNaturalNumbers(int n)
{
    int i, sum = 0;
    for (i = 1; i <= n; ++i)
    {
        sum += i;
    }
    return sum;
}