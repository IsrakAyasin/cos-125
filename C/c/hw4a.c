//Israk Ayasin
//This program takes in fahrenheit and converts it to celcius
#include<stdio.h>

int main(){
	printf("Enter tempearature in Fahrenheit = ");
	//variable for fahrenheit and taking in fahrenheit from the user
	float fahr;
	scanf("%f", &fahr);
	//It computes fahrenheit to celcius
	printf("Temperature in Celsius = %0.3f c\n", ((fahr-32)/1.8));

	return 0;
}
