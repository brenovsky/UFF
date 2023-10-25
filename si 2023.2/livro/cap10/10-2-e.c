#include <stdio.h>

float maior2(float x, float y)
{
    if (x > y) {
        return x;
    }
    else {
        return y;
    }
}

int main()
{
    float a[10], b[10];
    int i;

    for (i = 0; i < 10; i += 1) {
        scanf("%f", &a[i]);
    }

    float maior = maior2(a[0], a[1]);

    for (i = 2; i < 10; i += 1) {
        maior = maior2(maior, a[i]);
    }

//não terminado
}