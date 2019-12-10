# -*- coding: utf-8 -*-

"""
Created on Mon Dec  2 21:38:18 2019

@author: Christian
"""


import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt


def gen_puzzle(columns, rows, original_image):
    slicing_vertically = np.split(original_image, rows)
    row_counter = 0
    pieces_puzzle = np.zeros([columns * rows, int(original_image.shape[0] / rows), int(
        original_image.shape[1] / columns), 3], dtype=int)
    for slice in slicing_vertically:
        slicing_horizontally = np.hsplit(slice, columns)
        for horizontal in slicing_horizontally:
            pieces_puzzle[row_counter] = horizontal
            row_counter += 1
    return pieces_puzzle


def shuffle_puzzle(columns, rows, original_image):
    puzzle = gen_puzzle(columns, rows, original_image)
    np.random.shuffle(puzzle)
    return puzzle


def interchange_positions_of_pieces(old_position, new_position, puzzle):
    cp_puzzle = np.copy(puzzle)
    puzzle[old_position] = puzzle[new_position]
    puzzle[new_position] = cp_puzzle[old_position]
    return puzzle


def show_puzzle(columns, rows, original_image, pieces_puzzle):
    puzzle_for_show = np.zeros([rows, int(
        original_image.shape[0] / rows), original_image.shape[1], 3], dtype=int)
    for i in range(1, rows + 1):
        puzzle_for_show[i -
                        1] = np.concatenate(pieces_puzzle[(i - 1) * columns: i * columns], 1)
    puzzle_for_showing = np.concatenate(puzzle_for_show, 0)
    return puzzle_for_showing


def print_matrix_puzzle(columns, rows):
    counter = 0
    string_row = ""
    for row in range(rows):
        for iterab in range(columns):
            string_row += "|" + str(counter + 1) + "\t"
            counter += 1
        print(string_row)
        string_row = ""


def check_for_completed(original_image, puzzled_image):
    return np.array_equal(original_image, puzzled_image)


image = misc.face()  # Imagen con la que se trabajara el rompezacebzas
columns = input("Número de columnas: ")
rows = input("Número de filas: ")
puzzle = show_puzzle(int(columns), int(rows), image,
                     shuffle_puzzle(int(columns), int(rows), image))
plt.imshow(puzzle)
plt.show()
showing_new_puzzle = puzzle
while not check_for_completed(image, showing_new_puzzle):
    try:
        old_position = int(input("Posición inicial: "))
        new_position = int(input("Posición final:"))
        print(f"Se intercambiaron las posicione: {old_position} con la posición: {new_position}")
        new_puzzle = gen_puzzle(int(columns), int(rows), showing_new_puzzle)
        new_puzzle = interchange_positions_of_pieces(
            old_position - 1, new_position - 1, new_puzzle)
        showing_new_puzzle = show_puzzle(
            int(columns), int(rows), puzzle, new_puzzle)
        plt.imshow(showing_new_puzzle)
        plt.show()
    except:
        print("Intentelo de nuevo...")
print("COMPLETADO!!")