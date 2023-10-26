
#include <stdio.h>
/*
 the header file with the dataset should be inclded as #include "electricity.h"
 note that user defined header files should be included with "" not with <>
 make sure the electricity.h is in the same directory (folder)

 more info: The " " here are used to instruct the preprocessor to look into the working directory (if not found in the current directory, it will look in the standard library directory in gcc). If you are using " " you need to ensure that the header file you created is saved in the same directory in which you will save the C file that uses this header file.
 */
#include "electricity.h"

int main()
{
    // printing the 0,0 element of the electricity 2D array
    printf("%f\n", electricity[0][0]);
    return 0;
}
