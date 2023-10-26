//Israk Ayasin
//Checking whether an alphabet entered by the user is a vowel or a consonant.
#include<stdio.h>

int main(){
	//creating letter char variable to save the letter from the user
	char letter='n';
	
	//loop will keep going until you press #
	while(1){
	printf("Enter a letter: ");
	scanf(" %c", &letter);
	if(letter=='#'){
		break;}
	//checking if the user put a vowel
	else if(letter == 'a' || letter == 'A' || letter == 'o' || letter == 'O' || letter == 'u' || letter == 'U' || letter == 'i' || letter == 'I' || letter == 'e' || letter == 'E'){
		printf("%c is a vowel\n",letter);}
	//checking if it's a constant or not
	else if((letter<='z' && letter>='a')||(letter<='Z' && letter>='A')){
		printf("%c is a constant\n",letter);}
	//if nothing works it's a invalid character
	else{
		printf("%c is not a valid character\n", letter);}
	}
	printf("Good bye!");
	return 0;
}
