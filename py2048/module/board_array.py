from typing import Literal

import numpy as np

Direction = Literal["LEFT", "RIGHT", "TOP", "BOTTOM"]


def pack(
    src: np.ndarray, pack_direction: Direction, do_check: bool = False
) -> np.ndarray:
    nonzero = np.nonzero(src)
    zero = np.where(src == 0)
    tmp = (
        (nonzero, zero)
        if pack_direction == "LEFT" or pack_direction == "TOP"
        else (zero, nonzero)
    )
    concatenated = np.concatenate(tmp, axis=1)[0]
    result = src[concatenated]

    if not do_check:
        return result

    if all(src == result):
        result = np.append(result, 0)
    else:
        result = np.append(result, 1)

    return result


def merge(src: np.ndarray, merge_direction: Direction) -> np.ndarray:
    score = 0
    if merge_direction == "RIGHT" or merge_direction == "BOTTOM":
        src = src[::-1]

    for i in range(len(src) - 1):
        if src[i] == src[i + 1]:
            score += src[i]
            src[i] = src[i] * 2
            src[i + 1] = 0

    if merge_direction == "RIGHT" or merge_direction == "BOTTOM":
        src = src[::-1]

    src = np.append(src, score)
    return src


def get_spawn_idx(board: np.ndarray) -> np.ndarray:
    rows, cols = np.where(board == 0)
    idx = np.random.randint(0, len(rows))
    return np.array([rows[idx], cols[idx]])


def get_spawn_val() -> int:
    return np.random.randint(1, 3) * 2


def check_packed_board(
    board: np.ndarray, direction: Direction
) -> tuple[np.ndarray, bool]:
    if direction == "RIGHT" or direction == "LEFT":
        check_array = board[:, -1]
        checked = board[:, :-1]
    elif direction == "TOP" or direction == "BOTTOM":
        check_array = board[-1, :]
        checked = board[:-1, :]
    return checked, np.sum(check_array) != 0


def get_score(board: np.ndarray, direction: Direction) -> tuple[np.ndarray, int]:
    score = 0
    if direction == "RIGHT" or direction == "LEFT":
        scores = board[:, -1]
        scored = board[:, :-1]
    elif direction == "TOP" or direction == "BOTTOM":
        scores = board[-1, :]
        scored = board[:-1, :]

    score = np.sum(scores)
    return scored, score


def controll(board: np.ndarray, direction: Direction) -> tuple[np.ndarray, int, bool]:
    axis = 0 if direction == "TOP" or direction == "BOTTOM" else 1
    packed = np.apply_along_axis(
        pack, axis=axis, arr=board, pack_direction=direction, do_check=True
    )
    checked, is_continue = check_packed_board(packed, direction)
    merged = np.apply_along_axis(
        merge, axis=axis, arr=checked, merge_direction=direction
    )
    scored, score = get_score(merged, direction)
    if not is_continue and score == 0:
        return scored, 0, False
    result = np.apply_along_axis(
        pack, axis=axis, arr=scored, pack_direction=direction, do_check=False
    )
    return result, score, True


def init_board(board_size: int = 4) -> np.ndarray:
    board = np.zeros(board_size * board_size)
    board[0:2] = np.random.randint(1, 3) * 2
    np.random.shuffle(board)
    board = np.reshape(board, (board_size, board_size))
    return board
