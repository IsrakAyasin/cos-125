//Israk Ayasin
//This program finds the sum of all even numbers between 1 and n.
#include <stdio.h>
#include <stdlib.h>

int main (){
  //variables to save user input and sum
  int n, sum = 0;
  printf ("Input a number larger than 1: ");
  // Verify if the input is a number
  if (scanf ("%d", &n) != 1){
      printf ("Invalid input\n");
      return 1;}
  // Calculate the sum of all even numbers between 1 and n
  for (int i = 2; i <= n; i += 2){
      sum += i;}
  printf ("Sum of even numbers between 1 and %d: %d\n", n, sum);
  return 0;
}
