#include <stdio.h>

int main()
{
    int idade;

    scanf("%d", &idade);

    if (idade > 60)
    {
        printf("gratuito\n");
    }
    else
    {
        printf("pagante\n");
    }
    
    return 0;
}