shipList = []

class Ship:
    def __init__(self, length, x_pos, y_pos, orient):
        self.length = length
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.orient = orient
    def getLength(self):
        return self.length
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    def getOrient(self):
        return self.orient

class Battlefield:
    def __init__(self, length):
        self.length = length
        self.grid = self.initialisegrid()
    def displaygrid(self):
        for x in range(self.length):
            print()
            print(self.grid[x])
    def initialisegrid(self):
        p1bf = []
        for x in range(self.length):
            tmp = []
            for y in range(self.length):
                tmp.append("?")
            p1bf.append(tmp)
        return p1bf

def listShip():
    for i in range(len(shipList)):
        print(f"Ship number {i+1}")
        print(f"Length: {shipList[i].getLength()}")
        print(f"X Coordinate: {shipList[i].getX()}")
        print(f"Y Coordinate: {shipList[i].getY()}")
        print(f"Orientation: {shipList[i].getOrient()}")
        print()

def createShip(n):
    for _ in range(n):
        l = int(input("Insert the length of your ship: "))
        x = int(input("Insert the x coordinate of your ship: "))
        y = int(input("Insert the y coordinate of your ship: "))
        orient = input("Choose the orientation of you ship(left/right/up/down): ")
        ship = Ship(l, x, y, orient)
        shipList.append(ship)

length = int(input("Please input the length of the grid"))
b1 = Battlefield(length)
b1.displaygrid()

createShip(1)
listShip()