#include <stdio.h>

int main()
{
    int a[10];
    int i;

    for (i = 0; i < 10; i += 1) {
        scanf("%d", &a[i]);
    }

    for (i = 0; i < 10; i += 1) {
        if (a[i] % 2 == 0) {
            a[i] = 1;
        }
        else {
            a[i] = -1;
        }
    }

    for (i = 0; i < 10; i += 1) {
        printf("-> %d\n", a[i]);
    }

    return 0;
}