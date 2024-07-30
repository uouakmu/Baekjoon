#include <stdio.h>
#include <math.h>

int is_prime(long long x) {
    if (x <= 1) return 0;
    if (x <= 3) return 1;
    if (x % 2 == 0 || x % 3 == 0) return 0;
    for (long long i = 5; i * i <= x; i += 6) {
        if (x % i == 0 || x % (i + 2) == 0) return 0;
    }
    return 1;
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        long long n;
        scanf("%lld", &n);

        if (n <= 1) {
            printf("2\n");
            continue;
        }

        while (!is_prime(n)) {
            n++;
        }
        printf("%lld\n", n);
    }

    return 0;
}