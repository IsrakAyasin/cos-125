//Israk Ayasin
//This program shows Average grade, grade letter and total grade
#include<stdio.h>

int main(){

	//I create a bunch of variable to take different grade, name and subject code
	char name[30], code1, code2, code3, code4, grade;
	float grade1, grade2, grade3, grade4;
	printf("Enter the student's name: ");
	fgets(name, sizeof(name), stdin);
	printf("Enter subject code 1 and grade: ");
	scanf(" %c%f",&code1,&grade1);
	printf("Enter subject code 2 and grade: ");
	scanf(" %c%f",&code2,&grade2);
	printf("Enter subject code 3 and grade: ");
	scanf(" %c%f",&code3,&grade3);
	printf("Enter subject code 4 and grade: ");
	scanf(" %c%f",&code4,&grade4);
	
	//I am taking total grade and average grade
	float total = grade1+grade2+grade3+grade4;
	float average = total/4;
	//I am finding grade letter through average grade
	if (average>90){
		grade='A';}
	else if (average>80){
		grade='B';}
	else if (average>70){
		grade='C';}
	else{
		grade='F';}
	
	//I am printing out all the information over here
	printf("\nFinal grades for %s",name);
	printf("Total for %c%c%c%c: %0.2f\n",code1,code2,code3,code4,total);
	printf("Average: %0.2f%% \n",total/4);
	printf("Grade: %c\n",grade);

	return 0;
}
