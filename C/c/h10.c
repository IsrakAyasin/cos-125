#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER 1024
#define headers 2

struct car {
    char name[40];
    double mpg;
    int cylinders;
    double horsepower;
    double weight;
    int model;
    char origin[40];
};

int main(void) {
    char row[BUFFER];
    int index, size;
    int greatest_index = 0, lowest_index = 0;
    double greatest_efficiency = 0, lowest_efficiency = BUFFER;

    index = 0;
    size = 0;

    FILE *fPointer;
    struct car *cars = malloc(sizeof(struct car) * BUFFER);

    fPointer = fopen("cars.csv", "r");

    if (!fPointer) {
        printf("Error in file: \n");
    }
    else {
        while (fgets(row, BUFFER, fPointer)) {
            size++;
            
            if (size <= headers) {
                continue;
            }
            else {
                char *newbuf = strtok(row, "\r");
                char *token = strtok(newbuf, ",");
                while (token) {
                    switch(index)
                    {
                        case 0:
                            strcpy(cars[size-headers-1].name, token);
                            break;
                        case 1:
                            cars[size-headers-1].mpg = atof(token);
                            if (cars[size-headers-1].mpg > greatest_efficiency) {
                                greatest_efficiency = cars[size-headers-1].mpg;
                                greatest_index = size-headers-1;
                            }
					
                            if (cars[size-headers-1].mpg < lowest_efficiency) {
                                lowest_efficiency = cars[size-headers-1].mpg;
                                lowest_index = size-headers-1;
                            }
                            break;
                        case 2:
                            cars[size-headers-1].cylinders = atoi(token);
                            break;
                        case 3:
                            cars[size-headers-1].horsepower = atof(token);
                            break;
                        case 4:
                            cars[size-headers-1].weight = atof(token);
                            break;
                        case 5:
                            cars[size-headers-1].model = atoi(token);
                            break;
                        default:
                            strcpy(cars[size-headers-1].origin, token);
                            break;
                    }

                    token = strtok(NULL, ",");
                    index++;
                }
                index = 0;
            }
        }
    }

    free(cars);
    cars = NULL;
    fclose(fPointer);
    return 0;
}
