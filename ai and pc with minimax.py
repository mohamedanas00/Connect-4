for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()

    # # Ask for Player 1 Input
    if turn == PLAYER and not game_over:
        # Determine the PC's move
        if turn == PLAYER:
            # random_column = random.randint(0, 6)
            # board.select_column(random_column)
            # Use minimax to determine the best move for the PC
            # col = pick_best_move(board, turn, PLAYER)

            col, _ = minimax(board, 3, True)

        # else:
        # Use pick_best_move to determine the best move for the PC
        # col, _ = minimax(board, 5, -math.inf, math.inf, True)

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
                col, minimax_score = minimax(board, 3, False)

                # col = pick_best_move(board, AI, PLAYER)
            else:
                # Determine the AI's move using the minimax function
                col, minimax_score = minimax(board, 3, True)
            # col = pick_best_move(board, AI, PLAYER)

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