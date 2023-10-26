#include<stdio.h>
//Israk Ayasin
//Calculating if two number is same out of three

int main(){

	//createing necessary variables to calculate
	int first_number, second_number, third_number;
	printf("Enter the first number: ");
	scanf("%d", &first_number);
	printf("Enter the second number: ");
        scanf("%d", &second_number);
	printf("Enter the third number: ");
	scanf("%d", &third_number);

	//Comparing between numbers to see if one number came more than once and printing all of that
	if((first_number == second_number) ||(first_number == third_number))	{
		printf("value: %d\n", first_number);}
	else if((second_number == third_number)){
		printf("value: %d\n", second_number);}
	else {
		printf("value: ERROR\n");}

	return 0;
}
