//Israk Ayasin
//This program takes in your goal and monthly expenses. Then calculate them and show you if your saving enough or not
#include<stdio.h>

int main(){
	//These variable takes information from the user and saves and total adds all of them
	float goal, rent, utilities, transport, food, car, total,leftover;
	car=581.99;

	//I am taking all the necessary variables I need from the user
	printf("Enter monthly expense goal (USD): ");
	scanf("%f", &goal);
	printf("Enter rent (USD): ");
	scanf("%f", &rent);
	printf("Enter utilities (USD): ");
	scanf("%f", &utilities);
	printf("Enter transportation (USD): ");
	scanf("%f", &transport);
	printf("Enter food costs (USD): ");
	scanf("%f", &food);
	
	//I am adding all the expences and calculating leftover
	total= car+rent+utilities+transport+food;
	leftover= goal-total;

	//Printing out chart and summary
	printf("\nBudget Chart for Israk:");
	printf("\n%2s%21s%20s\n", "Expense", "Amount $", "Percent %");
    printf("-------------------------------------------------\n");
	printf("%2s%15.2f %18.2f%%\n", "Car Payment", car, car/total*100);
    printf("%2s%22.2f %18.2f%%\n", "Rent", rent, rent/total*100);
    printf("%2s%17.2f %18.2f%%\n", "Utilities", utilities, utilities/total*100);
    printf("%2s%12.2f %17.2f%%\n", "Transportation", transport, transport/total*100);
    printf("%2s%22.2f %18.2f%%\n\n", "Food", food, food/total*100);
	printf("Expense Goal%14.2f\n",goal);
	printf("Total expenses%12.2f\n",total);
	printf("Leftover amount%11.2f\n\n",leftover);
	//Checking if savings are sufficient
	if(leftover>=(goal/5)){
		printf("Good job. You are saving enough!\n");}
	else{
		printf("Try to save more!\n");}

	return 0;
}
