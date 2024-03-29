import operator
from platform import system
import re

field = []

def b26(a):
    # Convertit un nombre de base 10 en base 26 (alphabet)
    b = 26
    l = []
    while a/b != 0 :
        l.append(65 + int(a%b))
        a = int(a/b)
    l.reverse()
    if l == []:
        l.append(65 + 0)
    return l




def print65(l):
    # Permet d'afficher une lettre a partir du numéro de la table ASCII
    print(" ", end='')
    for i in range(0, len(l)):
        print(chr(l[i]), end='')
    print(" ", end='')





def print90(s):
    # Permet de retourner une lettre a partir du numéro de la table ASCII
    l = b26(s)
    r = ""
    for i in range(0, len(l)):
        r += chr(l[i])
    return r




def b92(a):
    # Permet d'afficher le nombre de lettres dans l'ordre croissant
    curros = system()
    if curros == "Darwin":
        print(" ", end='')
    print("  ", end='')
    for i in range(0, a):
        print65(b26(i))




def place(x, y, player):
    # Place le pion aux coordonnées (x, y)
    field[x][y] = player



def initField(x, y):
    # Prépare le terrain avec la taille souhaitée et place les pions de départ
    field.clear()
    if x < 0 or y < 0:
        x = 8
        y = 8
    for i in range(0, x):
        field.append([])
        for s in range(0, y):
            field[i].append(-1)
    
    place(int((len(field)-1)/2), int((len(field[len(field)-1])-1)/2), 0)
    place(int(((len(field)-1)/2)+1), int(((len(field[len(field)-1])-1)/2)+1), 0)
    place(int(((len(field)-1)/2)+1), int(((len(field[len(field)-1])-1)/2)), 1)
    place(int(((len(field)-1)/2)), int(((len(field[len(field)-1])-1)/2)+1), 1)
            






def printField():
    # Permet d'afficher le tableau sous une forme lisible pour l'utilisateur
    b92(len(field[0]))
    print("")
    curros = system()
    sorruc = 0
    if curros == "Darwin":
        for line in field:
            sorruc += 1
            if sorruc < 10:
                print("", end=' ')
            print(sorruc, end=' ')
            for s in range(0, len(line)):
                if line[s] == -1:
                    print("❇️", end=' ')
                elif line[s] == 0:
                    print("⚫️", end=' ')
                elif line[s] == 1:
                    print("⚪️", end=' ')
            print("")
    else:
        for line in field:
            sorruc += 1
            if sorruc < 10:
                print("", end=' ')
            print(sorruc, end='')
            for s in range(0, len(line)):
                if line[s] == -1:
                    print("❇️ ", end=' ')
                elif line[s] == 0:
                    print("⚫️ ", end=' ')
                elif line[s] == 1:
                    print("⚪️ ", end=' ')
            print("")





def cvToBool(arg):
    # Permet de convertir un entier vers un booléen (vrai ou faux)
    if arg == 1:
        return True
    else:
        return False




def cvToInt(arg):
    # Permet de convertir un booléen en entier
    if arg == True:
        return 1
    else:
        return 0




def placePion(x, y, player):
    # Permet de vérifier si les coordonnées entrées sont justes, de placer le pion et d'absorber le pion adverse
    if x > len(field)-1 or y > len(field[0])-1 or x < 0 or y < 0:
        print("Vous ne pouvez pas jouer en dehors du terrain.")
        return 1
    if field[x][y] != -1:
        print("Vous ne pouvez pas jouer sur une case déjà occupée.")
        return 2
        
    curplay = cvToBool(player)
        
    valueToReturn = -1
    
    # DIAGONALE BAS DROTE
    if x+2 < len(field) and y+2 < len(field[x]):
        if cvToBool(field[x+1][y+1]) == operator.not_(curplay) and cvToBool(field[x+2][y+2]) == curplay and field[x+1][y+1] != -1 and field[x+2][y+2] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x+1, y+1, player)
    # LIGNE BAS
    if x+2 < len(field):
        if cvToBool(field[x+1][y]) == operator.not_(curplay) and cvToBool(field[x+2][y]) == curplay and field[x+1][y] != -1 and field[x+2][y] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x+1, y, player)
    # DIAGONALE BAS GAUCHE
    if x+2 < len(field) and y-2 >= 0:
        if cvToBool(field[x+1][y-1]) == operator.not_(curplay) and cvToBool(field[x+2][y-2]) == curplay and field[x+1][y-1] != -1 and field[x+2][y-2] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x+1, y-1, player)
    # DIAGONALE HAUTE DROITE
    if y+2 < len(field[x]) and x-2 >= 0:
        if cvToBool(field[x-1][y+1]) == operator.not_(curplay) and cvToBool(field[x-2][y+2]) == curplay and field[x-1][y+1] != -1 and field[x-2][y+2] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x-1, y+1, player)
    # COLONNE DROITE
    if y+2 < len(field[x]):
        if cvToBool(field[x][y+1]) == operator.not_(curplay) and cvToBool(field[x][y+2]) == curplay and field[x][y+1] != -1 and field[x][y+2] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x, y+1, player)
    
    # LIGNE VERS LE HAUT
    if x-2 >= 0:
        if cvToBool(field[x-1][y]) == operator.not_(curplay) and cvToBool(field[x-2][y]) == curplay and field[x-1][y] != -1 and field[x-2][y] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x-1, y, player)
    # COLONNE GAUCHE
    if y-2 >= 0:
        if cvToBool(field[x][y-1]) == operator.not_(curplay) and cvToBool(field[x][y-2]) == curplay and field[x][y-1] != -1 and field[x][y-2] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x, y-1, player)
    # DIAGONALE HAUTE GAUCHE
    if x-2 >= 0 and y-2 >= 0:
        if cvToBool(field[x-1][y-1]) == operator.not_(curplay) and cvToBool(field[x-2][y-2]) == curplay and field[x-1][y-1] != -1 and field[x-2][y-2] != -1:
            valueToReturn = 0
            place(x, y, player)
            place(x-1, y-1, player)
    
    return valueToReturn
        



def playerCheck(player):
    # Vérification de la possibilité de jouer pour l'utilisateur
    curplay = cvToBool(player)
    valueToReturn = -1                                
    for x in range(0, len(field)):
        for y in range(0, len(field[x])):
            if field[x][y] == -1:
                # DIAGONALE BAS DROTE
                if x+2 < len(field) and y+2 < len(field[x]):
                    if cvToBool(field[x+1][y+1]) == operator.not_(curplay) and cvToBool(field[x+2][y+2]) == curplay and field[x+1][y+1] != -1 and field[x+2][y+2] != -1:
                        valueToReturn = 0
                # LIGNE BAS
                if x+2 < len(field):
                    if cvToBool(field[x+1][y]) == operator.not_(curplay) and cvToBool(field[x+2][y]) == curplay and field[x+1][y] != -1 and field[x+2][y] != -1:
                        valueToReturn = 0
                # DIAGONALE BAS GAUCHE
                if x+2 < len(field) and y-2 >= 0:
                    if cvToBool(field[x+1][y-1]) == operator.not_(curplay) and cvToBool(field[x+2][y-2]) == curplay and field[x+1][y-1] != -1 and field[x+2][y-2] != -1:
                        valueToReturn = 0
                # DIAGONALE HAUTE DROITE
                if y+2 < len(field[x]) and x-2 >= 0:
                    if cvToBool(field[x-1][y+1]) == operator.not_(curplay) and cvToBool(field[x-2][y+2]) == curplay and field[x-1][y+1] != -1 and field[x-2][y+2] != -1:
                        valueToReturn = 0
                # COLONNE DROITE
                if y+2 < len(field[x]):
                    if cvToBool(field[x][y+1]) == operator.not_(curplay) and cvToBool(field[x][y+2]) == curplay and field[x][y+1] != -1 and field[x][y+2] != -1:
                        valueToReturn = 0      
                # LIGNE VERS LE HAUT
                if x-2 >= 0:
                    if cvToBool(field[x-1][y]) == operator.not_(curplay) and cvToBool(field[x-2][y]) == curplay and field[x-1][y] != -1 and field[x-2][y] != -1:
                        valueToReturn = 0
                # COLONNE GAUCHE
                if y-2 >= 0:
                    if cvToBool(field[x][y-1]) == operator.not_(curplay) and cvToBool(field[x][y-2]) == curplay and field[x][y-1] != -1 and field[x][y-2] != -1:
                        valueToReturn = 0
                # DIAGONALE HAUTE GAUCHE
                if x-2 >= 0 and y-2 >= 0:
                    if cvToBool(field[x-1][y-1]) == operator.not_(curplay) and cvToBool(field[x-2][y-2]) == curplay and field[x-1][y-1] != -1 and field[x-2][y-2] != -1:
                        valueToReturn = 0
                
    return valueToReturn



def letterToNumber(letter):
    # Permet de convertir une lettre en base 10
    newletter = list(letter)
    converted = []
    for chr in newletter:
        converted.append(int(ord(chr)) - 65)
    converted.reverse()
    sum = 0
    for i in range(0, len(converted)):
        sum += converted[i] * 26**i
    return sum


def listeCoup(player):
    # Donne la liste des coups valides
    curplay = cvToBool(player)
    valueToReturn = -1                                
    for x in range(0, len(field)):
        for y in range(0, len(field[x])):
            if field[x][y] == -1:
                # DIAGONALE BAS DROTE
                if x+2 < len(field) and y+2 < len(field[x]):
                    if cvToBool(field[x+1][y+1]) == operator.not_(curplay) and cvToBool(field[x+2][y+2]) == curplay and field[x+1][y+1] != -1 and field[x+2][y+2] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # LIGNE BAS
                if x+2 < len(field):
                    if cvToBool(field[x+1][y]) == operator.not_(curplay) and cvToBool(field[x+2][y]) == curplay and field[x+1][y] != -1 and field[x+2][y] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # DIAGONALE BAS GAUCHE
                if x+2 < len(field) and y-2 >= 0:
                    if cvToBool(field[x+1][y-1]) == operator.not_(curplay) and cvToBool(field[x+2][y-2]) == curplay and field[x+1][y-1] != -1 and field[x+2][y-2] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # DIAGONALE HAUTE DROITE
                if y+2 < len(field[x]) and x-2 >= 0:
                    if cvToBool(field[x-1][y+1]) == operator.not_(curplay) and cvToBool(field[x-2][y+2]) == curplay and field[x-1][y+1] != -1 and field[x-2][y+2] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # COLONNE DROITE
                if y+2 < len(field[x]):
                    if cvToBool(field[x][y+1]) == operator.not_(curplay) and cvToBool(field[x][y+2]) == curplay and field[x][y+1] != -1 and field[x][y+2] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # LIGNE VERS LE HAUT
                if x-2 >= 0:
                    if cvToBool(field[x-1][y]) == operator.not_(curplay) and cvToBool(field[x-2][y]) == curplay and field[x-1][y] != -1 and field[x-2][y] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # COLONNE GAUCHE
                if y-2 >= 0:
                    if cvToBool(field[x][y-1]) == operator.not_(curplay) and cvToBool(field[x][y-2]) == curplay and field[x][y-1] != -1 and field[x][y-2] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                # DIAGONALE HAUTE GAUCHE
                if x-2 >= 0 and y-2 >= 0:
                    if cvToBool(field[x-1][y-1]) == operator.not_(curplay) and cvToBool(field[x-2][y-2]) == curplay and field[x-1][y-1] != -1 and field[x-2][y-2] != -1:
                        valueToReturn = 0
                        print("Vous pouvez jouer en " + str(print90(y)) + str(x+1))
                
                
    return valueToReturn



def mainMenu():
    # Menu principal
    chooser = input("Bienvenue.\n\nD: Démarrer une partie\nR: Règles du jeu\nQ: Quitter\n\nChoix: ")
    if chooser == "D" or chooser == "d":
        startGame()
    elif chooser == "R" or chooser == "r":
        print("Le jeu Black&White est simple. Deux adversaires s'affrontent sur un terrain de taille choisie (habituellement 8x8). L'un d'entre eux est blanc, l'autre noir. En encadrant un pion de la couleur adverse dans n'importe quelle direction (haut/bas, gauche/droite et diagonales), le pion adverse encerclé se retourne pour prendre la couleur du joueur. La partie continue jusqu'au remplissage du terrain, élimination, blocage mutuel ou abandon. Le gagnant est le joueur dont la couleur sera dominante sur le terrain à la fin de la partie. A tout moment, vous disposez d'un assistant vous proposant les coups valides (plus les coups apparaissent, le mieux ils sont) ainsi que d'un droit de passage de tour.\n")
        mainMenu()
    elif chooser == "Q" or chooser == "q":
        print("\n")
        return
    else:
        print("Erreur de lecture. Veuillez réessayer.")
        mainMenu()


def count():
    # Permet de compter le nombre de pions noirs et blancs
    black = 0
    white = 0
    for i in range(0, len(field)):
        for s in range(0, len(field[i])):
            if field[i][s] == 0:
                black += 1
            elif field[i][s] == 1:
                white += 1
    return [black, white]


def winner(abandon = False):
    # Permet de déterminer le gagnant de la partie et d'annoncer la manière à laquelle la partie s'est terminée
    counter = count()
    black = counter[0]
    white = counter[1]
    
    printField()
    
    if abandon == True:
        print("Fin de partie par abandon.")
    elif black + white == len(field) * len(field[0]):
        print("Fin de partie par remplissage de terrain.")
    elif black == 0 or white == 0:
        print("Fin de partie par élimination.")
    else:
        print("Fin de partie par blocage mutuel.")
    
    
    if black > white:
        print("Bravo joueur noir, vous avez gagné !\n")
    elif black < white:
        print("Bravo joueur blanc, vous avez gagné !\n")
    else:
        print("Fin de partie, égalité !\n")
                
    mainMenu()


def game(player, turn = 1):
    # Permet d'annoncer le nombre de tour, d'afficher le nombre de pions, de permetre au joueur de choisir son action et de déterminer si les deux joueurs peuvent jouer (fonction principale du jeu)
    print("\n\nTour", turn)
    notPlayer = cvToInt(operator.not_(cvToBool(player)))

    if playerCheck(player) == 0:
        if player == 0:
            print("Joueur noir, c'est à vous. Vous pouvez jouer.")
        else:
            print("Joueur blanc, c'est à vous. Vous pouvez jouer.")
        
        printField()
        counter = count()
        print("Il y a", counter[0], "pions noirs et", counter[1], "pions blancs sur le terrain.")
        verified = 0
        while verified == 0:
            request = input("Saisissez les coordonnées sous la forme A1 (P: passer son tour, A: abandonner, S: spoiler [AIDE]): ")
            request = request.upper()
            if request == "P":
                verified = 1
            elif request == "S":
                listeCoup(player)
            elif request == "A":
                verified = 1
                winner(True)
                return
            else:
                try:
                    spl = re.split('(\d+)', request)
                    # Requete REGEX pour séparer les lettres des nombres (d+ -> au moins un chiffre pour faire la séparation)
                    x = int(spl[1]) - 1
                    y = letterToNumber(spl[0])
                    result = placePion(x, y, player)
                    if result == 0:
                        verified = 1
                    elif result == -1:
                        print("Coup non-autorisé. Aucun pion n'a été absorbé.")
                except:
                    print("Une erreur s'est produite lors de la lecture des coordonnées.")
                
        game(notPlayer, turn+1)
    else:
        if playerCheck(notPlayer) == 0:
            if player == 0:
                print("Joueur noir, vous ne pouvez pas jouer.")
            else:
                print("Joueur blanc, vous ne pouvez pas jouer.")
                
            game(notPlayer, turn+1)
        else:
            print("Aucun des deux joueurs ne peut jouer.")
            winner()


def startGame():
    # Permet de créer le tableau avec la taille voulue par l'utilisateur et de démarrer la partie
    try:
        ins = input("Donnez la taille de terrain au format \"8x8\" (minimum 6x6): ")
        ins = ins.split("x")
        x = int(ins[0])
        y = int(ins[1])
        if x < 6:
            x = 6
        if y < 6:
            y = 6
    except:
        x = 8
        y = 8
    initField(x,y)
    game(0)
    

mainMenu()
