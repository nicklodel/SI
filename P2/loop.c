#include <stdio.h>
#include <stdlib.h>
int main(){
    int n=10;
//creating integer of size n.
int *piBuffer = malloc(n * sizeof(int));
//Assigned value to allocated memory
for (int i = 0; i < n; ++i)
{
piBuffer [i] = i * 3;
printf("\n%d\n",piBuffer[i]);
}
}