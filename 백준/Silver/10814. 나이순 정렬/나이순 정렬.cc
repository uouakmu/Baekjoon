#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int age;
    char name[101];
    int index;
} User;

int compare(const void *a, const void *b) {
    User *userA = (User *)a;
    User *userB = (User *)b;
    if (userA->age == userB->age) {
        return userA->index - userB->index;
    }
    return userA->age - userB->age;
}

int main() {
    int n;
    scanf("%d", &n);

    User *users = (User *)malloc(n * sizeof(User));
    for (int i = 0; i < n; i++) {
        scanf("%d %s", &users[i].age, users[i].name);
        users[i].index = i;
    }

    qsort(users, n, sizeof(User), compare);

    for (int i = 0; i < n; i++) {
        printf("%d %s\n", users[i].age, users[i].name);
    }

    free(users);
    return 0;
}
