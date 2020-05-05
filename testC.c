#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{

    int tab[100], taille, i, j, valeur;
	int trouver = -1;


	printf("Saisir le nombre d'élement du tableau \n");
	scanf("%d", &taille);
	printf("Saisir vos valeurs \n");
	for (i=0; i<taille; i++){
        scanf("%d", &tab[i]);
	};
    printf("Donner la valeur à chercher \n");
    scanf("%d", &valeur);
    for (j = 0; (j<taille) && (trouver == -1); j++){
        if (valeur == tab[j]){
            trouver = j;
        };
    };
	printf("La position de l'élément %d est %d \n", valeur, trouver);
	return 0;

}