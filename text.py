import pygame
#Coded By Tyler Gross gl0132
black = 0, 0, 0
pygame.init()
F = pygame.font.SysFont("Times New Norman", 24)

one = F.render("1", True, black)
two = F.render("2", True, black)
three = F.render("3", True, black)
four = F.render("4", True, black)
five = F.render("5", True, black)
six = F.render("6", True, black)
seven = F.render("7", True, black)
eight = F.render("8", True, black)
nine = F.render("9", True, black)
ten = F.render("10", True, black)
tone = F.render("11", True, black)
ttwo = F.render("12", True, black)
tthree = F.render("13", True, black)
tfour = F.render("14", True, black)
tfive = F.render("15", True, black)
tsix = F.render("16", True, black)
tseven = F.render("17", True, black)
teight = F.render("18", True, black)
tnine = F.render("19", True, black)
tw = F.render("20", True, black)
twone = F.render("21", True, black)
twtwo = F.render("22", True, black)
twthree = F.render("23", True, black)
twfour = F.render("24", True, black)
twfive = F.render("25", True, black)
twsix = F.render("26", True, black)
twseven = F.render("27", True, black)
tweight = F.render("28", True, black)
twnine = F.render("29", True, black)
tty = F.render("30", True, black)
ttyone = F.render("31", True, black)
ttytwo = F.render("32", True, black)
ttythree = F.render("33", True, black)
ttyfour = F.render("34", True, black)
ttyfive = F.render("35", True, black)
ttysix = F.render("36", True, black)
ttyseven = F.render("37", True, black)
ttyeight = F.render("38", True, black)
ttynine = F.render("39", True, black)
fty = F.render("40", True, black)
ftyone = F.render("41", True, black)
ftytwo = F.render("42", True, black)
ftythree = F.render("43", True, black)
ftyfour = F.render("44", True, black)
ftyfive = F.render("45", True, black)
ftysix = F.render("46", True, black)
ftyseven = F.render("47", True, black)
ftyeight = F.render("48", True, black)
ftynine = F.render("49", True, black)
fv = F.render("50", True, black)
fvone = F.render("51", True, black)
fvtwo = F.render("52", True, black)
fvthree = F.render("53", True, black)
fvfour = F.render("54", True, black)
fvfive = F.render("55", True, black)
fvsix = F.render("56", True, black)
fvseven = F.render("57", True, black)
fveight = F.render("58", True, black)
fvnine = F.render("59", True, black)
sxy = F.render("60", True, black)
sxyone = F.render("61", True, black)
sxytwo = F.render("62", True, black)
sxythree = F.render("63", True, black)
sxyfour = F.render("64", True, black)
sxyfive = F.render("65", True, black)
sxysix = F.render("66", True, black)
sxyseven = F.render("67", True, black)
sxyeight = F.render("68", True, black)
sxynine = F.render("69", True, black)
svn = F.render("70", True, black)
svnone = F.render("71", True, black)
svntwo = F.render("72", True, black)
svnthree = F.render("73", True, black)
svnfour = F.render("74", True, black)
svnfive = F.render("75", True, black)
svnsix = F.render("76", True, black)
svnseven = F.render("77", True, black)
svneight = F.render("78", True, black)
svnnine = F.render("79", True, black)
egt = F.render("80", True, black)
egtone = F.render("81", True, black)
egttwo = F.render("82", True, black)
egtthree = F.render("83", True, black)
egtfour = F.render("84", True, black)
egtfive = F.render("85", True, black)
egtsix = F.render("86", True, black)
egtseven = F.render("87", True, black)
egteight = F.render("88", True, black)
egtnine = F.render("89", True, black)
nin = F.render("90", True, black)
ninone = F.render("91", True, black)
nintwo = F.render("92", True, black)
ninthree = F.render("93", True, black)
ninfour = F.render("94", True, black)
ninfive = F.render("95", True, black)
ninsix = F.render("96", True, black)
ninseven = F.render("97", True, black)
nineight = F.render("98", True, black)
ninnine = F.render("99", True, black)
hunny = F.render("100", True, black)
pause = F.render("Pause", True, black)


def send_text(text):
    return text


hits_list = {
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
    'p': 'p'
}


class ships:
    battleship = {0: None, 1: None, 2: None, 3: None}
    carrier = {0: None, 1: None, 2: None, 3: None, 4: None}
    submarine = {0: None, 1: None, 2: None}
    destroyer = {0: None, 1: None}
    crusier  = {0: None, 1: None, 2: None}

    def __init__(self):
        self.battleship[1] = ""

    def load_battleship(self, text):
        if self.battleship[0] is not None:
            if self.battleship[0: None]:
                self.battleship[0:text]
            elif self.battleship[1:""]:
                self.battleship[1:text]
            elif self.battleship[2:""]:
                self.battleship[2:text]
            elif self.battleship[3:""]:
                self.battleship[3:text]
        else:
            return True


    def load_carrier(self, text):
        if self.carrier[0] is not None:
            if self.carrier[0: ""]:
                self.carrier[0:text]
            elif self.carrier[1:""]:
                self.carrier[1:text]
            elif self.carrier[2:""]:
                self.carrier[2:text]
            elif self.carrier[3:""]:
                self.carrier[3:text]
            elif self.carrier[4:""]:
                self.carrier[4:text]
        else:
            return True


    def load_crusier(self, text):
        if self.carrier[0] is not None:
            if self.crusier[0: ""]:
                self.crusier[0:text]
            elif self.crusier[1:""]:
                self.crusier[1:text]
            elif self.crusier[2:""]:
                self.crusier[2:text]
        else:
            return True


    def load_submarine(self, text):
        if self.submarine[0] is not None:
            if self.submarine[0: ""]:
                self.submarine[0:text]
            elif self.submarine[1:""]:
                self.submarine[1:text]
            elif self.submarine[2:""]:
                self.submarine[2:text]
        else:
            return True

    def load_destroyer(self, text):
        if self.destroyer[0] is not None:
            if self.destroyer[0: ""]:
                self.destroyer[0:text]
            elif self.destroyer[1:""]:
                self.destroyer[1:text]
        else:
            return True


    def checkcollision(self, spot):
        for x in range(4):
            if self.battleship[x] == spot:
                return True
        for x in range(3):
            if self.submarine[x] == spot:
                return True
        for x in range(5):
            if self.carrier[x] == spot:
                return True
        for x in range(2):
            if self.destroyer[x] == spot:
                return True
        for x in range(3):
            if self.crusier[x] == spot:
                return True
        return False



