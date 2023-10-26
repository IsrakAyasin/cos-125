#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// Calculates the total sales for each type of gas for the weekend
int* calculateSales(int arr1[], int arr2[], int arr3[]){
    int total; 
    static int result[4];// Array to store the total sales for each day and the weekend
    int matrix1[1][3] = {{3, 4, 5}};
    int matrix2[3][3];
    
    // Populate matrix2 with the daily sales data 
    for (int i = 0; i < 3; i++) {
        matrix2[i][0] = arr1[i];
        matrix2[i][1] = arr2[i];
        matrix2[i][2] = arr3[i];
    }
    int matrix3[1][3];
    for(int i = 0; i < 1; ++i)
	{
		for(int j = 0; j < 3; ++j)
		{
			matrix3[i][j] = 0;
		}
	}

    for (int i = 0; i < 1; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
    for (int i = 0; i < 1; i++) {
        for (int j = 0; j < 3; j++) {
            result[j]=matrix3[i][j];
            total+=matrix3[i][j];
        }
    }
    result[3]=total;

    return result;
}
// Checks if the user input is valid
int isValidInput(char *str) {
    int n = strlen(str);
    if (n < 5) {
        return 0;
    }
    for (int i = 0; i < n; i++) {
        if (str[i] == '#' && i > 0 && i < n - 1) {
            continue;
        }
        if (!isdigit(str[i])) {
            return 0;
        }
    }
    return 1;
}


int main() {
    int* p;
    char day1[30], day2[30], day3[30];
    int day1arr[3], day2arr[3], day3arr[3];
	
    //getting all the information
    printf("Enter daily sales in the format: regular#special#premium\nEnter total gallons of gas sales on Day 1:");
    fgets(day1, sizeof day1, stdin);
    printf("Enter total gallons of gas sales on Day 2:");
    fgets(day2, sizeof day2, stdin);
    printf("Enter total gallons of gas sales on Day 3:");
    fgets(day3, sizeof day3, stdin);

    // if(!isValidInput(day1) || !isValidInput(day2) || !isValidInput(day3)){
    //     printf("Invalid input. Enter again (in the format regular#special#premium): ");
    //     return -1;
    // }
    
    //converting a string to a int and saving it in an array.
    char* token = strtok(day1, "#");
    for (int i = 0; i < 3; i++) {
        day1arr[i] = atoi(token);
        token = strtok(NULL, "#");
    }
    token = strtok(day2, "#");
    for (int i = 0; i < 3; i++) {
        day2arr[i] = atoi(token);
        token = strtok(NULL, "#");
    }
    token = strtok(day3, "#");
    for (int i = 0; i < 3; i++) {
        day3arr[i] = atoi(token);
        token = strtok(NULL, "#");
    }
    
    //printing all the result
    p=calculateSales(day1arr, day2arr, day3arr);
    printf("Total sales on Day 1: $%d\n",*(p));
    printf("Total sales on Day 2: $%d\n",*(p+1));
    printf("Total sales on Day 3: $%d\n",*(p+2));
    printf("Total sales on weekend: $%d\n",*(p+3));
    return 0;
}



