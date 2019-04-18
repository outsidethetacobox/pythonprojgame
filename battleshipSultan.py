class player():
    def __init__(self):
        # None = num of shots player can fire
        self.shots = None

        # Shows where the player’s ships are and where the opponent has fired shots at
        self.primaryGrid = [[None] * 10] * 10

        # Shows where the player has fired shots at
        self.trackingGrid = [[None] * 10] * 10

        # Where the player's ships are
        self.pat = [[None] * 2] * 2
        self.des = [[None] * 2] * 3
        self.sub = [[None] * 2] * 3
        self.bat = [[None] * 2] * 4
        self.car = [[None] * 2] * 5

        # Ship's hp, individaul coordinate hp
        self.patHp = [2, 1, 1]
        self.desHp = [3, 1, 1, 1]
        self.subHp = [3, 1, 1, 1]
        self.batHp = [4, 1, 1, 1, 1]
        self.carHp = [5, 1, 1, 1, 1, 1]

        # Where the player fires shots at
        self.fireLoc = [[None] * 2] * 5

    def translate(self, s):
        s = s.strip()
        s = s.lower()
        if (2 <= len(s) <= 3):
            if (len(s) == 3):
                y = int(s[1]+s[2])
            else:
                y = int(s[1])

            if (1 <= y <= 10):
                x = ord(s[0])
                if (97 <= x <= 106):
                    return x, y
                else:
                 err = True
            else:
                err = True
        else:
            err = True

        # This is the error/try catch stuff, finish it later
        if (err == True):
        # print("Invalid input. Try again.")


    # Get the fireLoc from Tyler
    def inputFireLoc(self, fireInputs=[]):
        for w in range(a.status[0]):
            # This is a temp for the error/try catch stuff
            err = False

            # string to XY int       
            x,y = self.translate(fireInputs[w])
            self.fireLoc[w] = [x,y]

    def fire(self, object):
        for a in range(self.shots):
            # To check if a shot has been fired
            shotFired = False

            # Check if patrol boat still alive
            if(object.patHp[0] != 0):
                for b in range(2):
                    if(object.patHp[b + 1] != 0 and object.pat[b] == self.firLoc[a]):
                        object.patHp[b + 1] = 0
                        object.patHp[0] -= 1
                        shotFired = True
                        break

            # Check if destroyer still alive & no shot was fired
            if(object.desHp[0] != 0 and shotFired == False):
                for b in range(3):
                    if(object.desHp[b + 1] != 0 and object.des[b] == self.firLoc[a]):
                        object.desHp[b + 1] = 0
                        object.desHp[0] -= 1
                        shotFired = True
                        break

            # Check if submarine still alive & no shot was fired
            if(object.subHp[0] != 0 and shotFired == False):
                for b in range(3):
                    if(object.subHp[b + 1] != 0 and object.sub[b] == self.firLoc[a]):
                        object.subHp[b + 1] = 0
                        object.subHp[0] -= 1
                        shotFired = True
                        break

            # Check if battleship still alive & no shot was fired
            if(object.batHp[0] != 0 and shotFired == False):
                for b in range(4):
                    if(object.batHp[b + 1] != 0 and object.bat[b] == self.firLoc[a]):
                        object.batHp[b + 1] = 0
                        object.batHp[0] -= 1
                        shotFired = True
                        break

            # Check if carrier still alive & no shot was fired
            if(object.carHp[0] != 0 and shotFired == False):
                for b in range(5):
                    if(object.carHp[b + 1] != 0 and object.car[b] == self.firLoc[a]):
                        object.carHp[b + 1] = 0
                        object.carHp[0] -= 1
                        shotFired = True
                        break

            # Update tracking grid at fireLoc to 1 for hit and 0 for miss
            if(shotFired == True):
                self.trackingGrid[self.fireLoc[a][0]][self.fireLoc[a][1]] = 1
                object.primaryGrid[self.fireLoc[a][0]][self.fireLoc[a][1]] = 1
                self.isSunk(object)
            else:
                self.trackingGrid[self.fireLoc[a][0]][self.fireLoc[a][1]] = 0
                object.primaryGrid[self.fireLoc[a][0]][self.fireLoc[a][1]] = 0

    # Update tracking grid of what opponent ships have been sunk
    def isSunk(self, object):
        if(object.patHp[0] == 0):
            for a in range(2):
                self.trackingGrid[object.pat[b][0] - 96][object.pat[b][1]] = 2
                object.primaryGrid[object.pat[b][0] - 96][object.pat[b][1]] = 2

        if(object.desHp[0] == 0):
            for a in range(3):
                self.trackingGrid[object.des[b][0] - 96][object.des[b][1]] = 2
                object.primaryGrid[object.des[b][0] - 96][object.des[b][1]] = 2

        if(object.subHp[0] == 0):
            for a in range(3):
                self.trackingGrid[object.sub[b][0] - 96][object.sub[b][1]] = 2
                object.primaryGrid[object.sub[b][0] - 96][object.sub[b][1]] = 2

        if(object.batHp[0] == 0):
            for a in range(4):
                self.trackingGrid[object.bat[b][0] - 96][object.bat[b][1]] = 2
                object.primaryGrid[object.bat[b][0] - 96][object.bat[b][1]] = 2

        if(object.carHp[0] == 0):
            for a in range(5):
                self.trackingGrid[object.car[b][0] - 96][object.car[b][1]] = 2
                object.primaryGrid[object.car[b][0] - 96][object.car[b][1]] = 2


    # Get the shipLoc from Shawn for each ship
    def setShips(self, p = [], d = [], su = [], b = [], c = []):
        for w in range(2):
            # string of XY for patrol boat
            x,y = self.translate(p[w])
            self.pat[w] = [x,y]

        for w in range(3):
            # string of XY for destroyer
            x,y = self.translate(d[w])
            self.des[w] = [x,y]

        for w in range(3):
            # string of XY for submarine
            x,y = self.translate(su[w])
            self.sub[w] = [x,y]

        for w in range(4):
            # string of XY for battleship
            x,y = self.translate(b[w])
            self.bat[w] = [x,y]

        for w in range(5):
            # string of XY for carrier
            x,y = self.translate(c[w])
            self.car[w] = [x,y]
            

# Testing dictionary possibilty, ignore it...
"""
dictionary = {"Carrier": car, "Battleship": bat,
              "Submarine": sub, "Destroyer": des, "Patrol": pat}

print the entire dict:
for x, y in dictionary.items():
    print(x, y)
"""