#include<stdio.h>

int main(){
    FILE* fp = fopen("something.txt", "r");
    FILE* fp2 = fopen("ans.txt", "w+");

    int ch = fgets(fp)

    while(ch != EOF){
        if(ch==' '){
            fputc('#',fp2);
        }
        else if(ch=='\n'){
            fputc(ch, fp2);
        }
        else{
            fputc('x', fp2);
        }
        ch=fgets(fp)
    }

    return 0;
}