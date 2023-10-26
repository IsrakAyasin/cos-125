//Israk Ayasin
//finding monthly average, maximum and minimum consumption month, highest and lowest consumption year

#include <stdio.h>
#include "electricity.h"

//finding monthly average
void compute_monthly_average(float monthly_average[]) {
    int j;
    float sum;
    int NUM_YEARS=sizeof(electricity)/sizeof(electricity[0]);

    // Calculate the average consumption for each month over all the years
    for (int i = 0; i < 12; i++) {
        sum = 0;
        for (j = 0; j < NUM_YEARS; j++) {
            sum += electricity[j][i];
        }
        monthly_average[i] = sum / NUM_YEARS;
    }
}

//finding maximum and minimum consumption month
void highest_lowest_month(float monthly_average[],int max_min[]) {
    int max_index = 0, min_index = 0;
    float max_value = monthly_average[0];
    float min_value = monthly_average[0];
    
    // Find the index of the month with the highest and lowest average consumption
    for (int i = 1; i < 12; i++) {
        if (monthly_average[i] > max_value) {
            max_value = monthly_average[i];
            max_index = i;
        }
        if (monthly_average[i] < min_value) {
            min_value = monthly_average[i];
            min_index = i;
        }
    }
    max_min[0]=max_index;
    max_min[1]=min_index;
}

//finding totalt consumption for a year
float sum_year_consumption(int year_index) {
    int i;
    float sum = 0;

    // Calculate the total consumption for a given year
    for (i = 0; i < 12; i++) {
        sum += electricity[year_index][i];
    }

    return sum;
}

//finding highest and lowest consumption year
int max_min_consumption_year(int max_min[]) {
    int max_index = 0, min_index = 0;
    float max_value = 0;
    float min_value = 0;
    int NUM_YEARS=sizeof(electricity)/sizeof(electricity[0]);

    // Find the index of the year with the highest and lowest total consumption
    for (int i = 0; i < NUM_YEARS; i++) {
        if (sum_year_consumption(i) > max_value) {
            max_value = sum_year_consumption(i);
            max_index = i;
        }
    }
    
    for (int i = 0; i < NUM_YEARS; i++) {
        if (i == 0 || sum_year_consumption(i) < min_value) {
            min_value = sum_year_consumption(i);
            min_index = i;
        }
    }
    max_min[2]=max_index;
    max_min[3]=min_index;
    return 0;
}

int main() {
    float monthly_average[12];
    int max_min[4];
    compute_monthly_average(monthly_average);
    highest_lowest_month(monthly_average, max_min);
    max_min_consumption_year(max_min);
    
    // Print the results
    printf("Monthly Average Consumption:\n");
    for (int i = 0; i < 12; i++) {
        printf("Month %d: %.2f kW\n", i + 1, monthly_average[i]);
    }
    printf("Highest consumption month: Month %d\n", max_min[0] + 1);
    printf("Lowest consumption month: Month %d\n", max_min[1] + 1);
    printf("Highest consumption year: Year %d\n", max_min[2] + 1);
    printf("Lowest consumption year: Year %d\n", max_min[3] + 1);
    
    return 0;
}