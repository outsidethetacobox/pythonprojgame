# BattleshipSultan.py is the logic component of the battleship project, made by Sultan fw7888

import pygame
import battleship_pac.text as txt
import gameboard
import Battle_menu
import completeReq

class player():
    def __init__(self):
        # The type of game played and is set along with the ships at beginning of game (0 = classic, 1 = Salvo) 
        self.gameType = None

        # None = num of shots player can fire
        self.shots = None

        # Shows where the player’s ships are and where the opponent has fired shots at
        self.primaryGrid = {
            '1': None,
            '2': None,
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': None,
            '8': None,
            '9': None,
            '10': None,
            '11': None,
            '12': None,
            '13': None,
            '14': None,
            '15': None,
            '16': None,
            '17': None,
            '18': None,
            '19': None,
            '20': None,
            '21': None,
            '22': None,
            '23': None,
            '24': None,
            '25': None,
            '26': None,
            '27': None,
            '28': None,
            '29': None,
            '30': None,
            '31': None,
            '32': None,
            '33': None,
            '34': None,
            '35': None,
            '36': None,
            '37': None,
            '38': None,
            '39': None,
            '40': None,
            '41': None,
            '42': None,
            '43': None,
            '44': None,
            '45': None,
            '46': None,
            '47': None,
            '48': None,
            '49': None,
            '50': None,
            '51': None,
            '52': None,
            '53': None,
            '54': None,
            '55': None,
            '56': None,
            '57': None,
            '58': None,
            '59': None,
            '60': None,
            '61': None,
            '62': None,
            '63': None,
            '64': None,
            '65': None,
            '66': None,
            '67': None,
            '68': None,
            '69': None,
            '70': None,
            '71': None,
            '72': None,
            '73': None,
            '74': None,
            '75': None,
            '76': None,
            '77': None,
            '78': None,
            '79': None,
            '80': None,
            '81': None,
            '82': None,
            '83': None,
            '84': None,
            '85': None,
            '86': None,
            '87': None,
            '88': None,
            '89': None,
            '90': None,
            '91': None,
            '92': None,
            '93': None,
            '94': None,
            '95': None,
            '96': None,
            '97': None,
            '98': None,
            '99': None,
            '100': None,
            'p': 'p'}

        # Shows where the player has fired shots at
        self.trackingGrid = self.primaryGrid.copy()

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
        # This is the error/try catch for string
        try:
            s = s.strip()
            s = s.lower()
            
            # If the input string is a number 1 to 100
            n = int(s)
            if (1 <= n <= 100):        
                if(n <= 10):
                    x = n
                    y = 1
                else:
                    y = int(n / 10)
                    x = n % 10
                    if (x == 0):
                        x = 10
                return x, y
            # If the input string is A-J 1-10 (no space betweeen letter and number)
            elif (2 <= len(s) <= 3):
                if (len(s) == 3):
                    y = int(s[1]+s[2])
                else:
                    y = int(s[1])

                if (1 <= y <= 10):
                    x = ord(s[0]) - 96
                    if (97 <= x <= 106):
                        return x, y
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Invalid string value. Try again.")
        

    # Turn X,Y coordinates into string
    def getString(self, x, y):
        if (y == '1'):
            s = x
        elif (x == '10'):
            s = y + '0'
        else:
            s = y + x
        return s

    # Get the fireLoc from Tyler
    def inputFireLoc(self, fireInputs = []):
        for w in range(self.shots):
            # string to XY int
            x,y = self.translate(fireInputs[w])
            self.fireLoc[w] = [x,y]

    def fire(self, object):
        hit = 0
        for a in range(self.shots):
            # To check if a shot has been fired
            shotFired = False

            # Check if patrol boat still alive & no shot was fired
            if(object.patHp[0] != 0):
                for b in range(2):
                    if(object.patHp[b + 1] != 0 and object.pat[b] == self.fireLoc[a]):
                        object.patHp[b + 1] = 0
                        object.patHp[0] -= 1
                        shotFired = True
                        break

            # Check if destroyer still alive & no shot was fired
            if(object.desHp[0] != 0 and shotFired == False):
                for b in range(3):
                    if(object.desHp[b + 1] != 0 and object.des[b] == self.fireLoc[a]):
                        object.desHp[b + 1] = 0
                        object.desHp[0] -= 1
                        shotFired = True
                        break

            # Check if submarine still alive & no shot was fired
            if(object.subHp[0] != 0 and shotFired == False):
                for b in range(3):
                    if(object.subHp[b + 1] != 0 and object.sub[b] == self.fireLoc[a]):
                        object.subHp[b + 1] = 0
                        object.subHp[0] -= 1
                        shotFired = True
                        break

            # Check if battleship still alive & no shot was fired
            if(object.batHp[0] != 0 and shotFired == False):
                for b in range(4):
                    if(object.batHp[b + 1] != 0 and object.bat[b] == self.fireLoc[a]):
                        object.batHp[b + 1] = 0
                        object.batHp[0] -= 1
                        shotFired = True
                        break

            # Check if carrier still alive & no shot was fired
            if(object.carHp[0] != 0 and shotFired == False):
                for b in range(5):
                    if(object.carHp[b + 1] != 0 and object.car[b] == self.fireLoc[a]):
                        object.carHp[b + 1] = 0
                        object.carHp[0] -= 1
                        shotFired = True
                        break

            x = str(self.fireLoc[a][0])
            y = str(self.fireLoc[a][1])
            s = self.getString(x,y)
            # Update tracking grid at fireLoc to 1 for hit and 0 for miss
            if(shotFired == True):
                self.trackingGrid[s] = 1
                object.primaryGrid[s] = 1
                self.isSunk(object)
                hit = 1
            else:
                self.trackingGrid[s] = 0
                object.primaryGrid[s] = 0
        if (hit != 0):
            return 1
        else:
            return 0       

    # Update player's tracking grid of what opponent ships have been sunk and the opponent's primary grid
    def isSunk(self, object):
        # The count is to update the how many times the opponent can fire shots
        count = 0
        if(object.patHp[0] == 0):
            for b in range(2):
                x = str(object.pat[b][0])
                y = str(object.pat[b][1])
                s = self.getString(x,y)
                self.trackingGrid[s] = 2
                object.primaryGrid[s] = 2
            count += 1

        if(object.desHp[0] == 0):
            for b in range(3):
                x = str(object.des[b][0])
                y = str(object.des[b][1])
                s = self.getString(x,y)
                self.trackingGrid[s] = 2
                object.primaryGrid[s] = 2
            count += 1
                

        if(object.subHp[0] == 0):
            for b in range(3):
                x = str(object.sub[b][0])
                y = str(object.sub[b][1])
                s = self.getString(x,y)
                self.trackingGrid[s] = 2
                object.primaryGrid[s] = 2
            count += 1

        if(object.batHp[0] == 0):
            for b in range(4):
                x = str(object.bat[b][0])
                y = str(object.bat[b][1])
                s = self.getString(x,y)
                self.trackingGrid[s] = 2
                object.primaryGrid[s] = 2
            count += 1

        if(object.carHp[0] == 0):
            for b in range(5):
                x = str(object.car[b][0])
                y = str(object.car[b][1])
                s = self.getString(x,y)
                self.trackingGrid[s] = 2
                object.primaryGrid[s] = 2
            count += 1
        
        if (self.gameType == 1):
            object.shots = 5 - count


    # Get the gameMode/gameType and the shipLoc from Shawn for each ship
    def setShips(self, gameMode = 0, p = [], d = [], su = [], b = [], c = []):
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

        if (gameMode == 0):
            self.shots = 1
            self.gameType = 0
        else:
            self.shots = 5
            self.gameType = 1
