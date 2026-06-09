
# Fonctionnement du programme

Ce programme permet à l'utilisateur de générer plusieurs formes géométriques personnalisées à l'aide de la bibliothèque **Turtle Graphics**.

## Choix de l'utilisateur

L'utilisateur peut créer autant de formes qu'il le souhaite. Pour chaque forme, il sélectionne :

- Le type de forme :
  - Carré
  - Cercle
  - Triangle
- La taille :
  - Petite (1)
  - Moyenne (2)
  - Grande (3)
- La couleur :
  - Bleu
  - Vert
  - Rose
  - Rouge

## Stockage des données

Chaque forme est représentée par une liste contenant les trois informations suivantes :

```python
[forme, taille, couleur]
```

L'ensemble des formes demandées par l'utilisateur est ensuite stocké dans une liste principale.

## Génération des formes

Le programme parcourt la liste des formes à l'aide d'une boucle. Pour chaque élément :

1. Il identifie le type de forme à dessiner.
2. Il applique la taille sélectionnée. (En réalité, on multiplie simplement la taille par défaut par le coefficient selectionné par l'utilisateur)
3. Il applique la couleur choisie.
4. Il dessine la forme correspondante grâce à **Turtle Graphics**.

## Positionnement des formes

Après le dessin de chaque forme, la position du curseur est déplacée afin d'éviter que les différentes formes ne se superposent complètement. Cela permet une meilleure visualisation de l'ensemble des formes générées.