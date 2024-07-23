#include <stdio.h>
#include <stdlib.h>

#define OFFSET 10000000
#define SIZE 20000001

int main() {
    int n,m;
    int count[SIZE] = {0};

    scanf("%d", &n);
    for (int i=0; i < n; i++) {
        int num;
        scanf("%d", &num);
        count[num + OFFSET]++;
    }

    scanf("%d", &m);
    for (int i=0; i < m; i++) {
        int num;
        scanf("%d", &num);
        printf("%d ", count[num + OFFSET]);
    }

    return 0;    
}