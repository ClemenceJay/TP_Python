# Bruitage et débruitage d'image

Ce programme permet de simuler l'ajout de bruit sur une image puis d'appliquer un traitement de débruitage afin d'améliorer sa qualité visuelle.

## Fonctionnement général

Le traitement est divisé en deux étapes :

1. Ajout de bruit sur une image.
2. Débruitage de l'image bruitée.

## Ajout de bruit

Dans un premier temps, le programme charge une image d'origine :

```text
origine.jpg
```

Le programme génère ensuite un bruit gaussien sous la forme d'un nuage de points aléatoires.
Ce bruit est ajouté à l'image d'origine.

L'image bruitée est ensuite sauvegardée sous le nom :

```text
img_noise.jpg
```

## Débruitage de l'image

Pour l'étape de débruitage, le programme charge l'image à traiter :

```text
img_a_debruiter.png
```

Un filtre de lissage est alors appliqué afin de réduire le bruit présent dans l'image.
L'image débruitée est ensuite enregistrée sous le nom :

```text
noise_removed_img.png
```

## Fichiers utilisés

### Images d'entrée

Les images sources doivent être placées dans le dossier :

```text
img/
```

Fichiers utilisés :

```text
img/origine.jpg
img/img_a_debruiter.png
```

### Images générées

Après l'exécution du programme, les images suivantes sont créées dans le même dossier :

```text
img/img_noise.jpg
img/noise_removed_img.png
```

## Résultat attendu

À la fin de l'exécution :

- Une version bruitée de l'image d'origine est générée.
- Une version débruitée de l'image à traiter est créée.
- Les fichiers générés sont automatiquement enregistrés dans le dossier `img`.

## Packages utilisés

- Numpy pour la génération des point gaussiens
- cv2 pour la gestion et le traitement des images
