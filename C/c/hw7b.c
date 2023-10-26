//Israk Ayasin
//This is a C program to validate a user’s password and encrypt the password
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// function to test the password is at least eight characters long
int checkLength(int len){
    return(len>=8);
}

// function to test the password has at least one uppercase letter and one lowercase letter
int checkLetter(char pass[]){
    // initialize two flags for uppercase and lowercase letters
    int hasLower=0;
    int hasHigher=0;
    // use strlen to get the number of characters in pass
    for(int i=0; i<strlen(pass); i++){
        // check if the current character is a lowercase letter
        if(islower(pass[i])){
            hasLower=1;
        }
        // check if the current character is an uppercase letter
        if(isupper(pass[i])){
            hasHigher=1;
        }
    }
    return(hasHigher && hasLower);
}

// function to test the password has at least one digit
int checkDigit(char pass[]){
    // initialize a flag for digit
    int hasDigit=0;
    for(int i=0; i<strlen(pass); i++){
        // check if the current character is a digit
        if(isdigit(pass[i])){
            hasDigit=1;
        }
    }
    return hasDigit;
}

// function to test the password has at least one of these four characters: ! @ # $
int checkSpecial(char pass[]){
    // initialize a flag for special character
    int hasSpecial=0;
    for(int i=0; i<strlen(pass); i++){
        // check if the current character is one of the four special characters
        if(pass[i]=='!'||pass[i]=='@'||pass[i]=='#'||pass[i]=='$'){
            hasSpecial=1;
        }
    }
    return hasSpecial;
}

//function to encrypt the valid password
int encrypt(char pass[]){
    for(int i=0; i<strlen(pass); i++){
        if(pass[i]=='!'||pass[i]=='@'||pass[i]=='#'||pass[i]=='$'){
            printf("%c",pass[i]-1);
        }
        else{
            printf("%c",pass[i]+1);
        }
    }
    return 0;
}

int main()
{
    //variable to save the password
    char pass[30];
    printf("Please enter your preferred password:");
    scanf(" %[^\n]%*c", pass);

    if(checkLength(strlen(pass))&&checkLetter(pass)&&checkDigit(pass)&&checkSpecial(pass)){
        printf("Valid Password\nEncrypted password is = ");
        encrypt(pass);
    }
    else{
        printf("Invalid Password\n");
        // print the reasons why the password is invalid
        if(!checkLength(strlen(pass))){
           printf("Reason: your password should contain at least eight characters\n");
        }
        if(!checkLetter(pass)){
            printf("Reason: your password should contain at least one lowercase character and highercase character\n");
        }
        if(!checkDigit(pass)){
            printf("Reason: your password should contain at least one digit\n");
        }
        if(!checkSpecial(pass)){
            printf("Reason: your password should contain at least one of the four special characters “! @ # $”");
        }
    }
    return 0;
}