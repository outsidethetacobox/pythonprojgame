import pygame
import pybattleship.text as txt
# import battleshipSultan
# from Package_Battleship.gameover import gameover as gova REMOVE COMMENT
# Gameboard coded by Tyler Gross Gl0132

pygame.init()
clock = pygame.time.Clock()
black = 0, 0, 0
blue = 0, 0, 255
violet_blue = 138, 43, 226
red = 255, 0, 0
dar_red = 139, 0, 0
green = 0, 128, 0
clock = pygame.time.Clock()
Display = pygame.display.set_mode((800, 700))
F = pygame.font.SysFont("Times New Norman", 24)

one_button = pygame.Rect(50, 20, 60, 40)
two_button = pygame.Rect(115, 20, 60, 40)
three_button = pygame.Rect(180, 20, 60, 40)
four_button = pygame.Rect(245, 20, 60, 40)
five_button = pygame.Rect(310, 20, 60, 40)
six_button = pygame.Rect(375, 20, 60, 40)
seven_button = pygame.Rect(440, 20, 60, 40)
eight_button = pygame.Rect(505, 20, 60, 40)
nine_button = pygame.Rect(570, 20, 60, 40)
ten_button = pygame.Rect(635, 20, 60, 40)
eleven_button = pygame.Rect(50, 65, 60, 40)
twelve_button = pygame.Rect(115, 65, 60, 40)
thirteen_button = pygame.Rect(180, 65, 60, 40)
fourteen_button = pygame.Rect(245, 65, 60, 40)
fiveteen_button = pygame.Rect(310, 65, 60, 40)
sixteen_button = pygame.Rect(375, 65, 60, 40)
seventeen_button = pygame.Rect(440, 65, 60, 40)
eightteen_button = pygame.Rect(505, 65, 60, 40)
nineteen_button = pygame.Rect(570, 65, 60, 40)
twenty_button = pygame.Rect(635, 65, 60, 40)
twone_button = pygame.Rect(50, 110, 60, 40)
twtwo_button = pygame.Rect(115, 110, 60, 40)
twthree_button = pygame.Rect(180, 110, 60, 40)
twfour_button = pygame.Rect(245, 110, 60, 40)
twfive_button = pygame.Rect(310, 110, 60, 40)
twsix_button = pygame.Rect(375, 110, 60, 40)
twseven_button = pygame.Rect(440, 110, 60, 40)
tweight_button = pygame.Rect(505, 110, 60, 40)
twnine_button = pygame.Rect(570, 110, 60, 40)
tty_button = pygame.Rect(635, 110, 60, 40)
ttyone_button = pygame.Rect(50, 155, 60, 40)
ttytwo_button = pygame.Rect(115, 155, 60, 40)
ttythree_button = pygame.Rect(180, 155, 60, 40)
ttyfour_button = pygame.Rect(245, 155, 60, 40)
ttyfive_button = pygame.Rect(310, 155, 60, 40)
ttysix_button = pygame.Rect(375, 155, 60, 40)
ttyseven_button = pygame.Rect(440, 155, 60, 40)
ttyeight_button = pygame.Rect(505, 155, 60, 40)
ttynine_button = pygame.Rect(570, 155, 60, 40)
ft_button = pygame.Rect(635, 155, 60, 40)
ftone_button = pygame.Rect(50, 200, 60, 40)
fttwo_button = pygame.Rect(115, 200, 60, 40)
ftthree_button = pygame.Rect(180, 200, 60, 40)
ftfour_button = pygame.Rect(245, 200, 60, 40)
ftfive_button = pygame.Rect(310, 200, 60, 40)
ftsix_button = pygame.Rect(375, 200, 60, 40)
ftseven_button = pygame.Rect(440, 200, 60, 40)
fteight_button = pygame.Rect(505, 200, 60, 40)
ftnine_button = pygame.Rect(570, 200, 60, 40)
fv_button = pygame.Rect(635, 200, 60, 40)
fvone_button = pygame.Rect(50, 245, 60, 40)
fvtwo_button = pygame.Rect(115, 245, 60, 40)
fvthree_button = pygame.Rect(180, 245, 60, 40)
fvfour_button = pygame.Rect(245, 245, 60, 40)
fvfive_button = pygame.Rect(310, 245, 60, 40)
fvsix_button = pygame.Rect(375, 245, 60, 40)
fvseven_button = pygame.Rect(440, 245, 60, 40)
fveight_button = pygame.Rect(505, 245, 60, 40)
fvnine_button = pygame.Rect(570, 245, 60, 40)
sx_button = pygame.Rect(635, 245, 60, 40)
sxone_button = pygame.Rect(50, 290, 60, 40)
sxtwo_button = pygame.Rect(115, 290, 60, 40)
sxthree_button = pygame.Rect(180, 290, 60, 40)
sxfour_button = pygame.Rect(245, 290, 60, 40)
sxfive_button = pygame.Rect(310, 290, 60, 40)
sxsix_button = pygame.Rect(375, 290, 60, 40)
sxseven_button = pygame.Rect(440, 290, 60, 40)
sxeight_button = pygame.Rect(505, 290, 60, 40)
sxnine_button = pygame.Rect(570, 290, 60, 40)
svn_button = pygame.Rect(635, 290, 60, 40)
svnone_button = pygame.Rect(50, 335, 60, 40)
svntwo_button = pygame.Rect(115, 335, 60, 40)
svnthree_button = pygame.Rect(180, 335, 60, 40)
svnfour_button = pygame.Rect(245, 335, 60, 40)
svnfive_button = pygame.Rect(310, 335, 60, 40)
svnsix_button = pygame.Rect(375, 335, 60, 40)
svnseven_button = pygame.Rect(440, 335, 60, 40)
svneight_button = pygame.Rect(505, 335, 60, 40)
svnnine_button = pygame.Rect(570, 335, 60, 40)
ety_button = pygame.Rect(635, 335, 60, 40)
etyone_button = pygame.Rect(50, 380, 60, 40)
etytwo_button = pygame.Rect(115, 380, 60, 40)
etythree_button = pygame.Rect(180, 380, 60, 40)
etyfour_button = pygame.Rect(245, 380, 60, 40)
etyfive_button = pygame.Rect(310, 380, 60, 40)
etysix_button = pygame.Rect(375, 380, 60, 40)
etyseven_button = pygame.Rect(440, 380, 60, 40)
etyeight_button = pygame.Rect(505, 380, 60, 40)
etynine_button = pygame.Rect(570, 380, 60, 40)
nty_button = pygame.Rect(635, 380, 60, 40)
ntyone_button = pygame.Rect(50, 425, 60, 40)
ntytwo_button = pygame.Rect(115, 425, 60, 40)
ntythree_button = pygame.Rect(180, 425, 60, 40)
ntyfour_button = pygame.Rect(245, 425, 60, 40)
ntyfive_button = pygame.Rect(310, 425, 60, 40)
ntysix_button = pygame.Rect(375, 425, 60, 40)
ntyseven_button = pygame.Rect(440, 425, 60, 40)
ntyeight_button = pygame.Rect(505, 425, 60, 40)
ntynine_button = pygame.Rect(570, 425, 60, 40)
onehunny_button = pygame.Rect(635, 425, 60, 40)


acton = 3
# text , rect , color, hover color, hit_color, miss_color x, h, y, w, spot number, action
buttons = [
    [txt.one, one_button, blue, violet_blue, green, red, 50, 20, 60, 40, '1', txt.hits_list],
    [txt.two, two_button, blue, violet_blue, green, red, 115, 20, 60, 40, '2',  txt.hits_list],
    [txt.three, three_button, blue, violet_blue, green, red, 180, 20, 60, 40, '3',  txt.hits_list],
    [txt.four, four_button, blue, violet_blue, green, red, 245, 20, 60, 40, '4',  txt.hits_list],
    [txt.five, five_button, blue, violet_blue, green, red, 310, 20, 60, 40, '5',  txt.hits_list],
    [txt.six, six_button, blue, violet_blue, green, red, 375, 20, 60, 40, '6',  txt.hits_list],
    [txt.seven, seven_button, blue, violet_blue, green, red, 440, 20, 60, 40, '7',  txt.hits_list],
    [txt.eight, eight_button, blue, violet_blue, green, red, 505, 20, 60, 40, '8',  txt.hits_list],
    [txt.nine, nine_button, blue, violet_blue, green, red, 570, 20, 60, 40, '9',  txt.hits_list],
    [txt.ten, ten_button, blue, violet_blue, green, red, 635, 20, 60, 40, '10',  txt.hits_list],
    [txt.tone, eleven_button, blue, violet_blue, green, red, 50, 65, 60, 40, '11',  txt.hits_list],
    [txt.ttwo, twelve_button, blue, violet_blue, green, red, 115, 65, 60, 40, '12',  txt.hits_list],
    [txt.tthree, thirteen_button, blue, violet_blue, green, red, 180, 65, 60, 40, '13',  txt.hits_list],
    [txt.tfour, fourteen_button, blue, violet_blue, green, red, 245, 65, 60, 40, '14',  txt.hits_list],
    [txt.tfive, fiveteen_button, blue, violet_blue, green, red, 310, 65, 60, 40, '15',  txt.hits_list],
    [txt.tsix, sixteen_button, blue, violet_blue, green, red, 375, 65, 60, 40, '16',  txt.hits_list],
    [txt.tseven, seventeen_button, blue, violet_blue, green, red, 440, 65, 60, 40, '17',  txt.hits_list],
    [txt.teight, eightteen_button, blue, violet_blue, green, red, 505, 65, 60, 40, '18',  txt.hits_list],
    [txt.tnine, nineteen_button, blue, violet_blue, green, red, 570, 65, 60, 40, '19',  txt.hits_list],
    [txt.tw, twenty_button, blue, violet_blue, green, red, 635, 65, 60, 40, '20',  txt.hits_list],
    [txt.twone, twone_button, blue, violet_blue, green, red, 50, 110, 60, 40, '21',  txt.hits_list],
    [txt.twtwo, twtwo_button, blue, violet_blue, green, red, 115, 110, 60, 40, '22',  txt.hits_list],
    [txt.twthree, twthree_button, blue, violet_blue, green, red, 180, 110, 60, 40, '23',  txt.hits_list],
    [txt.twfour, twfour_button, blue, violet_blue, green, red, 245, 110, 60, 40, '24',  txt.hits_list],
    [txt.twfive, twfive_button, blue, violet_blue, green, red, 310, 110, 60, 40, '25',  txt.hits_list],
    [txt.twsix, twsix_button, blue, violet_blue, green, red, 375, 110, 60, 40, '26',  txt.hits_list],
    [txt.twseven, twseven_button, blue, violet_blue, green, red, 440, 110, 60, 40, '27',  txt.hits_list],
    [txt.tweight, tweight_button, blue, violet_blue, green, red, 505, 110, 60, 40, '28',  txt.hits_list],
    [txt.twnine, twnine_button, blue, violet_blue, green, red, 570, 110, 60, 40, '29',  txt.hits_list],
    [txt.tty, tty_button, blue, violet_blue, green, red, 635, 110, 60, 40, '30',  txt.hits_list],
    [txt.ttyone, ttyone_button, blue, violet_blue, green, red, 50, 155, 60, 40, '31',  txt.hits_list],
    [txt.ttytwo, ttytwo_button, blue, violet_blue, green, red, 115, 155, 60, 40, '32',  txt.hits_list],
    [txt.ttythree, ttythree_button, blue, violet_blue, green, red, 180, 155, 60, 40, '33',  txt.hits_list],
    [txt.ttyfour, ttyfour_button, blue, violet_blue, green, red, 245, 155, 60, 40, '34',  txt.hits_list],
    [txt.ttyfive, ttyfive_button, blue, violet_blue, green, red, 310, 155, 60, 40, '35',  txt.hits_list],
    [txt.ttysix, ttysix_button, blue, violet_blue, green, red, 375, 155, 60, 40, '36',  txt.hits_list],
    [txt.ttyseven, ttyseven_button, blue, violet_blue, green, red, 440, 155, 60, 40, '37',  txt.hits_list],
    [txt.ttyeight, ttyeight_button, blue, violet_blue, green, red, 505, 155, 60, 40, '38',  txt.hits_list],
    [txt.ttynine, ttynine_button, blue, violet_blue, green, red, 570, 155, 60, 40, '39',  txt.hits_list],
    [txt.fty, ft_button, blue, violet_blue, green, red, 635, 155, 60, 40, '40',  txt.hits_list],
    [txt.ftyone, ftone_button, blue, violet_blue, green, red, 50, 200, 60, 40, '41',  txt.hits_list],
    [txt.ftytwo, fttwo_button, blue, violet_blue, green, red, 115, 200, 60, 40, '42',  txt.hits_list],
    [txt.ftythree, ftthree_button, blue, violet_blue, green, red, 180, 200, 60, 40, '43',  txt.hits_list],
    [txt.ftyfour, ftfour_button, blue, violet_blue, green, red, 245, 200, 60, 40, '44',  txt.hits_list],
    [txt.ftyfive, ftfive_button, blue, violet_blue, green, red, 310, 200, 60, 40, '45',  txt.hits_list],
    [txt.ftysix, ftsix_button, blue, violet_blue, green, red, 375, 200, 60, 40, '46',  txt.hits_list],
    [txt.ftyseven, ftseven_button, blue, violet_blue, green, red, 440, 200, 60, 40, '47',  txt.hits_list],
    [txt.ftyeight, fteight_button, blue, violet_blue, green, red, 505, 200, 60, 40, '48',  txt.hits_list],
    [txt.ftynine, ftnine_button, blue, violet_blue, green, red, 570, 200, 60, 40, '49',  txt.hits_list],
    [txt.fv, fv_button, blue, violet_blue, green, red, 635, 200, 60, 40, '50',  txt.hits_list],
    [txt.fvone, fvone_button, blue, violet_blue, green, red, 50, 245, 60, 40, '51',  txt.hits_list],
    [txt.fvtwo, fvtwo_button, blue, violet_blue, green, red, 115, 245, 60, 40, '52',  txt.hits_list],
    [txt.fvthree, fvthree_button, blue, violet_blue, green, red, 180, 245, 60, 40, '53',  txt.hits_list],
    [txt.fvfour, fvfour_button, blue, violet_blue, green, red, 245, 245, 60, 40, '54',  txt.hits_list],
    [txt.fvfive, fvfive_button, blue, violet_blue, green, red, 310, 245, 60, 40, '55',  txt.hits_list],
    [txt.fvsix, fvsix_button, blue, violet_blue, green, red, 375, 245, 60, 40, '56',  txt.hits_list],
    [txt.fvseven, fvseven_button, blue, violet_blue, green, red, 440, 245, 60, 40, '57',  txt.hits_list],
    [txt.fveight, fveight_button, blue, violet_blue, green, red, 505, 245, 60, 40, '58',  txt.hits_list],
    [txt.fvnine, fvnine_button, blue, violet_blue, green, red, 570, 245, 60, 40, '59',  txt.hits_list],
    [txt.sxy, sx_button, blue, violet_blue, green, red, 635, 245, 60, 40, '60',  txt.hits_list],
    [txt.sxyone, sxone_button, blue, violet_blue, green, red, 50, 290, 60, 40, '61',  txt.hits_list],
    [txt.sxytwo, sxtwo_button, blue, violet_blue, green, red, 115, 290, 60, 40, '62',  txt.hits_list],
    [txt.sxythree, sxthree_button, blue, violet_blue, green, red, 180, 290, 60, 40, '63',  txt.hits_list],
    [txt.sxyfour, sxfour_button, blue, violet_blue, green, red, 245, 290, 60, 40, '64',  txt.hits_list],
    [txt.sxyfive, sxfive_button, blue, violet_blue, green, red, 310, 290, 60, 40, '65',  txt.hits_list],
    [txt.sxysix, sxsix_button, blue, violet_blue, green, red, 375, 290, 60, 40, '66',  txt.hits_list],
    [txt.sxyseven, sxseven_button, blue, violet_blue, green, red, 440, 290, 60, 40, '67',  txt.hits_list],
    [txt.sxyeight, sxeight_button, blue, violet_blue, green, red, 505, 290, 60, 40, '68',  txt.hits_list],
    [txt.sxynine, sxnine_button, blue, violet_blue, green, red, 570, 290, 60, 40, '69',  txt.hits_list],
    [txt.svn, svn_button, blue, violet_blue, green, red, 635, 290, 60, 40, '70',  txt.hits_list],
    [txt.svnone, svnone_button, blue, violet_blue, green, red, 50, 335, 60, 40, '71',  txt.hits_list],
    [txt.svntwo, svntwo_button, blue, violet_blue, green, red, 115, 335, 60, 40, '72',  txt.hits_list],
    [txt.svnthree, svnthree_button, blue, violet_blue, green, red, 180, 335, 60, 40, '73',  txt.hits_list],
    [txt.svnfour, svnfour_button, blue, violet_blue, green, red, 245, 335, 60, 40, '74',  txt.hits_list],
    [txt.svnfive, svnfive_button, blue, violet_blue, green, red, 310, 335, 60, 40, '75', txt.hits_list],
    [txt.svnsix, svnsix_button, blue, violet_blue, green, red, 375, 335, 60, 40, '76', txt.hits_list],
    [txt.svnseven, svnseven_button, blue, violet_blue, green, red, 440, 335, 60, 40, '77', txt.hits_list],
    [txt.svneight, svneight_button, blue, violet_blue, green, red, 505, 335, 60, 40, '78', txt.hits_list],
    [txt.svnnine, svnnine_button, blue, violet_blue, green, red, 570, 335, 60, 40, '79', txt.hits_list],
    [txt.egt, ety_button, blue, violet_blue, green, red, 635, 335, 60, 40, '80', txt.hits_list],
    [txt.egtone, etyone_button, blue, violet_blue, green, red, 50, 380, 60, 40, '81', txt.hits_list],
    [txt.egttwo, etytwo_button, blue, violet_blue, green, red, 115, 380, 60, 40, '82', txt.hits_list],
    [txt.egtthree, etythree_button, blue, violet_blue, green, red, 180, 380, 60, 40, '83', txt.hits_list],
    [txt.egtfour, etyfour_button, blue, violet_blue, green, red, 245, 380, 60, 40, '84', txt.hits_list],
    [txt.egtfive, etyfive_button, blue, violet_blue, green, red, 310, 380, 60, 40, '85', txt.hits_list],
    [txt.egtsix, etysix_button, blue, violet_blue, green, red, 375, 380, 60, 40, '86', txt.hits_list],
    [txt.egtseven, etyseven_button, blue, violet_blue, green, red, 440, 380, 60, 40, '87', txt.hits_list],
    [txt.egteight, etyeight_button, blue, violet_blue, green, red, 505, 380, 60, 40, '88', txt.hits_list],
    [txt.egtnine, etynine_button, blue, violet_blue, green, red, 570, 380, 60, 40, '89', txt.hits_list],
    [txt.nin, nty_button, blue, violet_blue, green, red, 635, 380, 60, 40, '90', ''],
    [txt.ninone, ntyone_button, blue, violet_blue, green, red, 50, 425, 60, 40, '91', txt.hits_list],
    [txt.nintwo, ntytwo_button, blue, violet_blue, green, red, 115, 425, 60, 40, '92', txt.hits_list],
    [txt.ninthree, ntythree_button, blue, violet_blue, green, red, 180, 425, 60, 40, '93', txt.hits_list],
    [txt.ninfour, ntyfour_button, blue, violet_blue, green, red, 245, 425, 60, 40, '94', txt.hits_list],
    [txt.ninfive, ntyfive_button, blue, violet_blue, green, red, 310, 425, 60, 40, '95', txt.hits_list],
    [txt.ninsix, ntysix_button, blue, violet_blue, green, red, 375, 425, 60, 40, '96', txt.hits_list],
    [txt.ninseven, ntyseven_button, blue, violet_blue, green, red, 440, 425, 60, 40, '97', txt.hits_list],
    [txt.nineight, ntyeight_button, blue, violet_blue, green, red, 505, 425, 60, 40, '98', txt.hits_list],
    [txt.ninnine, ntynine_button, blue, violet_blue, green, red, 570, 425, 60, 40, '99', txt.hits_list],
    [txt.hunny, onehunny_button, blue, violet_blue, green, red, 635, 425, 60, 40, '100', acton],

]


def sendhit(spot):
    txt.hits_list[int(spot)]: '1'
    print(spot)
    print(txt.hits_list[int(spot)])


def gethit(spot):
    print(spot)
    print(txt.hits_list[spot])
    if txt.hits_list[spot] == 1:
        return True
    else:
        return False


def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()


def button_hover(button_x, button_w, button_y, button_h, disply, color, rect, text, hover_color,
                 spot_num, hit_color, miss_color, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if button_x + button_w > mouse[0] > button_x and button_y + (button_h / 2) > mouse[1] > button_y:
        pygame.draw.rect(disply, hover_color, rect)
        Display.blit(text, rect)
        if click[0] == 1:
            pygame.time.wait(200)

            txt.hits_list.update({spot_num: '1'})
            print(spot_num)
            print(txt.hits_list[spot_num])
            print(txt.hits_list.get('70'))
    elif txt.hits_list.get(spot_num) == '1':
        pygame.draw.rect(disply, hit_color, rect)
        Display.blit(text, rect)



            # firefucntion(spot)
            # if fire returns 1
            # hover_color = hit_color
            # color = hit_color
            # if fire returns 2
            # hover_color = grey
            # color = grey
            # if returns 0
            # hover_color = miss_color

    else:
        pygame.draw.rect(disply, color, rect)
        Display.blit(text, rect)



def gameon():
    gaming = True
    txt.hits_list = {}
    Display.fill(black)
    while gaming:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
            # gova() REMOVE comment
        textsurf, textrect = text_objects("comp output bar", F)
        textrect.center = (400, 600)
        Display.blit(textsurf, textrect)
        for text, rect, color, hover, hit, miss, B_x, B_y, B_w, B_h, spot, action in buttons:
            button_hover(B_x, B_h, B_y, B_w, Display, color, rect, text, hover, spot, hit, miss, action)

        pygame.display.update()
        pygame.display.flip()

# coded By Shawn
def ship_placement(gameMode=None):
    # if game mode is classic, gameMode = 0
    # if salvo gameMode = 1

    pat = [None] * 2  # patrol
    des = [None] * 3  # destroyer
    sub = [None] * 3  # submarine
    bat = [None] * 4  # battleship
    car = [None] * 5

    gaming = True
    Display.fill(black)
    while gaming:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
            # gova() REMOVE comment
        textsurf, textrect = text_objects("comp output bar", F)
        textrect.center = (400, 600)
        Display.blit(textsurf, textrect)

        for text, rect, color, hover, hit, miss, B_x, B_y, B_w, B_h, spot in buttons:
            value = button_hover(B_x, B_h, B_y, B_w, Display, color, rect, text, hover, hit, miss, spot)
            if value != None:
                if pat[0] == None:
                    pat[0] = value
                    print("patrol [1] is at " + str(value))
                    clock.tick(2)

                elif pat[1] == None:
                    pat[1] = value
                    print("patrol [2]  is at " + str(value))
                    clock.tick(2)
                elif des[0] == None:
                    des[0] = value
                    print("destroyer [1] is at " + str(value))
                    clock.tick(2)
                elif des[1] == None:
                    des[1] = value
                    print("destroyer [2] is at " + str(value))
                    clock.tick(2)
                elif des[2] == None:
                    des[2] = value
                    print("destroyer [3] is at " + str(value))
                    clock.tick(1)
                elif sub[0] == None:
                    sub[0] = value
                    print("submarine [1] is at " + str(value))
                    clock.tick(1)
                elif sub[1] == None:
                    sub[1] = value
                    print("submarine [2] is at " + str(value))
                    clock.tick(1)
                elif sub[2] == None:
                    sub[2] = value
                    print("submarine [3] is at " + str(value))
                    clock.tick(1)
                elif bat[0] == None:
                    bat[0] = value
                    print("battleship [1] is at " + str(value))
                    clock.tick(1)
                elif bat[1] == 0:
                    bat[1] = value
                    print("battleship [2] is at " + str(value))
                    clock.tick(1)
                elif bat[2] == None:
                    bat[2] = value
                    print("battleship [3] is at " + str(value))
                    clock.tick(1)
                elif bat[3] == None:
                    bat[3] = value
                    print("battleship [4] is at " + str(value))
                    clock.tick(1)
                elif car[0] == None:
                    car[0] = value
                    print("carrier [1] is at " + str(value))
                    clock.tick(1)
                elif car[1] == None:
                    car[1] = value
                    print("carrier [2] is at " + str(value))
                    clock.tick(1)
                elif car[2] == None:
                    car[2] = value
                    print("carrier [3] is at " + str(value))
                    clock.tick(1)
                elif car[3] == None:
                    car[3] = value
                    print("carrier [4] is at " + str(value))
                    clock.tick(1)
                elif car[4] == None:
                    car[4] = value
                    print("carrier [5] is at " + str(value))
                    clock.tick(1)
                else:
                    None

        pygame.display.update()
        pygame.display.flip()

    a = battleshipSultan.player()

    a.setShips(0, pat, des, sub, bat, car)


# REMOVE THIS WHEN DONE TESTING
# ship_placement()
gameon()
"""
patrol = 2
destroyer = 3
submarine = 3
battleship = 4
carrier =  5
"""