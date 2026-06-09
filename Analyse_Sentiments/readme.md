# Analyse de sentiment

Ce programme permet d'analyser le sentiment exprimé par un utilisateur à partir d'un message texte et de déterminer si celui-ci est plutôt positif ou négatif.

## Méthode utilisée

Pour réaliser cette analyse, le programme s'appuie sur plusieurs listes de mots, termes et expressions associés à des sentiments positifs ou négatifs.

Trois niveaux d'intensité sont définis pour chaque catégorie :

- Intensité forte : ±5 points
- Intensité moyenne : ±3 points
- Intensité faible : ±1 point

Cela représente au total :

- 3 listes de termes positifs
- 3 listes de termes négatifs

## Saisie utilisateur

Le programme demande à l'utilisateur de répondre à la question :

```text
Comment vous sentez-vous aujourd'hui ?
```

La réponse est ensuite analysée afin de détecter la présence des différents termes contenus dans les listes de référence.

## Calcul du score

Pour chaque liste :

1. Le programme parcourt les termes qu'elle contient.
2. Il vérifie si chaque terme est présent dans le message de l'utilisateur.
3. Lorsqu'un terme est détecté, le score correspondant à sa pondération est ajouté (si positif) ou retiré (si négatif) au score total

À la fin de l'analyse, un score totale est obtenu

## Détermination du sentiment

Une fois le score calculé, le programme compare :

- Si le score total est supérieur à 0, le sentiment est considéré comme positif.
- Si le score total est inférieur à 0, le sentiment est considéré comme négatif.
- S'il est égal à 0, le résultat est considéré comme neutre.

## Limites actuelles

### Normalisation du texte

Actuellement, le programme convertit uniquement le message en minuscules avant l'analyse. Et prend en compte les versions masculine et feminine de chaque termes.

Il ne supprime pas encore :

- Les accents
- Les caractères spéciaux
- Certaines variations d'écriture

Cela peut empêcher la détection correcte de certains termes selon la façon dont l'utilisateur rédige son message.

### Chevauchement des termes

Certains mots ou expressions présents dans les différentes listes peuvent se recouper.

Cela peut entraîner :

- L'ajout de plusieurs scores pour une même idée exprimée ;
- La détection simultanée de termes positifs et négatifs dans certains cas ;
- Des résultats parfois moins précis que souhaité.

### Précision de la pondération

Certains mots ou expressions présents dans les différentes listes peuvent ne pas être bien classés dans la bonne liste.
Cela peut entraîner une sous-évaluation ou une sur-estimation du sentiment de l'utilisateur.