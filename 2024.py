import random
import tkinter as ath

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
        print("|" + "|".join(f"{v or ' ':4}" for v in ligne) + "|")
    print("+----+----+----+----+")

import random
import tkinter as ath

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
        print("|" + "|".join(f"{v or ' ':4}" for v in ligne) + "|")
    print("+----+----+----+----+")

def deplacer_a_gauche(ligne):
    ligne_sans_zeros = [case for case in ligne if case != 0]
    i = 0
    while i < len(ligne_sans_zeros) - 1:
        if ligne_sans_zeros[i] == ligne_sans_zeros[i + 1]:
            ligne_sans_zeros[i] *= 2
            ligne_sans_zeros[i + 1] = 0
            i += 1
        i += 1
    ligne_apres_fusion = [case for case in ligne_sans_zeros if case != 0]
    while len(ligne_apres_fusion) < len(ligne):
        ligne_apres_fusion.append(0)
    return ligne_apres_fusion

def deplacer_a_droite(ligne):
    ligne_inverse = ligne[::-1]
    ligne_apres_gauche = deplacer_a_gauche(ligne_inverse)
    ligne_finale = ligne_apres_gauche[::-1]
    return ligne_finale

def deplacer_vers_haut(grille):
    grille1 = [list(colonne) for colonne in zip(*grille)]
    grille_move = [deplacer_a_gauche(colonne) for colonne in grille1]
    grille4 = [list(ligne) for ligne in zip(*grille_move)]
    return grille4

def deplacer_vers_bas(grille):
    grille1 = [list(colonne) for colonne in zip(*grille)]
    grille2 = [colonne[::-1] for colonne in grille1]
    grille_move = [deplacer_a_gauche(colonne) for colonne in grille2]
    grille3 = [colonne[::-1] for colonne in grille_move]
    grille4 = [list(ligne) for ligne in zip(*grille3)]
    return grille4

def grille_pleine(grille):
    return all(v != 0 for ligne in grille for v in ligne)

def mouvements_possibles(grille):
    if not grille_pleine(grille):
        return True
    for i in range(4):
        for j in range(4):
            if i < 3 and grille[i][j] == grille[i + 1][j]:
                return True
            if j < 3 and grille[i][j] == grille[i][j + 1]:
                return True
    return False

def test_win(grille):
    return any(v >= 2048 for ligne in grille for v in ligne)

def mettre_a_jour_grille():
    for i in range(4):
        for j in range(4):
            valeur = grille[i][j]
            case = cases[i][j]
            case.config(text=str(valeur) if valeur else "", bg=COULEURS.get(valeur, "#cdc1b4"))

def jouer(direction):
    global grille
    if direction == "↑":
        nouvelle_grille = deplacer_vers_haut(grille)
    elif direction == "↓":
        nouvelle_grille = deplacer_vers_bas(grille)
    elif direction == "←":
        nouvelle_grille = [deplacer_a_gauche(ligne) for ligne in grille]
    elif direction == "→":
        nouvelle_grille = [deplacer_a_droite(ligne) for ligne in grille]

    if nouvelle_grille != grille:
        grille = nouvelle_grille
        ajouter_tuile(grille)
        mettre_a_jour_grille()
        if test_win(grille):
            label_status.config(text="Félicitations, vous avez gagné !", fg="green")
        elif not mouvements_possibles(grille):
            label_status.config(text="Game Over !", fg="red")

COULEURS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}

fenetre = ath.Tk()
fenetre.title("2048 - projet")
grille = creer_grille()
ajouter_tuile(grille)
ajouter_tuile(grille)

cases = [[None for _ in range(4)] for _ in range(4)]
frame_grille = ath.Frame(fenetre, bg="#bbada0", bd=3)
frame_grille.grid(row=0, column=0)
for i in range(4):
    for j in range(4):
        case = ath.Label(frame_grille, text="", width=4, height=2, font=("Helvetica", 24), bg="#cdc1b4", fg="#776e65")
        case.grid(row=i, column=j, padx=5, pady=5)
        cases[i][j] = case

label_status = ath.Label(fenetre, text="Touches : ↑ (haut), ↓ (bas), ← (gauche), → (droite)", font=(12))
label_status.grid(row=1, column=0)

fenetre.bind("<Up>", lambda event: jouer("↑"))
fenetre.bind("<Down>", lambda event: jouer("↓"))
fenetre.bind("<Left>", lambda event: jouer("←"))
fenetre.bind("<Right>", lambda event: jouer("→"))

mettre_a_jour_grille()
fenetre.mainloop()

def fusionner_ligne(ligne):
    ligne = [v for v in ligne if v != 0]
    i = 0
    while i < len(ligne) - 1:
        if ligne[i] == ligne[i + 1]:
            ligne[i] *= 2
            ligne[i + 1] = 0
            i += 1
        i += 1
    ligne = [v for v in ligne if v != 0]
    while len(ligne) < 4:
        ligne.append(0)
    return ligne

def grille_pleine(grille):
    return all(v != 0 for ligne in grille for v in ligne)

def mouvements_possibles(grille):
    if not grille_pleine(grille):
        return True
    for i in range(4):
        for j in range(4):
            if i < 3 and grille[i][j] == grille[i + 1][j]:
                return True
            if j < 3 and grille[i][j] == grille[i][j + 1]:
                return True
    return False

def test_win(grille):
    return any(v >= 2048 for ligne in grille for v in ligne)

def mettre_a_jour_grille():
    for i in range(4):
        for j in range(4):
            valeur = grille[i][j]
            case = cases[i][j]
            case.config(text=str(valeur) if valeur else "", bg=COULEURS.get(valeur, "#cdc1b4"))

def jouer(direction):
    global grille
    if direction == "↑":
        nouvelle_grille = deplacer_haut(grille)
    elif direction == "↓":
        nouvelle_grille = deplacer_bas(grille)
    elif direction == "←":
        nouvelle_grille = deplacer_gauche(grille)
    elif direction == "→":
        nouvelle_grille = deplacer_droite(grille)

    if nouvelle_grille != grille:
        grille = nouvelle_grille
        ajouter_tuile(grille)
        mettre_a_jour_grille()
        if test_win(grille):
            label_status.config(text="Félicitations, vous avez gagné !", fg="green")
        elif not mouvements_possibles(grille):
            label_status.config(text="Game Over !", fg="red")

COULEURS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
}

fenetre = ath.Tk()
fenetre.title("2048 - projet")
grille = creer_grille()
ajouter_tuile(grille)
ajouter_tuile(grille)

cases = [[None for _ in range(4)] for _ in range(4)]
frame_grille = ath.Frame(fenetre, bg="#bbada0", bd=3)
frame_grille.grid(row=0, column=0)
for i in range(4):
    for j in range(4):
        case = ath.Label(frame_grille, text="", width=4, height=2, font=("Helvetica", 24), bg="#cdc1b4", fg="#776e65")
        case.grid(row=i, column=j, padx=5, pady=5)
        cases[i][j] = case

label_status = ath.Label(fenetre, text="Touches : ↑ (haut), ↓ (bas), ← (gauche), → (droite)", font=(12))
label_status.grid(row=1, column=0)

fenetre.bind("<Up>", lambda event: jouer("↑"))
fenetre.bind("<Down>", lambda event: jouer("↓"))
fenetre.bind("<Left>", lambda event: jouer("←"))
fenetre.bind("<Right>", lambda event: jouer("→"))

mettre_a_jour_grille()
fenetre.mainloop()
