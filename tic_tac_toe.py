board=[' ' for x in range(10)]


def insert_Letter(letter,pos):
    board[pos]=letter

def space_is_free(pos):
    return board[pos]==' '

def print_board(board):
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('----------')

def is_winner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7
                                                                                                                                                                                                                                                                                                                                                        ]==le)

def play_move():
    run=True
    while run:
        move=input('Please select a position to place \'X\' (1,9): ')
        try:
            move=int(move)
            if move>0 and move<10:
                if space_is_free(move):
                    run=False
                    insert_Letter('X',move)
                else:
                    print('Sorry, this place occupied')
            else:
                print("Please type a number within a range")
        except:
            print("Please type a number")

def comp_move():
    #The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
    possible_move=[x for x,letter in enumerate(board) if letter==' ' and x!=0]
    move=0
    for let in ['O','X']:
        for i in possible_move:
            board_copy=board[:]
            board_copy[i]=let
            if is_winner(board_copy,let):
                move=i
                return move
            
    corners_open=[]
    for i in possible_move:
        if i in [1,3,7,9]:
            corners_open.append(i)
    if len(corners_open)>0:
        move=select_random(corners_open)
        return move

    if 5 in possible_move:
        move=5
        return move
    
              
    edges_open=[]
    for i in possible_move:
        if i in [1,3,7,9]:
            edges_open.append(i)
    if len(edges_open)>0:
        move=select_random(edges_open)
        return move


def select_random(li):
    import random
    ln=len(li)
    r=random.randrange(1,ln)
    return li[r]

def is_board_full(board):
    if board.count(' ')>1:
        return True
    return False

def main():
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while (is_board_full(board)):
        if not (is_winner(board,'O')):
            play_move()
            print_board(board)
        else:
            print('O is winner') 
            break

        if not (is_winner(board,'X')):
            move=comp_move()
            if move==0:
                print("Tie game")
            else:
                insert_Letter('O',move)
                print("Computer placed an \'O\' at position ",move)
                print_board(board)
        else:
            print('X is winner') 
            break


if __name__=="__main__":
    main()

