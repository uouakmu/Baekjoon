#include <stdio.h>
#include <stdlib.h>

#define MAX_N 100000

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int n;
    int s[MAX_N];
    int distances[MAX_N - 1];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &s[i]);
    }
    qsort(s, n, sizeof(int), compare);

    for (int i = 0; i < n - 1; i++) {
        distances[i] = s[i + 1] - s[i];
    }

    int gcd_value = distances[0];
    for (int i = 1; i < n - 1; i++) {
        gcd_value = gcd(gcd_value, distances[i]);
    }

    int required_trees = 0;
    for (int i = 0; i < n - 1; i++) {
        required_trees += (distances[i] / gcd_value) - 1;
    }

    printf("%d\n", required_trees);

    return 0;
}