//Israk Ayasin
//This program read a student’s name and three grades. Arranges the three grades in ascending order and displays the student’s name, grades in ascending order, and the average

#include <stdio.h>

void swap(int *x, int *y);
void rank_student_grades(int *num1, int *num2, int *num3);
float calculate_average(int g1, int g2, int g3);

int main()
{
    //varables to save name and grades
    char name[20];
    int g1, g2, g3;
    // read name and three grades
    printf("Enter student's name: ");
    scanf(" %[^\n]%*c", name);
    printf("Enter student's first grade: ");
    scanf("%d", &g1);
    printf("Enter student's second grade: ");
    scanf("%d", &g2);
    printf("Enter student's third grade: ");
    scanf("%d", &g3);
    //printing the original grades and ordered grades
    printf("Original grades: %s %d %d %d\n", name, g1, g2, g3);
    rank_student_grades(&g1, &g2, &g3);
    printf("Ordered grades:  %s %d %d %d %.2f\n", name, g1, g2, g3, calculate_average(g1, g2, g3));
    return 0;
}

//change the values in num1, num2, and num3 in ascending order
void rank_student_grades(int *num1, int *num2, int *num3)
{
    if (*num1 > *num2)
    {
        swap(num1, num2);
    }
    if (*num1 > *num3)
    {
        swap(num1, num3);
    }
    if (*num2 > *num3)
    {
        swap(num2, num3);
    }
    return;
}

//swap the values by reference
void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
    return;
}

//calculate the average of three grades
float calculate_average(int g1, int g2, int g3)
{
    float average = (g1 + g2 + g3) / 3.0;
    return average;
}