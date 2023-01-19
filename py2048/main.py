import curses
import datetime
import json
import os

import numpy as np

from module.board_array import (Direction, check_game_continue, controll,
                                get_spawn_idx, get_spawn_val, init_board)


def main(stdscr):
    curses.initscr()
    board = init_board()

    rows, cols = board.shape
    total_score = 0
    turn = 0
    game_history: dict = {}

    dt_now = datetime.datetime.now()
    logdir = "gamelogs/{}".format(dt_now.strftime("%Y-%m-%d-%H-%M-%S"))
    os.makedirs(logdir, exist_ok=True)
    np.savetxt(os.path.join(logdir, "initial_board.csv"), board)

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
        else:
            continue

        board, score, is_continue = controll(board, direction)

        if not is_continue:
            continue

        total_score += score
        spawn_idx = get_spawn_idx(board)
        spawn_val = get_spawn_val()

        game_history[turn] = {
            "direction": direction,
            "spawn_idx_row": int(spawn_idx[0]),
            "spawn_idx_col": int(spawn_idx[1]),
            "spawn_val": spawn_val,
        }

        board[tuple(spawn_idx)] = spawn_val
        turn += 1

    np.savetxt(os.path.join(logdir, "last_board.csv"), board)
    stdscr.addstr(10, 1, "GAME OVER. PRESS ANY KEY")
    stdscr.getch()
    game_history["score"] = total_score
    with open(os.path.join(logdir, "controll_log.json"), "w") as f:
        json.dump(game_history, f, indent=2)


if __name__ == "__main__":
    curses.wrapper(main)
