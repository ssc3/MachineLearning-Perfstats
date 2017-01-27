#include "stdio.h"
#include "stdlib.h"
#include "inttypes.h"
#include <time.h>
#define SIZE 10000


int main() {

    uint32_t count = 0;
    uint32_t arr[SIZE];
    uint32_t i;
    srand(time(NULL));

    for(i=0; i<SIZE; i++) {
       arr[i] = i;
       //arr[i] = rand();
    }

    for(i=1; i<SIZE; i++) {
        if (arr[i-1] < arr[i])
            count++;
    }

    printf("Count = %d\n", count);

}
