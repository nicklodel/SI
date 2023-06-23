#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
int N=5;
char buf[N];
char buf2[N-1];
char *q = buf;
char *p = buf2;
    while (*p){
    *q++ = *p++;}

}
