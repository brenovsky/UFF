#include <stdio.h>

int chamadas = 0;

void hanoi(int n, char O, char T, char D)
{
    chamadas++;
    if (n == 1) {
        printf("Disco 1: %c -> %c", O, D);
    }

    hanoi(n - 1, O, T, D);
    printf("\n Disco %d: %c -> %c", O, D);
    hanoi(n - 1, T, D, O);
}

int main()
{
    int n; //numero de discos

    scanf("%d", &n);

    hanoi(n, 'O', 'D', 'T'); // origem, destino, trabalho

    printf("\n\n%d\n\n", chamadas);

    return 0;
}
