#include <stdio.h>

int main()
{
    float a, b, c, media;

    scanf("%f%f%f", &a, &b, &c);

    media = (a + b + c) / 3;

    if (media >= 7.0)
    {
        printf("aprovado\n");
    }
    else if (media < 3)
    {
        printf("reprovado\n");
    } 
    else
    {
        printf("prova final\n");
    }

    return 0;
}