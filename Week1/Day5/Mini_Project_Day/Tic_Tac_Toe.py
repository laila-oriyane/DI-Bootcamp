# Step 1: Representing the Game Board
board = [" " for _ in range(9) ] 

# Step 2: Displaying the Game Board
def display_board(board) :
    print()
    print(board[0] +" | "+ board[1] +" | "+ board[2] )
    print("--+---+--")
    print(board[3] +" | "+ board[4] +" | "+ board[5] )
    print("--+---+--")
    print(board[6] +" | "+ board[7] +" | "+ board[8] )
    print()
display_board(board)

# Step 3: Getting Player Input
def player_input(board,player) :
    while True:
        position = int(input(f"{player}, choose a position (1-9) : ")) - 1
        if position < 0 or position > 8 :
            print(" Please choose a number between 1 and 9.")
        elif board[position] != " " :
            print("That spot is already taken.")
        else :
            board[position]=player
            break
        
# Step 4: Checking for a Winner
def check_win(board,player) :
    win_combos=[
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8], #columns
        [0,4,8],[2,4,6] #diagonal
    ]
    for combo in win_combos :
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player :
            return True
    return False

# Step 5: Checking for a Tie 
def check_tie(board) :
    return " " not in board

# Step 6: The Main Game Loop
def play() :
    board = [" " for _ in range(9) ] 
    current_player = "X"

    while True:
        display_board(board)
        player_input(board,current_player)

        if check_win(board,current_player) :
            display_board(board)
            print(f"Current player {current_player} wins!")
            break
        
        if check_tie(board) :
            display_board(board)
            print("it's a tie!")
            break

        #switch player  
        if current_player == "X" :
            current_player = "O"
        else :
            current_player ="X" 

# Running the app 
if __name__ == "__main__":
    play()

        



    