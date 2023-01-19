import curses

from module.board_array import (Direction, check_game_continue, controll,
                                get_spawn_idx, get_spawn_val, init_board)


def main(stdscr):
    curses.initscr()
    board = init_board()

    rows, cols = board.shape
    total_score = 0
    turn = 0
    # Clear screen
    while check_game_continue(board):
        stdscr.clear()
        stdscr.addstr(0, 0, "Turn : {}".format(turn))
        stdscr.addstr(0, 10, "SCORE : {}".format(total_score))

        for row in range(rows):
            for col in range(cols):
                stdscr.addstr(
                    1 + 2 * row, col + 4 * (col + 1), "{}".format(int(board[row][col]))
                )

        c = stdscr.getch()

        direction: Direction
        if c == ord("w"):
            direction = "TOP"
        elif c == ord("a"):
            direction = "LEFT"
        elif c == ord("s"):
            direction = "BOTTOM"
        elif c == ord("d"):
            direction = "RIGHT"

        board, score, is_continue = controll(board, direction)
        stdscr.addstr(0, 30, "is_continue : {}".format(is_continue))
        if not is_continue:
            continue

        total_score += score
        spawn_idx = get_spawn_idx(board)
        board[tuple(spawn_idx)] = get_spawn_val()
        turn += 1


if __name__ == "__main__":
    curses.wrapper(main)
