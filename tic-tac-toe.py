#Build a tic tac toe game to learn coding in python
#need board
#--------Global variables ---------
board = ["-", "-", "-"
         ,"-", "-", "-"
         ,"-", "-", "-"]
#If game is still going
game_still_going = True
#Who won
winner = None

#Who is currently playing
current_player = "X"

#display board
#declaring a function to display the board
def display_board():            #Has zero indexing
    print(board[0] +  " | "  + board[1] +  " | "  + board[2])
    print(board[3] +  " | "  + board[4] +  " | "  + board[5])
    print(board[6] +  " | "  + board[7] +  " | "  + board[8])

#play game
def play_game():
    #Global Variables
    global current_player

    #Display the initial board
    display_board() 

    #Handling the turns of the players-Loop through turns
    while game_still_going:
        #Handling the turns
        handle_turn(current_player)
        #Check if the game has ended
        check_if_game_over()
        #switching between players
        flip_player()

    #The game has ended
    if winner == "X" or winner == "O":
             print(winner + " Won!!")
    elif winner == None:
         print("Its a Tie!!")     

#-----------Sub functions----------------
#Check whether the game is over
def check_if_game_over():
    check_if_win()

    check_if_tie()

#Checking if there is a win
def check_if_win():

        #Set up global variables
        global winner
        global game_still_going

        #check rows
        row_winner = check_rows()
        #check columns        
        column_winner = check_columns()        
        #check diagonals
        diagonal_winner = check_diagonals()


        
        if row_winner:
             #there was a win
            winner = row_winner
        elif column_winner:
             #there is a win
            winner = column_winner
        elif diagonal_winner:
             #there is a win
            winner = diagonal_winner
        else:
            winner = None   
        return

def check_rows():         
    #Global Variables
    global game_still_going

     
    #Check if any of the rows have the same values
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    #if any row has a match
    if row1 or row2 or row3:
        game_still_going = False
    #Return what won X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():

    #Global Variables
    global game_still_going

    #Check if any of the cols have the same value
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    #if any col has won, stop the game
    if col1 or col2 or col3:
         game_still_going = False

    #Check hwo won if X or O
    if col1:
         return board[0]
    elif col2:
         return board[1]
    elif col3:
         return board[2]
    return

def check_diagonals():

    #Global Variables
    global game_still_going

    #Check if any diagonals won
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[6] == board[4] == board[2] != "-"

    #If there is a win, stop the game
    if dia1 or dia2:
         game_still_going = False

    #Checking what won X or O
    if dia1:
         return board[0]
    elif dia2:
         return board[6]
    return
#Checking if there is a tie
def check_if_tie():
    #Global Variables
    global winner 
    global game_still_going   

    #check if board is full and there is no winner
    if "-" not in board and winner == None:
         game_still_going = False
    
    return

#Switching the player
def flip_player():
    #Global Variables\
    global current_player

    #If the current player is X, Change it to O
    if current_player == "X":
        current_player = "O"
    #If the current player is O, Change it to X
    elif current_player == "O":
         current_player = "X"
        
    return

#Handle a turn form a single player
def handle_turn(player):

    #Showing whose turn it is
    print(player + "'s turn")

    #Handling intputs
    position = input("Choose the position from 1-9: ")

    #Validate the input
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6" , "7", "8", "9"]:
            position = input("Wrong Input!! Enter 1 to 9: ")

        #Casting the input to integer
        position = int(position) - 1

        #Putting something into the board   
        if board[position] == "-":
            valid = True
        else:
            print("Spot already taken, Go Again")
            

    board[position] = player

    display_board()

#---------------Starting the game----------------
play_game()


