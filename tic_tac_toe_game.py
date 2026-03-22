"""
An implementation of the Tic Tac Toe game, developed as an exercise for the Python online course.
Coded from the ground up without using the course's sample solution.

Author: Ignacio Martinez
Last updated: 2026-03-22
"""

# Global variables

field = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# I created a single list so that items could be accessed directly via their index. An alternative would have been to create three lists, one for each row or column, but this would have added an extra step to the access procedure.

# Renders the current state of the game board.
def game_board():

    for item in range(len(field)):
    # Own words: len() makes the entire list available to range().

        if item in [2, 5, 8]:
        # 2, 5, 8 are the indexes of the list items that need to have a line break right after them so that the game board displays properly.

            print(field[item])

        else:

            print(field[item], end=" | ")
            # Prints a pipe separator after the remaining numbers to complete the display of the game board.

game_board()

# Evaluates whether user input is a valid move.
def move():

    # Counter variable
    counter_odd_even = 1

    while True:

        # What follows checks if, before their next move, one of the two players has already won. This approach is lengthy and requires a lot of code.
        if all(field[i] == "X" for i in [0, 1, 2]) or all(field[i] == "X" for i in [3, 4, 5]) or all(field[i] == "X" for i in [6, 7, 8]) or all(field[i] == "X" for i in [0, 3, 6]) or all(field[i] == "X" for i in [1, 4, 7]) or all(field[i] == "X" for i in [2, 5, 8]) or all(field[i] == "X" for i in [0, 4, 8]) or all(field[i] == "X" for i in [2, 4, 6]):

            print("SPIELER 1, du hast gewonnen!")

            break

        elif all(field[i] == "O" for i in [0, 1, 2]) or all(field[i] == "O" for i in [3, 4, 5]) or all(field[i] == "O" for i in [6, 7, 8]) or all(field[i] == "O" for i in [0, 3, 6]) or all(field[i] == "O" for i in [1, 4, 7]) or all(field[i] == "O" for i in [2, 5, 8]) or all(field[i] == "O" for i in [0, 4, 8]) or all(field[i] == "O" for i in [2, 4, 6]):

            print("SPIELER 2, du hast gewonnen!")

            break

        elif counter_odd_even % 2 == 1:
        # If the value of the counter variable is an odd number, it is player 1's move.

            player = "SPIELER 1"
            symbol = "X"

        else:
        # If the value of the counter variable is an even number, it is player 2's move.

            player = "SPIELER 2"
            symbol = "O"

        # Prompts the user for a number between 1 and 9 (game board) and stores it.
        choice = input(player + ", bitte gib das gewünschte Feld ein: ")

        try:

            # Converts user input to 0-based index for game board position lookup.
            compare = int(choice) - 1

            if field[compare] in ["X", "O"]:
            # Verifies if the adjusted 0-based position corresponds to an occupied position ("X" or "O").

                print("Dieses Feld ist schon belegt. ", end="")

            elif compare in range(len(field)):
            # Execute the player's move if all validation checks pass.

                field[compare] = symbol
                # Updates the game board at the selected position with the player's symbol ("X" or "O").

                game_board()

                counter_odd_even += 1
                # Toggles the player next turn by incrementing the counter (odd: player 1, even: player 2).

            else:

                print("Die eingegebene ganze Zahl muss zwischen 1 und 9 liegen. ", end="")

        except ValueError:

            print("Ihre Angabe ist keine ganze Zahl. ", end="")

move()
