//Israk Ayasin
//Taking some information and outputting a summary statement
#include<stdio.h>
#include<string.h>
int main(){
	
	//variables needed to make the statement
	char name[30];
	int birthDate;
	float salary;
	
	//taking the name and removing the last letter. So that I don't copy the new line character
	printf("New applicant's name: ");
	fgets(name, sizeof(name), stdin);
	if (name[strlen(name) - 1] == '\n') {
		name[strlen(name) - 1] = '\0';
	}

	printf("Enter applicant's birth year: ");
	scanf("%d", &birthDate);
	printf("Enter monthly salary(USD): ");
	scanf("%f", &salary);

	//printing everything here
	printf("%s is a %d year-old applicant, who requests a monthly salary of $%0.2f.",name, 2023-birthDate, salary);
	return 0;
}
