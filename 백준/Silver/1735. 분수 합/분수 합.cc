#include <stdio.h>

int gcd(int a, int b) {
    while (b!=0) {
        int temp = b;
        b = a%b;
        a = temp;
    }
    return a;
}

int main() {
    int u1, u2, d1, d2;

    scanf("%d %d", &u1, &u2);
    scanf("%d %d", &d1, &d2);

    int u3 = u1*d2 + u2*d1;
    int d3 = u2*d2;

    int cd = gcd(u3,d3);

    u3 /= cd;
    d3 /= cd;

    printf("%d %d\n", u3, d3);

    return 0;
}