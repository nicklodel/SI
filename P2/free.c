#include <stdio.h>
#include <stdlib.h>
int main(){
int *i = (int*)malloc(sizeof(int));
int j = 0;
*i = 4;
free(i);
/* ...el programa continúa */
*i = j;
printf("%d",*i);
}