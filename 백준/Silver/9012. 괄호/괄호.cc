#include <stdio.h>
#include <string.h>

#define MAX_LEN 51

int check(char *string) {
    int stack = 0;
    for (int i = 0; i < strlen(string); i++) {
        if (string[i] == '(') {
            stack++;
        } else if (string[i] == ')') {
            if (stack > 0) {
                stack--;
            } else {
                return 0;
            }
        }
    }
    return stack == 0;
}

int main() {
    int n;
    scanf("%d", &n);
    char string[MAX_LEN];

    for (int i = 0; i < n; i++) {
        scanf("%s", string);
        if (check(string)) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}