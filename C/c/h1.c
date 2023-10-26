#include<stdio.h>
#include<math.h>

int main(){
	int power, base;
	printf("Input a power between 1-4\n");
	scanf("%d", &power);
	printf("Input a base between 20-30\n");
	scanf("%d", &base);
	
	int result = pow(base, power);
	printf("Answer: %d\n", result);

	return 0;
}
