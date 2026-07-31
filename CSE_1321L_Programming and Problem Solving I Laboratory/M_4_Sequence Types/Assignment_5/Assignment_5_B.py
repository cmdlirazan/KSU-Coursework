#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 5B

import random

def create_board(width, height):
    board = []
    number_of_treasures = 0

    for _ in range(height):
        row = []
        for _ in range(width):
            if random.random() >= 0.7:
                row.append('T')
                number_of_treasures += 1
            else:
                row.append('O')
        board.append(row)

    return board, number_of_treasures

def print_board(board):
    for row in board:
        display_row = []
        for cell in row:
            if cell == 'T':
                display_row.append('O')
            else:
                display_row.append(cell)
        print(" ".join(display_row))

def play_game():
    width = int(input("Enter the width of the grid: "))
    height = int(input("Enter the height of the grid: "))

    board, number_of_treasures = create_board(width, height)
    undiscovered_treasures = number_of_treasures

    print(f"Number of treasures hidden: {number_of_treasures}")

    while undiscovered_treasures > 0:
        row = int(input(f"Enter the row number (0 to {height - 1}): "))
        col = int(input(f"Enter the column number (0 to {width - 1}): "))

        if board[row][col] == 'T':
            print("Congratulations! You found a treasure!")
            board[row][col] = 'X'
            undiscovered_treasures -= 1
            print_board(board)
        else:
            print("No treasure here, try again!")

    print("Congratulations! You've found all the treasures!")
    print_board(board)

play_game()