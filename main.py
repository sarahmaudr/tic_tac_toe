print("#############################################################")
print("                    Jeu de Tic Tac Toe")
print("#############################################################")
print() # ligne vide

# Création du plateau
plateau = [" " for _ in range(9)]

def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu actuel dans la console.

    Args: 
        plateau (list): liste de 9 cases représentant le plateau.
    """
    print()
    print(f" {plateau[0]} | {plateau[1]} | {plateau[2]} ")
    print("---+---+---")
    print(f" {plateau[3]} | {plateau[4]} | {plateau[5]} ")
    print("---+---+---")
    print(f" {plateau[6]} | {plateau[7]} | {plateau[8]} ")
    print()


def jouer_un_coup(plateau, joueur):
    """
    Permet à un joueur de jouer un coup valide sur le plateau.

    Vérifie que l'entrée est un nombre entre 0 et 8 et que la case n'est pas déjà occupée.

    Args:
        plateau (list) : plateau de jeu
        joueur (str) : symbole du joueur ("X" ou "O")
    """

    while True:
        choix = input(f"Joueur {joueur}, choisis une position (0 à 8) : ")

        # Vérifier que c'est un nombre
        if not choix.isdigit():
            print("Entrée invalide. Entrez un nombre.")
            continue

        position = int(choix)

        # Vérifier que la position est dans les limites
        if position < 0 or position > 8:
            print("Position hors limites. Choisis entre 0 et 8.")
            continue

        # Vérifier que la case est libre
        if plateau[position] != " ":
            print("Case déjà occupée. Choisis une autre position.")
            continue

        # Coup valide
        plateau[position] = joueur
        break

def verifier_victoire(plateau, joueur):
    """
    Vérifie si le joueur a gagné la partie.

    Args:
        plateau (list): plateau de jeu
        joueur (str): symbole du joueur ("X" ou "O")

    Returns:
        bool: True si le joueur gagne, False sinon
    """
    
    combinaisons_gagnantes = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinaisons_gagnantes:
        if plateau[a] == plateau[b] == plateau[c] == joueur:
            return True

    return False

plateau = [" " for _ in range(9)]
joueur_actuel = "X"

while True:
    afficher_plateau(plateau)
    jouer_un_coup(plateau, joueur_actuel)

    if verifier_victoire(plateau, joueur_actuel):
        afficher_plateau(plateau)
        print(f"Le joueur {joueur_actuel} a gagné !")
        break

    if " " not in plateau:
        afficher_plateau(plateau)
        print("Match nul !")
        break

    # Changer de joueur
    if joueur_actuel == "X":
        joueur_actuel = "O"
    else:
        joueur_actuel = "X"