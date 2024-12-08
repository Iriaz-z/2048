print("Hello, World!")
import random

def creer_grille():
    return [[0, 0, 0, 0] for _ in range(4)]

def ajouter_tuile(grille):
    lignes_vides = []
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                lignes_vides.append((i, j))
    if lignes_vides:
        i, j = random.choice(lignes_vides)
        grille[i][j] = random.choice([2, 4])

def afficher_grille(grille):
    for ligne in grille:
        print("+----+----+----+----+")
        print("|" + "|".join(f"{val or ' ':4}" for val in ligne) + "|")
    print("+----+----+----+----+")

#les tests
grille = creer_grille()
ajouter_tuile(grille)
ajouter_tuile(grille)
afficher_grille(grille)

#test sur un autre pc le deposit