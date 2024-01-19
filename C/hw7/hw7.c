#include <stdio.h>

void fibonacci(int limit){
    int first = 0, second = 1, tem=1;
    printf("%d, %d",first, second);
    while ((tem+first) <= limit){
        tem = first + second;
        printf(", %d", tem);
        first=second;
        second=tem;
        }
    printf("\n");
}

int ask(){
    printf("Enter a number: ");
    int limit;
    scanf("%d", &limit);
    return limit;
}

int main() {
    int limit = ask();
    while(limit<1){
        printf("Invalid input – please try a positive integer.\n");
        limit = ask();}
    fibonacci(limit);
    return 0;
}
