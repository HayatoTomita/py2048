from typing import Literal

import numpy as np


def add(a, b):
    return a + b


Direction = Literal["LEFT", "RIGHT"]


def pack(src: np.ndarray, pack_direction: Direction) -> np.ndarray:
    nonzero = np.nonzero(src)
    zero = np.where(src == 0)
    tmp = (nonzero, zero) if pack_direction == "LEFT" else (zero, nonzero)
    concatenated = np.concatenate(tmp, axis=1)[0]
    return src[concatenated]


def merge(src: np.ndarray, merge_direction: Direction) -> np.ndarray:
    if merge_direction == "RIGHT":
        src = src[::-1]

    for i in range(len(src) - 1):
        if src[i] == src[i + 1]:
            src[i] = src[i] * 2
            src[i + 1] = 0

    if merge_direction == "RIGHT":
        src = src[::-1]

    return src
