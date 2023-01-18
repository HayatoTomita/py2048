import numpy as np
from module import board_array


def test_pack_left():
    input_array = np.array([0, 0, 2, 0])
    result_array = np.array([2, 0, 0, 0])
    assert all(board_array.pack(input_array, "LEFT") == result_array)


def test_pack_rigth():
    input_array = np.array([0, 0, 2, 0])
    result_array = np.array([0, 0, 0, 2])
    assert all(board_array.pack(input_array, "RIGHT") == result_array)


def test_merge_left():
    input_array = np.array([2, 2, 0, 0])
    result_array = np.array([4, 0, 0, 0, 2])
    assert all(board_array.merge(input_array, "LEFT") == result_array)


def test_merge_rigth():
    input_array = np.array([0, 0, 2, 2])
    result_array = np.array([0, 0, 0, 4, 2])
    assert all(board_array.merge(input_array, "RIGHT") == result_array)


def test_merge_multi_three_left():
    input_array = np.array([2, 2, 2, 0])
    result_array = np.array([4, 0, 2, 0, 2])
    assert all(board_array.merge(input_array, "LEFT") == result_array)


def test_merge_multi_three_right():
    input_array = np.array([0, 2, 2, 2])
    result_array = np.array([0, 2, 0, 4, 2])
    assert all(board_array.merge(input_array, "RIGHT") == result_array)


def test_merge_multi_four_left():
    input_array = np.array([2, 2, 2, 2])
    result_array = np.array([4, 0, 4, 0, 4])
    assert all(board_array.merge(input_array, "LEFT") == result_array)


def test_merge_multi_four_right():
    input_array = np.array([2, 2, 2, 2])
    result_array = np.array([0, 4, 0, 4, 4])
    assert all(board_array.merge(input_array, "RIGHT") == result_array)
