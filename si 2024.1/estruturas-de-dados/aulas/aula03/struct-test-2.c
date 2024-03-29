#include <stdio.h>
#include <stdlib.h>

typedef struct lista {

    int info;
    struct lista* prox;

} TLista;

void cria_lista(TLista* lista) { //ponteiro aponta para NULL

    lista -> prox = NULL;
}

void insereInicio(TLista* lista, int valor) {// inserir elemento no inicio da lista

    TLista* novo = (TLista*) malloc(sizeof(TLista));

    novo -> info = valor;
    novo -> prox = lista -> prox; //novo prox, aponta para onde o ponteiro 'lista' aponta (começo da lista)

    lista -> prox = novo; //ponteiro do começo aponta para o novo inicio
}

void imprimirLista(TLista* lista) {

    TLista* p = lista -> prox;

    while (p != NULL) {
        printf("%d ", p->info);

        p = p -> prox;
    }
}

int main() {

    int input;
    TLista vetor;

    cria_lista(&vetor);

    do {
        scanf("%d", &input);
        insereInicio(&vetor, input);
    } while(input != 0);

    imprimirLista(&vetor);

    return 0;
}