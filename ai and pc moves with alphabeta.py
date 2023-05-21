def pick_best_move(board, player, opponent):
    """
    Determines the best move for the given player using a heuristic function.
    """
    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)

    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, player)
        score = score_position(temp_board, player, opponent)

        if score > best_score:
            best_score = score
            best_col = col

    return best_col

def alphabeta(board, depth, alpha, beta, maximizingPlayer):#alphabeta
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_PIECE,PLAYER))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = alphabeta(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = alphabeta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
turn = random.randint(PLAYER, AI)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # # Ask for Player 1 Input
        if turn == PLAYER and not game_over:
            # Determine the PC's move
            if turn == PLAYER:

              col, _ = alphabeta(board, 5, -math.inf, math.inf, True)

            col = pick_best_move(board, turn, PLAYER)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)
                time.sleep(2)

                if winning_move(board, PLAYER_PIECE):
                    label = myfont.render("PC wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

                turn += 1
                turn = turn % 2

                print_board(board)
                draw_board(board)
            # # Ask for Player 2 Input
            if turn == AI and not game_over:
                if AI == PLAYER:
                    # Determine the AI's move using the pick_best_move function
                    col, minimax_score = alphabeta(board, 5, -math.inf, math.inf, False)

                else:
                    # Determine the AI's move using the minimax function
                     col, minimax_score = alphabeta(board, 5, -math.inf, math.inf, True)


                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, AI_PIECE)
                    time.sleep(2)

                    if winning_move(board, AI_PIECE):
                        label = myfont.render("AI wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn += 1
                    turn = turn % 2

                    print_board(board)
                    draw_board(board)
    if game_over:
        pygame.time.wait(3000)
