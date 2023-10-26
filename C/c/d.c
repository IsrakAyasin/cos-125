#include <stdio.h>
#include "electricity.h"

void compute_monthly_average(float monthly_average[]) {
    int j;
    float sum;
    int NUM_YEARS=sizeof(electricity)/sizeof(electricity[0]);

    for (int i = 0; i < 12; i++) {
        sum = 0;
        for (j = 0; j < NUM_YEARS; j++) {
            sum += electricity[j][i];
        }
        monthly_average[i] = sum / NUM_YEARS;
    }
}

void highest_lowest_month(float monthly_average[],int result[]) {
    int max_index = 0, min_index = 0;
    float max_value = monthly_average[0];
    float min_value = monthly_average[0];
    
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
    result[0]=max_index;
    result[1]=min_index;
}

int main() {
    float monthly_average[12];
    int result[2];
    compute_monthly_average(monthly_average);
    highest_lowest_month(monthly_average, result);

    printf("Monthly Average Consumption:\n");
    for (int i = 0; i < 12; i++) {
        printf("Month %d: %.2f kW\n", i + 1, monthly_average[i]);
    }
    printf("Highest consumption month: Month %d\n", result[0] + 1);
    printf("Lowest consumption month: Month %d\n", result[1] + 1);
    // Uncomment the following lines to print highest and lowest consumption years
    // printf("Lowest consumption year: Year %d\n", lowest_year + 1);
    // printf("Highest consumption year: Year %d\n", highest_year + 1);
    return 0;
}