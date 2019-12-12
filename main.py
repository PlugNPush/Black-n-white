field = []

def initField(x, y):
    for i in range(0, x):
        field.append([])
        for s in range(0, y):
            field[i].append(-1)
            
def printField():
    for line in field:
        for s in range(0, len(line)):
            if line[s] == -1:
                print("🟩", "", end='')
            elif line[s] == 0:
                print("⚫️", "", end='')
            elif line[s] == 1:
                print("⚪️", "", end='')
        print("")

def place(x, y, player):
    field[x][y] = player

initField(8, 8)
place(3, 2, 0)
place(2, 5, 1)
printField()






