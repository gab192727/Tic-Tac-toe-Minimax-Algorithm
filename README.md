# Google Tic-Tac-toe-Minimax-Algorithm

## Overview

This project is a classic implementation of the Tic Tac Toe game using Python and the Pygame library. The game features an interactive graphical interface where a human player can play against an AI opponent. The AI uses the minimax algorithm with alpha-beta pruning to determine the optimal move. This README provides an overview of the project structure, the key components of the implementation, and instructions on how to run and play the game.

## Project Structure

The project consists of a single Python class, `Tictactoe`, which encapsulates all the functionalities required for the game. The main components of the class are:

1. **Initialization (`__init__` method)**: This sets up the game board, dimensions, colors, and other necessary parameters. It also initializes the Pygame library and creates the game window.

2. **Game Mechanics**:
   - **Board Representation**: The game board is represented as a 3x3 grid using a nested list.
   - **Winning Combinations**: All possible winning combinations are generated and stored.
   - **Player Turns**: The game alternates between the human player (Player 1) and the AI (Player 2).

3. **Drawing Functions**:
   - **`draw_lines`**: Draws the grid lines on the game board.
   - **`draw_winning_line`**: Animates the winning line when a player wins.
   - **`draw_tie_message`**: Displays a message when the game is a draw.
   - **`update_screen`**: Updates the game screen with the current state of the board.

4. **AI Implementation (`ai_algo` method)**: The AI uses the minimax algorithm with alpha-beta pruning to determine the best move. The minimax function recursively evaluates all possible moves and selects the optimal one.

5. **Game Logic**:
   - **`check_winner`**: Checks if there is a winner after each move.
   - **`check_tie`**: Checks if the game is a draw.
   - **`check_valid_squares`**: Ensures moves are made on valid squares.
   - **`mark_square`**: Marks the board with the player's move.

6. **User Interaction**:
   - **`get_row_col`**: Converts mouse click positions to grid coordinates.
   - **`main loop**: The main game loop that handles user input and updates the game state.

## Instructions to Run the Game

### Prerequisites

- Pygame library. You can install it using pip:
  ```bash
  pip install pygame
