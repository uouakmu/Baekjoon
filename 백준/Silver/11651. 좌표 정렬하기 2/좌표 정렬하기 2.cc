#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Coordinate;

int compare(const void *a, const void *b){
    Coordinate *cA = (Coordinate *)a;
    Coordinate *cB = (Coordinate *)b;

    if (cA->y == cB->y) {
        return cA->x - cB->x;
    }
    else {
        return cA->y - cB->y;
    }
}

int main() {
    int n;
    scanf("%d",&n);

    Coordinate coordinates[n];
    for (int i=0; i<n; i++) {
        scanf("%d %d", &coordinates[i].x, &coordinates[i].y);
    }

    qsort(coordinates, n ,sizeof(Coordinate), compare);

    for (int i=0; i<n; i++) {
        printf("%d %d\n", coordinates[i].x, coordinates[i].y);
    }
    return 0;
}