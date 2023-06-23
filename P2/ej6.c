#include <stdio.h>
int main(void)
{
unsigned int uiData = 2;
int iData = -20;
printf("\n%d\n",uiData+iData);
if(iData + uiData > 6)
{
printf("%s\n", "a+b > 6");
}
else
{
printf("%s\n", "a+b < 6");
}
return 0;
}