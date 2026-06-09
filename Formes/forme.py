from turtle import *

listeForme = {
    "1": "Cercle",
    "2": "Triangle",
    "3": "Carre"
}

listeTaille = {
    "1": "Petit",
    "2": "Moyen",
    "3": "Grand"
}

listeCouleur = {
    "1": "red",
    "2": "blue",
    "3": "green",
    "4": "pink"
}

choixEnCours = True
listeFormeUser = []


while choixEnCours == True:
    
    
    newForme = []
    formeEnCours = True
    while formeEnCours == True :
        for c, desc in listeForme.items():
            print(f"{c}. {desc}")
        choixForme = input(f"Choisissez une de ces formes: {', '.join(listeForme)}: ")
        if choixForme in listeForme :
            newForme.append(int(choixForme))
            formeEnCours = False
        else : print("Choix invalide")
    
    tailleEnCours = True
    while tailleEnCours == True and choixEnCours == True:
        for c, desc in listeTaille.items():
            print(f"{c}. {desc}")
        choixTaille = input(f"Choisissez une de ces taille: {', '.join(listeTaille)}: ")
        if choixTaille in listeTaille :
            newForme.append(int(choixTaille))
            tailleEnCours = False
        else : print("Choix invalide")
    
    couleurEnCours = True
    while couleurEnCours == True and choixEnCours == True:
        for c, desc in listeCouleur.items():
            print(f"{c}. {desc}")
        choixCouleur = input(f"Choisissez une de ces taille: {', '.join(listeCouleur)}: ")
        if choixCouleur in listeCouleur :
            newForme.append(listeCouleur[choixCouleur])
            couleurEnCours = False
        else : print("Choix invalide")
    
    # Ajout de la forme a la liste
    listeFormeUser.append(newForme)
    
    # Ajouter nouvelle forme oui/non avec true ou false selon
    recommencer = True
    while recommencer == True : 
        choixAjouter = input("Voulez-vous ajouter une autre forme? Y/N : ")
        if choixAjouter == 'N': 
            choixEnCours = False
            recommencer = False
        elif choixAjouter == 'Y':
            choixEnCours = True
            recommencer = False

for forme in listeFormeUser :
    
    if (forme[0]== 1) :
        with fill():
            color(forme[2])
            circle(50*forme[1])
    elif (forme[0]== 2) :
        with fill():
            for i in range(3):
                color(forme[2])
                forward(100*forme[1])
                left(120)
    elif (forme[0]== 3) :
        with fill():
            for i in range(4):
                color(forme[2])
                forward(100*forme[1])
                right(90)
                
    penup()
    forward(50)
    pendown()
    
exitonclick()
    
