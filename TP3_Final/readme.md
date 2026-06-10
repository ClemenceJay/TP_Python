# TP Cryptanalyse — Automatisation de Brute-Force Stéganographique

## 📖 Contexte du Projet

Ce projet a été réalisé dans le cadre du module **Initiation à la programmation réseau et de sécurité en Python** pour la *Certification de Développeur Full Stack* au sein de l'**IT-Akademy**.

L'objectif principal est de mener une cryptanalyse par force brute afin de retrouver un message secret dissimulé dans une image par stéganographie.

* **Outil de chiffrement d'origine :** [ImageCypher.fr](https://imagecypher.fr/)
* **Fichier cible fourni :** `imagecypher-secret.png`
* **Dictionnaire fourni :** Un tableur Excel (`Codes_possibles.xlsx`) contenant plus de 400 mots de passe potentiels.

*Ce script d'automatisation a été développé avec l'assistance de Gemini.*

---

## 🛠️ Technologies & Dépendances

Le script est conçu pour s'exécuter avec **Python 3.14+** et s'appuie sur deux bibliothèques majeures :

* **Pandas & OpenPyXL :** Pour l'ouverture, l'extraction et le nettoyage des données du fichier Excel.
* **Selenium WebDriver :** Pour piloter le navigateur Chrome, simuler le comportement humain (clics, navigation, saisie de texte) et analyser dynamiquement le comportement du site.

Pour installer les dépendances sur la version Python 3.14, exécutez la commande suivante dans votre terminal :
`python3.14 -m pip install pandas openpyxl selenium`

---

## ⚙️ Fonctionnement et Logique du Code

Le script suit un flux d'exécution séquentiel pour tester le dictionnaire sans intervention humaine :

1. **Extraction et Nettoyage des Clés :** À l'aide de `pandas`, le script charge le fichier Excel. Par défaut, Excel interprète les grands nombres sous forme de décimaux (ex: `9949970239476577.0`). Le code les convertit d'abord en entiers (`Int64`) pour éliminer proprement le `.0`, puis en chaînes de caractères (`str`).
2. **Initialisation de Selenium :** Un navigateur Chrome automatisé s'ouvre et se dirige sur `https://imagecypher.fr/`.
3. **Préparation de la Page :** Le script simule un clic sur l'onglet de décryptage (`#tab-decode`) et injecte l'image chiffrée dans le champ d'upload dédié.
4. **Boucle de Brute-Force :** Le programme itère sur la liste de mots de passe nettoyée. Pour chaque tentative, il vide le champ de texte, écrit le mot de passe actuel et clique sur le bouton "Décoder".
5. **Détection de Réussite :** Plutôt que de recharger ou de scanner tout le code source de la page, le script utilise la propriété `.is_displayed()` de Selenium pour vérifier si l'élément de succès (ou d'erreur) est visible à l'écran. Dès que le message de réussite apparaît, la boucle s'interrompt et affiche le mot de passe valide ainsi que le message secret décrypté dans le terminal.
6. **Gestion des Délais :** Des pauses (`time.sleep()`) sont appliquées entre chaque action pour s'assurer que le site internet a le temps de charger les éléments et d'exécuter ses calculs JavaScript internes.

---

## ⚠️ Points de Vigilance

* **Visibilité des Éléments (DOM) :** Selenium ne peut pas interagir avec des éléments qui ne sont pas visibles ou affichés dans la fenêtre du navigateur. Lors du lancement, **il est nécessaire de scroller manuellement** jusqu'à la zone d'import du fichier pour que Selenium puisse simuler les clics correctement. Si la zone est masquée par l'affichage, le script s'arrêtera avec une erreur.
* **Chemins des Fichiers :** Les chemins de l'image et de l'Excel doivent être configurés selon l'arborescence de votre propre machine.
* **Chemin Absolu Obligatoire :** Pour l'importation de l'image via Selenium (`send_keys`), vous devez impérativement renseigner un **chemin ABSOLU** (ex: `C:/Users/cleme/.../imagecypher-secret.png`) et non un chemin relatif, sans quoi l'envoi du fichier échouera.