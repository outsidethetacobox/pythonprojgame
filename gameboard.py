import pygame

pygame.init()
clock = pygame.time.Clock()
black = 0, 0, 0
blue = 0, 0, 255
violet_blue = 138, 43, 226
red = 255, 0, 0
dar_red = 139, 0, 0
clock = pygame.time.Clock()
Display = pygame.display.set_mode((800, 700))
F = pygame.font.SysFont("Times New Norman", 24)
classic = F.render("1", True, black)
classic2 = F.render("2", True, black)
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



# text , rect , color, hover color, x, h, y, w, action
buttons = [
    [classic, one_button, blue, violet_blue, 50, 20, 60, 40],
    [classic2, two_button, blue, violet_blue, 115, 20, 60, 40],
    [classic2, three_button, blue, violet_blue, 180, 20, 60, 40],
    [classic2, four_button, blue, violet_blue, 245, 20, 60, 40],
    [classic2, five_button, blue, violet_blue, 310, 20, 60, 40],
    [classic2, six_button, blue, violet_blue, 375, 20, 60, 40],
    [classic2, seven_button, blue, violet_blue, 440, 20, 60, 40],
    [classic2, eight_button, blue, violet_blue, 505, 20, 60, 40],
    [classic2, nine_button, blue, violet_blue, 570, 20, 60, 40],
    [classic2, ten_button, blue, violet_blue, 635, 20, 60, 40],
    [classic2, eleven_button, blue, violet_blue, 50, 65, 60, 40],
    [classic2, twelve_button, blue, violet_blue, 115, 65, 60, 40],
    [classic2, thirteen_button, blue, violet_blue, 180, 65, 60, 40],
    [classic2, fourteen_button, blue, violet_blue, 245, 65, 60, 40],
    [classic2, fiveteen_button, blue, violet_blue, 310, 65, 60, 40],
    [classic2, sixteen_button, blue, violet_blue, 375, 65, 60, 40],
    [classic2, seventeen_button, blue, violet_blue, 440, 65, 60, 40],
    [classic2, eightteen_button, blue, violet_blue, 505, 65, 60, 40],
    [classic2, nineteen_button, blue, violet_blue, 570, 65, 60, 40],
    [classic2, twenty_button, blue, violet_blue, 635, 65, 60, 40],
    [classic2, twone_button, blue, violet_blue, 50, 110, 60, 40],
    [classic2, twtwo_button, blue, violet_blue, 115, 110, 60, 40],
    [classic2, twthree_button, blue, violet_blue, 180, 110, 60, 40],
    [classic2, twfour_button, blue, violet_blue, 245, 110, 60, 40],
    [classic2, twfive_button, blue, violet_blue, 310, 110, 60, 40],
    [classic2, twsix_button, blue, violet_blue, 375, 110, 60, 40],
    [classic2, twseven_button, blue, violet_blue, 440, 110, 60, 40],
    [classic2, tweight_button, blue, violet_blue, 505, 110, 60, 40],
    [classic2, twnine_button, blue, violet_blue, 570, 110, 60, 40],
    [classic2, tty_button, blue, violet_blue, 635, 110, 60, 40],
    [classic2, ttyone_button, blue, violet_blue, 50, 155, 60, 40],
    [classic2, ttytwo_button, blue, violet_blue, 115, 155, 60, 40],
    [classic2, ttythree_button, blue, violet_blue, 180, 155, 60, 40],
    [classic2, ttyfour_button, blue, violet_blue, 245, 155, 60, 40],
    [classic2, ttyfive_button, blue, violet_blue, 310, 155, 60, 40],
    [classic2, ttysix_button, blue, violet_blue, 375, 155, 60, 40],
    [classic2, ttyseven_button, blue, violet_blue, 440, 155, 60, 40],
    [classic2, ttyeight_button, blue, violet_blue, 505, 155, 60, 40],
    [classic2, ttynine_button, blue, violet_blue, 570, 155, 60, 40],
    [classic2, ft_button, blue, violet_blue, 635, 155, 60, 40],
    [classic2, ftone_button, blue, violet_blue, 50, 200, 60, 40],
    [classic2, fttwo_button, blue, violet_blue, 115, 200, 60, 40],
    [classic2, ftthree_button, blue, violet_blue, 180, 200, 60, 40],
    [classic2, ftfour_button, blue, violet_blue, 245, 200, 60, 40],
    [classic2, ftfive_button, blue, violet_blue, 310, 200, 60, 40],
    [classic2, ftsix_button, blue, violet_blue, 375, 200, 60, 40],
    [classic2, ftseven_button, blue, violet_blue, 440, 200, 60, 40],
    [classic2, fteight_button, blue, violet_blue, 505, 200, 60, 40],
    [classic2, ftnine_button, blue, violet_blue, 570, 200, 60, 40],
    [classic2, fv_button, blue, violet_blue, 635, 200, 60, 40],
    [classic, fvone_button, blue, violet_blue, 50, 245, 60, 40],
    [classic2, fvtwo_button, blue, violet_blue, 115, 245, 60, 40],
    [classic2, fvthree_button, blue, violet_blue, 180, 245, 60, 40],
    [classic2, fvfour_button, blue, violet_blue, 245, 245, 60, 40],
    [classic2, fvfive_button, blue, violet_blue, 310, 245, 60, 40],
    [classic2, fvsix_button, blue, violet_blue, 375, 245, 60, 40],
    [classic2, fvseven_button, blue, violet_blue, 440, 245, 60, 40],
    [classic2, fveight_button, blue, violet_blue, 505, 245, 60, 40],
    [classic2, fvnine_button, blue, violet_blue, 570, 245, 60, 40],
    [classic2, sx_button, blue, violet_blue, 635, 245, 60, 40],
    [classic, sxone_button, blue, violet_blue, 50, 290, 60, 40],
    [classic2, sxtwo_button, blue, violet_blue, 115, 290, 60, 40],
    [classic2, sxthree_button, blue, violet_blue, 180, 290, 60, 40],
    [classic2, sxfour_button, blue, violet_blue, 245, 290, 60, 40],
    [classic2, sxfive_button, blue, violet_blue, 310, 290, 60, 40],
    [classic2, sxsix_button, blue, violet_blue, 375, 290, 60, 40],
    [classic2, sxseven_button, blue, violet_blue, 440, 290, 60, 40],
    [classic2, sxeight_button, blue, violet_blue, 505, 290, 60, 40],
    [classic2, sxnine_button, blue, violet_blue, 570, 290, 60, 40],
    [classic2, svn_button, blue, violet_blue, 635, 290, 60, 40],
    [classic, svnone_button, blue, violet_blue, 50, 335, 60, 40],
    [classic2, svntwo_button, blue, violet_blue, 115, 335, 60, 40],
    [classic2, svnthree_button, blue, violet_blue, 180, 335, 60, 40],
    [classic2, svnfour_button, blue, violet_blue, 245, 335, 60, 40],
    [classic2, svnfive_button, blue, violet_blue, 310, 335, 60, 40],
    [classic2, svnsix_button, blue, violet_blue, 375, 335, 60, 40],
    [classic2, svnseven_button, blue, violet_blue, 440, 335, 60, 40],
    [classic2, svneight_button, blue, violet_blue, 505, 335, 60, 40],
    [classic2, svnnine_button, blue, violet_blue, 570, 335, 60, 40],
    [classic2, ety_button, blue, violet_blue, 635, 335, 60, 40],
    [classic, etyone_button, blue, violet_blue, 50, 380, 60, 40],
    [classic2, etytwo_button, blue, violet_blue, 115, 380, 60, 40],
    [classic2, etythree_button, blue, violet_blue, 180, 380, 60, 40],
    [classic2, etyfour_button, blue, violet_blue, 245, 380, 60, 40],
    [classic2, etyfive_button, blue, violet_blue, 310, 380, 60, 40],
    [classic2, etysix_button, blue, violet_blue, 375, 380, 60, 40],
    [classic2, etyseven_button, blue, violet_blue, 440, 380, 60, 40],
    [classic2, etyeight_button, blue, violet_blue, 505, 380, 60, 40],
    [classic2, etynine_button, blue, violet_blue, 570, 380, 60, 40],
    [classic2, nty_button, blue, violet_blue, 635, 380, 60, 40],
    [classic, ntyone_button, blue, violet_blue, 50, 425, 60, 40],
    [classic2, ntytwo_button, blue, violet_blue, 115, 425, 60, 40],
    [classic2, ntythree_button, blue, violet_blue, 180, 425, 60, 40],
    [classic2, ntyfour_button, blue, violet_blue, 245, 425, 60, 40],
    [classic2, ntyfive_button, blue, violet_blue, 310, 425, 60, 40],
    [classic2, ntysix_button, blue, violet_blue, 375, 425, 60, 40],
    [classic2, ntyseven_button, blue, violet_blue, 440, 425, 60, 40],
    [classic2, ntyeight_button, blue, violet_blue, 505, 425, 60, 40],
    [classic2, ntynine_button, blue, violet_blue, 570, 425, 60, 40],
    [classic2, onehunny_button, blue, violet_blue, 635, 425, 60, 40],




]


def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()


def button_hover(button_x, button_w, button_y, button_h, disply, color, rect, text, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if button_x + button_w > mouse[0] > button_x and button_y + (button_h / 2) > mouse[1] > button_y:
        pygame.draw.rect(disply, hover_color, rect)
        Display.blit(text, rect)
    else:
        pygame.draw.rect(disply, color, rect)
        Display.blit(text, rect)


def gameon():
    gaming = True
    while gaming:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
        textsurf, textrect = text_objects("comp output bar", F)
        textrect.center = (400, 600)
        Display.blit(textsurf, textrect)
        for text, rect, color, hover, B_x, B_y, B_w, B_h in buttons:
            button_hover(B_x, B_h, B_y, B_w, Display, color, rect, text, hover)
        pygame.display.update()
        pygame.display.flip()


gameon()
pygame.QUIT