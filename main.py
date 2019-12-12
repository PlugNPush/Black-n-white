import operator

field = []

def place(x, y, player):
    field[x][y] = player

def initField(x, y):
    for i in range(0, x):
        field.append([])
        for s in range(0, y):
            field[i].append(-1)
    
    place(int((len(field)-1)/2), int((len(field[len(field)-1])-1)/2), 0)
    place(int(((len(field)-1)/2)+1), int(((len(field[len(field)-1])-1)/2)+1), 0)
    place(int(((len(field)-1)/2)+1), int(((len(field[len(field)-1])-1)/2)), 1)
    place(int(((len(field)-1)/2)), int(((len(field[len(field)-1])-1)/2)+1), 1)
            
def printField():
    for line in field:
        for s in range(0, len(line)):
            if line[s] == -1:
                print("❇️", "", end='')
            elif line[s] == 0:
                print("⚫️", "", end='')
            elif line[s] == 1:
                print("⚪️", "", end='')
        print("")

def cvToBool(arg):
    if arg == 1:
        return True
    else:
        return False

def placePion(x, y, player):
    if x > len(field)-1 or y > len(field[0])-1 or x < 0 or y < 0:
        print("Vous ne pouvez pas jouer en dehors du terrain.")
        return 1
    if field[x][y] != -1:
        print("Vous ne pouvez pas jouer sur une case déjà occupée.")
        return 2
        
    curplay = cvToBool(player)
        
    valueToReturn = -1
    # LIGNE VERS LE HAUT
    if cvToBool(field[x-1][y]) == operator.not_(curplay) and cvToBool(field[x-2][y]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x-1, y, player)
    # DIAGONALE HAUTE DROITE
    if cvToBool(field[x-1][y+1]) == operator.not_(curplay) and cvToBool(field[x-2][y+2]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x-1, y+1, player)
    # COLONNE DROITE
    if cvToBool(field[x][y+1]) == operator.not_(curplay) and cvToBool(field[x][y+2]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x, y+1, player)
    # DIAGONALE BAS DROTE
    if cvToBool(field[x+1][y+1]) == operator.not_(curplay) and cvToBool(field[x+2][y+2]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x+1, y+1, player)
    # LIGNE BAS
    if cvToBool(field[x+1][y]) == operator.not_(curplay) and cvToBool(field[x+2][y]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x+1, y, player)
    # DIAGONALE BAS GAUCHE
    if cvToBool(field[x+1][y-1]) == operator.not_(curplay) and cvToBool(field[x+2][y-2]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x+1, y-1, player)
    # COLONNE GAUCHE
    if cvToBool(field[x][y-1]) == operator.not_(curplay) and cvToBool(field[x][y-2]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x, y-1, player)
    # DIAGONALE HAUTE GAUCHE
    if cvToBool(field[x-1][y-1]) == operator.not_(curplay) and cvToBool(field[x-2][y-2]) == curplay:
        valueToReturn = 0
        place(x, y, player)
        place(x-1, y-1, player)
    
    return valueToReturn
        

initField(8, 8)
placePion(4, 2, 0)
placePion(5, 4, 1)
printField()






