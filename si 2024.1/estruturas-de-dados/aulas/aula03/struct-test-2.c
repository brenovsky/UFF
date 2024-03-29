#include <stdio.h>
#include <stdlib.h>

typedef struct lista {
    int info;
    struct lista* prox;
} TLista;

TLista* cria_lista() { //o ponteiro vai apontar pra null
    return NULL;
}

TLista* insere_inicio(TLista* li, int i) { //nao entendi esses parametros

    TLista* novo = (TLista*) malloc(sizeof(TLista)); //criei a lista nova

    novo -> info = i; //receber a informação
    novo -> prox = li; //li só aponta pro inicio do vetor

    return novo;

}

int main() {


    return 0;
}