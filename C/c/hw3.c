#include <stdio.h>
#include <math.h>

int main(){
	char name[] = "The Z Store";
	float item_1 = 21.45;
	float item_2 = 10.00;
	float item_3 = 14.90;
	float item_4 = 33.50;

	float purchase_1=item_1*2;
	float purchase_2=item_2*2;
	float purchase_3=item_3*2;
	float purchase_4=item_4*2;
	float total=purchase_1+purchase_2+purchase_3+purchase_4;
	float gst=total*.10;
	float allTotal=total+gst;

	printf("Welcome to %s\n\n",name);
	printf("Item1\t\t$%0.2f  *2  $%0.2f\n",item_1,purchase_1);
	printf("Item2\t\t$%0.2f  *2  $%0.2f\n",item_2,purchase_2);
	printf("Item3\t\t$%0.2f  *2  $%0.2f\n",item_3,purchase_3);
	printf("Item4\t\t$%0.2f  *2  $%0.2f\n",item_4,purchase_4);
	printf("\nItem total:\t$%0.2f\n",total);
	printf("\nGST:\t\t$%0.2f\n",gst);
	printf("Total:\t\t$%0.2f\n",allTotal);

	return 0;
}
