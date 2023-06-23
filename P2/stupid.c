#include <stdio.h>
int stupid(int a){
    return (a+1) > a;
}

int main(){
    for (int i=1;i<20;i++){
        printf("%d\n",stupid(i));
    }
}