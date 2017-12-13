import random

#makes a board
board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

sank_ships = 0

print "Let's play Battleship!"
print_board(board)

#general set up
ships = []
#a list of lists that hold the placement values for all the ships

def random_pos(board):
    return random.randint(0, len(board) - 1)

def border_x(row1, col1, topleft_border, bottomright_border):
    if row1 in topleft_border:
        row2 = row1 + 1
        col2 = col1
        return [row2, col2]
    elif row1 in bottomright_border:
        row2 = row1 - 1
        col2 = col1
        return [row2, col2]
        # checks if ship is on edge of board or will run into it
        # assigns col to go up or down if so
    elif col1 in topleft_border or col1 in bottomright_border:
        return border_y(row1, col1, topleft_border, bottomright_border)
    else:
        return random.choice([row_placement(row1, col1), col_placement(row1, col1)])
        # if not on y border or x border, assigns random new adjacent x or y values

def border_y(row1, col1, topleft_border, bottomright_border):
    if col1 in topleft_border:
        col2 = col1 + 1
        row2 = row1
        return [row2, col2]
    elif col1 in bottomright_border:
        col2 = col1 - 1
        row2 = row1
        return [row2, col2]
    elif row1 in topleft_border or row1 in bottomright_border:
        return border_x(row1, col1, topleft_border, bottomright_border)
    else:
        return random.choice([row_placement(row1, col1), col_placement(row1, col1)])

def row_placement(row1, col1):
    row2 = row1 + random.choice([1, -1])
    col2 = col1
    return [row2, col2]

def col_placement(row1, col1):
    col2 = col1 + random.choice([1, -1])
    row2 = row1
    return [row2, col2]

#ship1(aircraftcarrier) placement
topleft_border = [0, 1, 2, 3]
bottomright_border = [6, 7, 8, 9]

ship1a_col = random_pos(board)
ship1a_row = random_pos(board)

ship1b_row = None
ship1b_col = None

place_b = [(border_y(ship1a_row, ship1a_col, topleft_border, bottomright_border)), (border_x(ship1a_row, ship1a_col, topleft_border, bottomright_border))]
ship1b = random.choice(place_b)
#list made because random.choice prefers to choose from a pre-made list
ship1b_row = ship1b[0]
ship1b_col = ship1b[1]
# chooses x or y axis and assigns the second coordinate of the ship on that axis

if ship1b_col > ship1a_col:
    ship1c_col = ship1b_col + 1
    ship1d_col = ship1c_col + 1
    ship1e_col = ship1d_col + 1
    ship1b_row = ship1c_row = ship1d_row = ship1e_row = ship1a_row
elif ship1b_col < ship1a_col:
    ship1c_col = ship1b_col - 1
    ship1d_col = ship1c_col - 1
    ship1e_col = ship1d_col - 1
    ship1b_row = ship1c_row = ship1d_row = ship1e_row = ship1a_row
if ship1b_row > ship1a_row:
    ship1c_row = ship1b_row + 1
    ship1d_row = ship1c_row + 1
    ship1e_row = ship1d_row + 1
    ship1b_col = ship1c_col = ship1d_col = ship1e_col = ship1a_col
elif ship1b_row < ship1a_row:
    ship1c_row = ship1b_row - 1
    ship1d_row = ship1c_row - 1
    ship1e_row = ship1d_row - 1
    ship1b_col = ship1c_col = ship1d_col = ship1e_col = ship1a_col
# adds the rest of the coordinates for ship

ship1 = [[ship1a_row, ship1a_col], [ship1b_row, ship1b_col], [ship1c_row, ship1c_col], [ship1d_row, ship1d_col], [ship1e_row, ship1e_col]]
ships.append(ship1)
# adds ship to ships list of coordinates to check

#ship2(battleship)
topleft_border = [0, 1, 2]
bottomright_border = [7, 8, 9]

ship2a_row = None
ship2a_col = None
ship2b_row = None
ship2b_col = None
ship2c_row = None
ship2c_col = None
ship2d_row = None
ship2d_col = None

def place_ship2():
    ship2 = [[ship2a_row, ship2a_col], [ship2b_row, ship2b_col], [ship2c_row, ship2c_col], [ship2d_row, ship2d_col]]
    global ship2
    global ship2a_row
    global ship2a_col
    global ship2b_row
    global ship2b_col
    global ship2c_row
    global ship2c_col
    global ship2d_row
    global ship2d_col

    ship2a_col = random_pos(board)
    ship2a_row = random_pos(board)

    place_b = [(border_y(ship2a_row, ship2a_col, topleft_border, bottomright_border)), (border_x(ship2a_row, ship2a_col, topleft_border, bottomright_border))]
    ship2b = random.choice(place_b)
    ship2b_row = ship2b[0]
    ship2b_col = ship2b[1]

    if ship2b_col > ship2a_col:
        ship2c_col = ship2b_col + 1
        ship2d_col = ship2c_col + 1
        ship2b_row = ship2c_row = ship2d_row = ship2a_row
    elif ship2b_col < ship2a_col:
        ship2c_col = ship2b_col - 1
        ship2d_col = ship2c_col - 1
        ship2b_row = ship2c_row = ship2d_row = ship2a_row
    elif ship2b_row > ship2a_row:
        ship2c_row = ship2b_row + 1
        ship2d_row = ship2c_row + 1
        ship2b_col = ship2c_col = ship2d_col = ship2a_col
    elif ship2b_row < ship2a_row:
        ship2c_row = ship2b_row - 1
        ship2d_row = ship2c_row - 1
        ship2b_col = ship2c_col = ship2d_col = ship2a_col
    ship2 = [[ship2a_row, ship2a_col], [ship2b_row, ship2b_col], [ship2c_row, ship2c_col], [ship2d_row, ship2d_col]]
    return ship2

place_ship2()

def check2():
    for coordinate in ship2:
        if coordinate in ship1:
            place_ship2()
            print 'ship2 after reprint'
            check2()
check2()

# for i in ship2:
#     while i in ships:
#         ship2a_col = random_pos(board)
#         ship2a_row = random_pos(board)

ships.append(ship2)

#ship3(submarine)
topleft_border = [0, 1]
bottomright_border = [6, 7]

ship3a_row = None
ship3a_col = None
ship3b_row = None
ship3b_col = None
ship3c_row = None
ship3c_col = None

def place_ship3():
    ship3 = [[ship3a_row, ship3a_col], [ship3b_row, ship3b_col], [ship3c_row, ship3c_col]]
    global ship3
    global ship3a_row
    global ship3a_col
    global ship3b_row
    global ship3b_col
    global ship3c_row
    global ship3c_col

    ship3a_col = random_pos(board)
    ship3a_row = random_pos(board)
    # while [ship3a_row, ship3a_col] in ship1 or [ship3a_row, ship3a_col] in ship2:
    #     ship3a_row = random_pos(board)
    #     ship3a_col = random_pos(board)
    #     print 'ship3a reprint'

    place_b = [(border_y(ship3a_row, ship3a_col, topleft_border, bottomright_border)), (border_x(ship3a_row, ship3a_col, topleft_border, bottomright_border))]
    ship3b = random.choice(place_b)
    ship3b_row = ship3b[0]
    ship3b_col = ship3b[1]

    if ship3b_col > ship3a_col:
        ship3c_col = ship3b_col + 1
        ship3b_row = ship3c_row = ship3a_row
    elif ship3b_col < ship3a_col:
        ship3c_col = ship3b_col - 1
        ship3b_row = ship3c_row = ship3a_row
    elif ship3b_row > ship3a_row:
        ship3c_row = ship3b_row + 1
        ship3b_col = ship3c_col = ship3a_col
    elif ship3b_row < ship3a_row:
        ship3c_row = ship3b_row - 1
        ship3b_col = ship3c_col = ship3a_col
    ship3 = [[ship3a_row, ship3a_col], [ship3b_row, ship3b_col], [ship3c_row, ship3c_col]]

place_ship3()

def check3():
    for coordinate in ship3:
        if coordinate in ship1 or coordinate in ship2:
            place_ship3()
            print 'ship3 after reprint'
            check3()
check3()

ships.append(ship3)

#ship4(cruiser)
ship4a_row = None
ship4a_col = None
ship4b_row = None
ship4b_col = None
ship4c_row = None
ship4c_col = None

def place_ship4():
    ship4 = [[ship4a_row, ship4a_col], [ship4b_row, ship4b_col], [ship4c_row, ship4c_col]]
    global ship4
    global ship4a_row
    global ship4a_col
    global ship4b_row
    global ship4b_col
    global ship4c_row
    global ship4c_col
    ship4a_row = random_pos(board)
    ship4a_col = random_pos(board)
    # while [ship4a_row, ship4a_col] in ship1 or [ship4a_row, ship4a_col] in ship2 or [ship4a_row, ship4a_col] in ship3:
    #     ship4a_row = random_pos(board)
    #     ship4a_col = random_pos(board)
    #     print 'ship4 reprint'

    place_b = [(border_y(ship4a_row, ship4a_col, topleft_border, bottomright_border)), (border_x(ship4a_row, ship4a_col, topleft_border, bottomright_border))]
    ship4b = random.choice(place_b)
    ship4b_row = ship4b[0]
    ship4b_col = ship4b[1]

    if ship4b_col > ship4a_col:
        ship4c_col = ship4b_col + 1
        ship4b_row = ship4c_row = ship4a_row
    elif ship4b_col < ship4a_col:
        ship4c_col = ship4b_col - 1
        ship4b_row = ship4c_row = ship4a_row
    elif ship4b_row > ship4a_row:
        ship4c_row = ship4b_row + 1
        ship4b_col = ship4c_col = ship4a_col
    elif ship4b_row < ship4a_row:
        ship4c_row = ship4b_row - 1
        ship4b_col = ship4c_col = ship4a_col
    ship4 = [[ship4a_row, ship4a_col], [ship4b_row, ship4b_col], [ship4c_row, ship4c_col]]
    return ship4

place_ship4()

def check4():
    for coordinate in ship4:
        if coordinate in ship1 or coordinate in ship2 or coordinate in ship3:
            place_ship4()
            print 'ship4 after reprint'
            check4()
check4()

ships.append(ship4)

#ship5(destroyer)
topleft_border = [0]
bottomright_border = [6]

ship5a_row = None
ship5a_col = None
ship5b_row = None
ship5b_col = None

def place_ship5():
    ship5 = [[ship5a_row, ship5a_col], [ship5b_row, ship5b_col]]
    global ship5
    global ship5a_row
    global ship5a_col
    global ship5b_row
    global ship5b_col
    ship5a_row = random_pos(board)
    ship5a_col = random_pos(board)
    # while [ship5a_row, ship5a_col] in ship1 or [ship5a_row, ship5a_col] in ship2 or [ship5a_row, ship5a_col] in ship3 or [ship5a_row, ship5a_col] in ship4:
    #     ship5a_row = random_pos(board)
    #     ship5a_col = random_pos(board)
    #     print 'ship5 reprint'

    place_b = [(border_y(ship5a_row, ship5a_col, topleft_border, bottomright_border)), (border_x(ship5a_row, ship5a_col, topleft_border, bottomright_border))]
    ship5b = random.choice(place_b)
    ship5b_row = ship5b[0]
    ship5b_col = ship5b[1]

    ship5 = [[ship5a_row, ship5a_col], [ship5b_row, ship5b_col]]

place_ship5()

def check5():
    for coordinate in ship5:
        if coordinate in ship1 or coordinate in ship2 or coordinate in ship3 or coordinate in ship4:
            place_ship5()
            print 'ship5 after reprint'
            check5()
check5()

ships.append(ship5)

print ship1
print ship2
print ship3
print ship4
print ship5
print ships

def user_turn():
    miss = 0
    def check_hit(ship):
        global sank_ships
        ship_length = len(ship)
        hits = 0
        print hits
        print ship

        for pair in ship:
            if board[pair[0]][pair[1]] == "X":
                hits += 1
                if hits == ship_length:
                    ships.remove(ship)
                    sank_ships += 1
                    print sank_ships

    for turn in range(50):
        guess_row = int(raw_input("Guess Row:"))
        if guess_row not in range(0, 10, 1):
            print "That's not part of the board! Please guess integers 0-9"
            user_turn()

        guess_col = int(raw_input("Guess Col:"))
        if guess_col not in range(0, 10, 1):
            print "That's not part of the board! Please guess integers 0-9"
            user_turn()

        if board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "M":
            print "You guessed that one already."
            # checks old guesses based on "X" or "M" placed

        for ship in ships:
            for pair in ship:
                if pair == [guess_row, guess_col]:
                    print "You hit my ship!"
                    board[guess_row][guess_col] = "X"

            check_hit(ship)
        # for ship in ships:
        #     ship_length = len(ship)
        #     hits = 0
        #     for pair in ship:
        #         if board[pair[0]][pair[1]] == "X":
        #             hits += 1
        #             if hits >= ship_length:
        #                 print "You sank my ship!"
            # for pair in ship1:
            #     sank_ships = check_hit(sank_ships)
            #     # if board[pair[0]][pair[1]] == "X":
            #     #     hits += 1
            #     #     if hits >= ship_length:
            #     #         sank_ships += 1
            # for pair in ship2:
            #     if board[pair[0]][pair[1]] == "X":
            #         hits += 1
            #         if hits >= ship_length:
            #             sank_ships += 1
            # for pair in ship3:
            #     if board[pair[0]][pair[1]] == "X":
            #         hits += 1
            #         if hits >= ship_length:
            #             sank_ships += 1
            # for pair in ship4:
            #     if board[pair[0]][pair[1]] == "X":
            #         hits += 1
            #         if hits >= ship_length:
            #             sank_ships += 1
            # for pair in ship5:
            #     sank_ships = check_hit(sank_ships)
                # if board[pair[0]][pair[1]] == "X":
                #     hits += 1
                #     if hits >= ship_length:
                #         sank_ships += 1
        plural = '' if sank_ships == 1 else 's'
        message = 'You have sunk %d ship%s.'
        print (message % (sank_ships, plural))
        if sank_ships >= 5:
            print "You Win!"
            print_board(board)
            break

        if guess_row < 0 or guess_row > 10 or guess_col < 0 or guess_col > 10:
            print "Oops, that's not even in the ocean."
            # determines if guess is outside game board without starting the game over

        elif board[guess_row][guess_col] == "O":
            print "You missed my ship!"
            board[guess_row][guess_col] = "M"
            # replaces "O" with "M" on game board to show guesses
            message = "You have %d miss%s left."
            miss += 1
            plural = '' if miss == 9 else 'es'
            count = 10 - miss
            print (message % (count, plural))
        # shows user what turn they are on, gives game over condition
        if miss == 10:
            print "Game Over"
            print_board(board)
            break

        print_board(board)
        # shows inputs so far
user_turn()

        # for i in ship2:
        #     if board[i] == "X":
        #         print "You sank my ship!"
        # for i in ships:
        #     if board[i, i] != "X":
        #         print "There are still more ships."
            #this will need work- dont know how this works for a list of lists. dont know how to make it check every i in list before printing you win.
            # checks if user has sunk all ships, then breaks loop if so

            # if guess_row == ship1_row and guess_col == ship1_col\
            # or guess_row == ship2_row and guess_col == ship2_col\
            # or guess_row == ship3_row and guess_col == ship3_col:
                # if [guess_row, guess_col] in ship1 or [guess_row, guess_col] in ship2 or [guess_row, guess_col] in ship3 or [guess_row, guess_col] in ship4 or [guess_row, guess_col] in ship5:
                #     board[guess_row][guess_col] = "X"
                #     print guess_row, guess_col
                #     print "You hit my ship!"
                #     print_board(board)
                # if [ship1_row,ship1_col] == "S" and\
                # [ship2_row,ship2_col] == "S" and\
                # [ship3_row,ship3_col] == "S":

# to fix - user input sting, or blank
#    - y and x inputs are switched- fix that

# # Make your game a two-player game.
#
# # Use functions to allow your game to have more features like rematches,
# # statistics and more!
