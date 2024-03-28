#include <stdio.h>
#include <stdlib.h>

struct ponto2d {
    int x;
    int y;
} TPonto;

int main() {

    struct ponto2d p;

    scanf("%d %d", &p.x, &p.y);

    printf("%d %d", p.x, p.y);

    return 0;
}