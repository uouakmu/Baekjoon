#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(int x) {
    if (x <= 1) return false;
    for (int i = 2; i <= sqrt(x); i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    for (int i = m; i <= n; i++) {
        if (is_prime(i)) {
            printf("%d\n", i);
        }
    }
    
    return 0;
}
