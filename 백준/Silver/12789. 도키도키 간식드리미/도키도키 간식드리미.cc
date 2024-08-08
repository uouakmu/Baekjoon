#include <stdio.h>

#define MAX_N 1001

int main() {
    int n;
    int line[MAX_N];
    int stack[MAX_N];
    int top = -1;
    int chk = 1;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &line[i]);
    }

    for (int i = 0; i < n; i++) {
        stack[++top] = line[i];
        
        while (top >= 0 && stack[top] == chk) {
            top--;
            chk++;
        }
        
        if (top > 0 && stack[top] > stack[top - 1]) {
            printf("Sad\n");
            return 0;
        }
    }

    if (top >= 0) {
        printf("Sad\n");
    } else {
        printf("Nice\n");
    }

    return 0;
}