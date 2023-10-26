//Israk Ayasin
//This is a C program to multiply two matrices

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    srand(time(NULL));
    
    //variables to save rows and columns of matrices
    char matrix1Size[30], matrix2Size[30];
    
    // Get the size of matrix
    printf("Enter number of rows and columns of first matrix (format: r x c):");
    fgets(matrix1Size, sizeof(matrix1Size), stdin);
    printf("Enter number of rows and columns of second matrix (format: r x c):");
    fgets(matrix2Size, sizeof(matrix2Size), stdin);
    
    //assigning rows and columns
    int rows1 = (int)matrix1Size[0]-'0';
    int cols1 = (int)matrix1Size[2]-'0';
    int rows2 = (int)matrix2Size[0]-'0';
    int cols2 = (int)matrix2Size[2]-'0';
    int rows3 = rows1;
    int cols3 = cols2;

    //creating the matrises
    int matrix1[rows1][cols1];
    int matrix2[rows2][cols2];
    int matrix3[rows3][cols3];
    
    //checking if we can multiply matrices
    if((cols1==0) || (rows1==0) || (cols2==0) ||(rows2==0)){
        printf("Error: The number of rows or columns of a matrix can’t be 0. Please try again.");
        return 0;
    }
    if(cols1!=rows2){
        printf("Reason: the number of columns of the 1st matrix must equal to the number of rows of the 2nd matrix. Please try again.");
        return 0;
    }
    
    // Generate random numbers for matrix 1 and 2
    for (int i=0; i<rows1; i++){
        for (int j=0; j<cols1; j++){
            matrix1[i][j] = ((rand() % (10)) + 1);
        }
    }
    for (int i=0; i<rows2; i++){
        for (int j=0; j<cols2; j++){
            matrix2[i][j] = ((rand() % (10)) + 1);
        }
    }
    
    // Initialize all elements of third matrix to zero
    for(int i = 0; i < rows3; ++i)
	{
		for(int j = 0; j < cols3; ++j)
		{
			matrix3[i][j] = 0;
		}
	}
	
	// Multiply matrices
    for(int i = 0; i < rows3; i++)
	{
		for(int j = 0; j < cols3; j++)
		{
			for(int k=0; k< cols1; k++)
			{
				matrix3[i][j] += matrix1[i][k] * matrix2[k][j];
			}
		}
	}
    
    //printing all 3 matrix
    printf("\tMatrix A\t\tMatrix B\t\tMatrix C\n");
    for (int i=0; i<rows1 || i<rows2 || i<rows3; i++){
        if (i<rows1){
            printf("\t");
            for (int j=0; j<cols1; j++){
                printf(" %d ",matrix1[i][j]);
            }
        } else {
            printf("\t\t");
        }
        printf("\t.\t");
        if (i<rows2){
            for (int j=0; j<cols2; j++){
                printf(" %d ",matrix2[i][j]);
            }
        } else {
            printf("\t\t");}
        printf("\t=\t");
        if (i<rows3){
            for (int j=0; j<cols2; j++){
                printf(" %d ",matrix3[i][j]);}
        } else {
            printf("\t\t");}
        printf("\n");
    }

return 0;
}
