from random import randint

# user will attack this board
attackCpuBoard = []

# cpu will attack this board
unseenboard =[]

# board that user will attack
for x in range(5):
    attackCpuBoard.append(["0"] * 5)

# board that cpu will attack
for i in range(5):
    unseenboard.append(["0"] * 5)

user_set_row = int(input("set row: "))
user_set_col = int(input("set col: "))

# print board that will show on screen that user will attack
def print_board(attackCpuBoard):
    for row in attackCpuBoard:
        print(" ".join(row))

# print board that cpu will attack
def cpu_attack_board(unseenboard):
    for hiderow in unseenboard:
        print(" ".join(hiderow))

print("Lets play battleship!")
print("below is what you attacked")
print_board(attackCpuBoard)
print()
print()
print("below is what cpu will attack")
cpu_attack_board(unseenboard)


# random define to place cpu ships
def random_row(attackCpuBoard):
    return randint(0, len(attackCpuBoard) - 1)

# random define to place cpu ships
def random_col(attackCpuBoard):
    return randint(0, len(attackCpuBoard[0]) - 1)
#=====================================================================================
#=====================================================================================
# use these functions also

# cpu picks random row for ship
def cpu_random_row(unseenboard):
    return randint(1, len(10))
# cpu picks random col for ship
def cpu_random_col(unseenboard):
    return randint(1, len(10))

#=====================================================================================
#=====================================================================================
    
# set cpu ships
cpu_set_ship_row = random_row(attackCpuBoard)
cpu_set_ship_col = random_col(attackCpuBoard)
print("cpu set row at: ", cpu_set_ship_row)
print("cpu set col at: ", cpu_set_ship_col)

# define algorithm for hitting multiple spots 
hit = False

turn = 1
while turn < 10:
    print()
    print("turn = ", turn)
    # USER TURN
    # user will guess a row to attack
    user_guess_row = int(input("guess row: "))
    user_guess_col = int(input("guess col: "))

    # if hit
    if user_guess_row == cpu_set_ship_row and user_guess_col == cpu_set_ship_col:
        print("Congrats you have sunk the cpu battleship!")
        break
    # if invalid
    else:
        if(user_guess_row < 0 or user_guess_row > 4) or (user_guess_col < 0 or user_guess_col > 4):
            print("value not in the ocean")
        elif(attackCpuBoard[user_guess_row][user_guess_col] == "X"):
            print("You have already guessed that")
            turn = turn - 1
        else:
            print("You missed the cpu battleship")
            attackCpuBoard[user_guess_row][user_guess_col] = "X"
    print_board(attackCpuBoard)

    #=====================================================================================
    #=====================================================================================
    #=====================================================================================
    # use from here onwards
    # each test is a different location to attack
                      
    # CPU TURN
    cpu_guess_row = cpu_random_row(unseenboard)
    cpu_guess_col = cpu_random_col(unseenboard)
    #cpu_guess_row = 2
    #cpu_guess_col = 2
    print("cpu guessed row: ", cpu_guess_row)
    print("cpu guessed col: ", cpu_guess_col)
    # if hit == true then smart attack will start
    # all test statements do the same thing but attack a different location
    if (hit == True):
        if (test == 1):
            # next turn user will get the remembered values and attack nearby
            temp = remember_row - 1
            if temp == user_set_row and remember_col == user_set_col:
                print("the cpu has hit a ship")
                print("tes1 hit")
                print("tmp = ", temp)
                print("rem_col = ", remember_col)
                # if hit then remember this as new location
                remember_row = temp
                remember_col = remember_col
                test = 1
            else:
                # if nearby value is out of area
                if (temp < 0 or temp > 4):
                    print("this number is not in the ocean")
                    # if not hit check next nearby location
                    test = 2
                    print("tes1 out")
                    print("tmp = ", temp)
                    print("rem_col = ", remember_col)
                    # check if new location is already hit
                elif (unseenboard[temp][remember_col] == "X"):
                    print("cpu has already guessed that")
                    test = 2
                    print("tes1 reguess")
                    print("tmp = ", temp)
                    print("rem_col = ", remember_col)   
                else:
                    # missed ship and mark as hit
                    print("missed battleship")
                    unseenboard[temp][remember_col] = "X"
                    test = 2
                    print("tes1 miss")
                    print("tmp = ", temp)
                    print("rem_col = ", remember_col)
        # if not hit at test 1 then attack test 2 next turn
        elif (test == 2):
            temp = remember_row + 1
            if temp == user_set_row and remember_col == user_set_col:
                print("the cpu has hit a ship")
                remember_row = temp
                remember_col = remember_col
                test = 1
                print("tes2 hit")
                print("tmp = ", temp)
                print("rem_col = ", remember_col)
            else:
                if (temp < 0 or temp > 4):
                    print("this number is not in the ocean")
                    test = 3
                    print("tes2 out")
                    print("tmp = ", temp)
                    print("rem_col = ", remember_col)
                elif (unseenboard[temp][remember_col] == "X"):
                    print("cpu has already guessed that")
                    test = 3
                    print("tes2 reguess")
                    print("tmp = ", temp)
                    print("rem_col = ", remember_col)
                else:
                    print("missed battleship")
                    unseenboard[temp][remember_col] = "X"
                    test = 3
                    print("tes2 miss")
                    print("tmp = ", temp)
                    print("rem_col = ", remember_col)
        elif (test == 3):
            temp = remember_col - 1
            if remember_row == user_set_row and temp == user_set_col:
                print("the cpu has hit a ship")
                remember_row = remember_row
                remember_col = temp
                test = 1
                print("tes2 hit")
                print("rem_row = ", remember_row)
                print("tmp = ", temp)
            else:
                if (temp < 0 or temp > 4):
                    print("this number is not in the ocean")
                    test = 4
                    print("tes3 out")
                    print("rem_row = ", remember_row)
                    print("tmp = ", temp)
                elif (unseenboard[remember_row][temp] == "X"):
                    print("cpu has already guessed that")
                    test = 4
                    print("tes3 reguess")
                    print("rem_row = ", remember_row)
                    print("tmp = ", temp)
                else:
                    print("missed battleship")
                    unseenboard[remember_row][temp] = "X"
                    test = 4
                    print("tes3 miss")
                    print("rem_row = ", remember_row)
                    print("tmp = ", temp)
        elif (test == 4):
            temp = remember_col + 1
            if remember_row == user_set_row and temp == user_set_col:
                print("the cpu has hit a ship")
                remember_row = remember_row
                remember_col = temp
                test = 1
                print("tes4 hit")
                print("rem_row = ", remember_row)
                print("tmp = ", temp)
            else:
                if (temp < 0 or temp > 4):
                    print("this number is not in the ocean")
                    hit = False
                    print("tes4 out")
                    print("rem_row = ", remember_row)
                    print("tmp = ", temp)
                elif (unseenboard[temp][remember_col] == "X"):
                    print("cpu has already guessed that")
                    hit = False
                    print("tes3 reguess")
                    print("rem_row = ", remember_row)
                    print("tmp = ", temp)
                else:
                    print("missed battleship")
                    unseenboard[temp][remember_col] = "X"
                    hit = False
                    print("tes3 miss")
                    print("rem_row = ", remember_row)
                    print("tmp = ", temp)
        
    else:
        # check if the cpu guesses correctly
        if cpu_guess_row == (object.pat and cpu_guess_col == user_set_col:
            print("The cpu has hit your battleship!")
            # remember these rows and columms to attack smart
            remember_row = cpu_guess_row
            remember_col = cpu_guess_col
            # ship has been hit so turn on smart mode
            hit = True
            # go to what the cpu should attack next
            test = 1
        else:
            # if this spot has already been attacked
            if (unseenboard[cpu_guess_row][cpu_guess_col] == "X"):
                print("The cpu has already guessed that")
                # keep attacking randomly so smart mode off
                hit = False
                test = 1
            else:
                # missed battlehip but mark this spot as attacked
                print("The cpu has missed your battleship")
                unseenboard[cpu_guess_row][cpu_guess_col] = "X"
                hit = False
                test = 1
                #print board
            cpu_attack_board(unseenboard)
    turn = turn + 1




#===========================================================================
#===========================================================================
def cpu_ship_placement(gameMode=None, a=object):
    # if game mode is classic, gameMode = 0
    # if salvo gameMode = 1
    arr = [False] * 100

    comp = battleshipSultan.player()

    cpupat = [None] * 2  # patrol
    cpudes = [None] * 3  # destroyer
    cpusub = [None] * 3  # submarine
    cpubat = [None] * 4  # battleship
    cpucar = [None] * 5  # carrier

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

        #for text, rect, color, hover, hit, miss, B_x, B_y, B_w, B_h, spot in buttons:
        value = set_cpu_ship()
        temp = value + 1
        cpupat[0] = 2
        #print("patrol [1] is at " + str(value))
        cpupat[1] = 3
        #print("patrol [2]  is at " + str(value))

        cpudes[0] = 16
        #print("destroyer [1] is at " + str(value))
        cpudes[1] = 17
        #print("destroyer [2] is at " + str(value))
        cpudes[2] = 18
        #print("destroyer [3] is at " + str(value))

        cpusub[0] = 31
        #print("submarine [1] is at " + str(value))
        cpusub[1] = 32
        #print("submarine [2] is at " + str(value))
        cpusub[2] = 33
        #print("submarine [3] is at " + str(value))

        cpubat[0] = 55
        #print("battleship [1] is at " + str(value))
        cpubat[1] = 56
        #print("battleship [2] is at " + str(value))
        cpubat[2] = 57
        #print("battleship [3] is at " + str(value))
        cpubat[3] = 58
        #print("battleship [4] is at " + str(value))

        cpucar[0] = 86
        #print("carrier [1] is at " + str(value))
        cpucar[1] = 87
        #print("carrier [2] is at " + str(value))
        cpucar[2] = 88
        #print("carrier [3] is at " + str(value))
        cpucar[3] = 89
        #print("carrier [4] is at " + str(value))
        cpucar[4] = 90
        #print("carrier [5] is at " + str(value))


        pygame.display.update()
        pygame.display.flip()

    # Check THIS
    a.setShips(0, pat, des, sub, bat, car)


# REMOVE THIS WHEN DONE TESTING
# ship_placement()

# =================================================================================================================================
# =================================================================================================================================

    
            
        

                          
        
                 
