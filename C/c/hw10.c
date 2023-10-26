//Israk Ayasin
//This is a C program that reads data from a CSV file named "cars.csv" and stores it in an array of struct named "car". Each row in the CSV file represents a car and contains 7 fields - name, mpg, cyl, hPow, weight, model, and origin. The program then creates an array of struct pointers named "car_ptrs" and assigns each pointer to the address of each struct in the "car" array. The program then sorts the array of struct pointers based on the "mpg" field of each struct using the "qsort" function. Finally, the program prints the name and mpg of the least efficient car and the highest and lowest mpg values.
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define HEADING_ROWS 2 // Define a constant for number of heading rows in the file

// Define a struct to hold car data
struct cars {
    char name[30];
    double mpg;
    int cyl;
    double hPow;
    double weight;
    int model;
    char origin[30];
};

// Function to add data to the struct array
struct cars* add_data(struct cars *car, char *row, int *size) {
    ++*size; // Increase size of the struct array by 1
    if (car == NULL) { // If the struct array is empty
        car = (struct cars*) malloc(*size * sizeof(struct cars)); // Allocate memory for the struct array
    } else { // If the struct array already has data
        car = realloc(car, *size * sizeof(struct cars)); // Reallocate memory for the struct array
    }

    // Split the row string by comma and add data to the struct fields
    char* value = strtok(row, ",");
    strcpy((car+*size-1)->name, value);
    (car+*size-1)->mpg = atof(strtok(NULL, ","));
    (car+*size-1)->cyl = atoi(strtok(NULL, ","));
    (car+*size-1)->hPow = atof(strtok(NULL, ","));
    (car+*size-1)->weight = atof(strtok(NULL, ","));
    (car+*size-1)->model = atoi(strtok(NULL, ","));
    strcpy((car+*size-1)->origin, strtok(NULL, ","));

    return car; // Return the struct array
}

// Function to compare the mpg values of two struct pointers
int compare_mpg(const void *a, const void *b) {
    struct cars *car_a = *(struct cars **)a;
    struct cars *car_b = *(struct cars **)b;
    if (car_a->mpg < car_b->mpg) {
        return -1;
    } else if (car_a->mpg > car_b->mpg) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    // Open the file cars.csv in read only mode
    FILE* fp = fopen("cars.csv", "r");
    int size = 0;
    struct cars *car = NULL;
    if (!fp) { // If there is any file operation error
        printf("Can't open file\n");
    } else {
        // Define a buffer to hold each row temporary
        char buffer[1024];
        // Row number
        int row = 0;

        // Read one line at a time and process
        while (fgets(buffer, 1024, fp)) {
            row++;

            // First two rows do not have data
            if (row <= HEADING_ROWS) {
                continue;
            }

            // Remove newline character at the end of each line
            char *newbuf = strtok(buffer, "\r");
            car = add_data(car, newbuf, &size); // Add data to the struct array
        }

        // Create an array of struct pointers
        struct cars *car_ptrs[size];
        for (int i=0; i<size; i++) {
            car_ptrs[i] = &car[i];
        }

        // Sort the array of struct pointers based on mpg values
        qsort(car_ptrs, size, sizeof(struct cars *), compare_mpg);

        // Print the least and most efficient cars
	    printf("Least efficient car: %s \n MPG: %0.2lf, Cylinders: %d, Horsepower: %0.2lf, Weight: %0.2lf, Model: %d, Origin: %s\n", car_ptrs[0]->name, car_ptrs[0]->mpg, car_ptrs[0]->cyl, car_ptrs[0]->hPow, car_ptrs[0]->weight, car_ptrs[0]->model, car_ptrs[0]->origin);
		printf("\nMost efficient car: %s \n MPG: %0.2lf, Cylinders: %d, Horsepower: %0.2lf, Weight: %0.2lf, Model: %d, Origin: %s\n", car_ptrs[size-1]->name, car_ptrs[size-1]->mpg, car_ptrs[size-1]->cyl, car_ptrs[size-1]->hPow, car_ptrs[size-1]->weight, car_ptrs[size-1]->model, car_ptrs[size-1]->origin);
        // Close the file
        fclose(fp);
    }
    //freeing the memory
    if (car != NULL) {
    free(car);
    car = NULL;
}
    return 0;
}
