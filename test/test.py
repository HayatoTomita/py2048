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


def test_controll_case_1():
    input_array = np.array([[8, 0, 0, 0],
                             [0, 0, 0, 0],
                             [4, 4, 0, 0],
                             [0, 0, 0, 0]])
    result = np.array([[8, 0, 0, 0],
                       [0, 0, 0, 0],
                       [8, 0, 0, 0],
                       [0, 0, 0, 0]])
    direction = "LEFT"
    controlled, score, is_continue = board_array.controll(input_array, direction)
    assert np.allclose(controlled, result) and score == 4 and is_continue == True

def test_game_continue_not_over():
    input_array = np.array([[4, 2, 4, 2],
                            [2, 4, 2, 4],
                            [4, 2, 4, 2],
                            [2, 4, 4, 2]])
    is_gameover = board_array.check_game_continue(input_array)
    assert is_gameover == True

def test_game_continue_with_zero():
    input_array = np.array([[4, 2, 4, 2],
                            [2, 4, 2, 4],
                            [4, 2, 4, 2],
                            [2, 4, 2, 0]])
    is_gameover = board_array.check_game_continue(input_array)
    assert is_gameover == True

def test_game_continue_boardfull():
    input_array = np.array([[4, 2, 4, 2],
                            [2, 4, 2, 4],
                            [4, 2, 4, 2],
                            [2, 4, 2, 4]])
    is_gameover = board_array.check_game_continue(input_array)
    assert is_gameover == True