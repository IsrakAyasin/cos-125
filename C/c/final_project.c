//Israk Ayasin and Camron Rith
//Israk did the display method and statistic_option method and Cam did the main method and the reserve method
//The program is a car park management system that allows users to view the current status of the car park, reserve empty slots, and view the occupancy percentage. The program reads the initial state of the car park from a file, displays a menu for the user to choose options, and performs the corresponding actions based on the user's input.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define Rows 14
#define Columns 9
#define FILENAME "carpark1.txt"
#define MAX_LINE_LENGTH 256

// Function declarations
void display_option(char car_park[][Columns]);
void reserve_option(char car_park[][Columns]);
void statistic_option(char car_park[][Columns]);

int main(){
    char car_park[Rows][Columns];
    FILE* fp = fopen(FILENAME, "r");

    if (fp == NULL) {
        printf("Error opening the file\n");
        return 1;}

    int numLines = 0;
    char buffer[MAX_LINE_LENGTH];
    // Read the car park data from the file
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        buffer[strcspn(buffer, "\n")] = '\0'; // Remove the newline character
        strcpy(car_park[numLines], buffer);
        numLines++;}

    fclose(fp);
    char option;
    while (option != 'Q') {
        printf("Select your choice from the menu:\n");
        printf("Option 1: D to display the current status of the car park\n");
        printf("Option 2: R to reserve an empty slot in the car park\n");
        printf("Option 3: S to display the occupancy percentage of the car park\n");
        printf("Option 4: Q to quit\n");
        printf("Enter your choice: ");
        scanf(" %c", &option);

        if (option == 'D') {
            display_option(car_park);
        }
        else if (option == 'R') {
            reserve_option(car_park);
        }
        else if (option == 'S') {
            statistic_option(car_park);
        }
        else if (option == 'Q') {
            // Save the data to the file before quitting
            // TODO: Add code to save the data to the file

            break;
        }
        else {
            printf("Invalid option. Please try again.\n");
        }
    }
    printf("GOODBYE! SEE YOU SOON.\n");
    return 0;
}

// Function to display the current status of the car park
void display_option(char car_park[][Columns]) {
    printf("Current Car Park Status:\n");
    for (int i = 0; i < Rows; i++) {
        for (int j = 0; j < Columns; j++) {
            printf("%c", car_park[i][j]);
        }
        printf("\n");
    }
    printf("  ABCDEFGH\n");
    for (int i = 0; i < Rows; i++) {
        printf("%d ", i + 1);
        for (int j = 0; j < Columns; j++) {
            printf("%c", car_park[i][j]);
        }
        printf("\n");
    }
}

// Function to reserve an empty slot in the car park
void reserve_option(char car_park[][Columns]) {
    char option;
    int row, column;
    while (1) {
        printf("The closest available slot is 2C. Do you want to reserve it? (y/n)\n");
        printf("Enter 'y' for yes or 'n' for no: ");
        scanf(" %c", &option);
        if (option == 'y') {
            if (car_park[1][2] == 'X') {
                printf("ERROR! Unfortunately, the 2C slot is already occupied.\n");
            }
			else{
				car_park[1][2] = 'X';
				printf("The slot 2C is reserved!\n");
			}
			break;
		}
		else if (option == 'n'){
			printf("Please, enter your preferred empty slot(row column): ");
			scanf("%d", &row);
			scanf(" %d", &column);
			row--;
			column = column -'A';
			if (row < 0 || row >= Rows || column <0 || column >= Columns){
				printf("Error!! Invalid Slot\n");
			}
			else if (car_park[row][column] == 'X'){
				printf("ERROR!! the slot is already occupied.\n");
			}
			else{
				car_park[row][column] = 'X';
				printf("Your selection %d%c is succesfully reserved!\n", row+1, column+'A');
				break;
			}
		}
		else {
			printf("Invalid choice, Please try again\n");
		}
	}
}

// Function to calculate and display the occupancy percentage of the car park
void statistic_option(char car_park[][Columns]) {
    int occupied_slots = 0;
    int total_slots = Rows * Columns;
    float occupancy;
    for (int i = 0; i < Rows; i++) {
        for (int j = 0; j < Columns; j++) {
            if (car_park[i][j] == 'X') {
                occupied_slots++;
            }
        }
    }
    occupancy = (100.0 * occupied_slots) / total_slots;
    printf("Current Occupancy: %.1f%%\n", occupancy);
}
