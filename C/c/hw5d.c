#include<stdio.h>
//Israk Ayasin
//Calcules cost of candy and toffee with or without discount

int main(){

	//creating necessary varaible to calculate
	char name[30];
	int chocolate, toffee;
	float chocolateWithDis, chocolatePrice, toffeePrice, toffeeWithDis, totalPrice, totalWithDis;

	printf("Enter customer name: ");
	scanf(" %s", name);
	printf("Enter number of chocolate bags: ");
	scanf("%d", &chocolate);
	printf("Enter number of toffee bags: ");
	scanf("%d", &toffee);
	
	//calculating price and price with discount
	chocolatePrice=chocolate*15.5;
	if(chocolate>5){
		chocolateWithDis=chocolatePrice-(chocolatePrice*0.1);}
	else{
		chocolateWithDis=chocolatePrice;}
	toffeePrice=toffee*6.9;
	if(toffee>2){
		toffeeWithDis=toffeePrice-(toffeePrice*0.05);}
	else{
		toffeeWithDis=toffeePrice;}
	totalPrice=toffeeWithDis+chocolateWithDis;
	if(totalPrice>100){
		totalWithDis=totalPrice-(totalPrice*0.1);}
	else{
		totalWithDis=totalPrice;}

	//Printing out all of the information
	printf("\t\tHello %s", name);
	printf("\n\nChocolates \t*%d\t$%0.2f",chocolate,chocolatePrice);
	printf("\n\tafter discount\t$%0.2f",chocolateWithDis);
	printf("\n\nToffee \t\t*%d\t$%0.2f",toffee, toffeePrice);
	printf("\n\tafter discount\t$%0.2f",toffeeWithDis);
	printf("\n\nTotal after discount\t$%0.2f",totalPrice);
	printf("\nafter 10%% discount\t$%0.2f", totalWithDis);
	printf("\n\n\t\tYou owe\t$%0.2f",totalWithDis);
	printf("\n\t\tThank You!\n");
	return 0;
}
