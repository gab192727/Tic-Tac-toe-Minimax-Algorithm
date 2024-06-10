import pygame as py
import math

class Tictactoe:
    def __init__(self):

        self.DIMENSION = 625
        # You can change the row and col to 4 to have a 4x4 board hehe
        self.ROW_COL = 3


        self.OFFSET = self.DIMENSION // 75
        self.x_os = self.DIMENSION // 15
        self.SQ_SIZE = self.DIMENSION // self.ROW_COL
        self.OBJECT_SIZE = self.DIMENSION // 50
        self.O_SIZE = self.SQ_SIZE // 3.2
        self.X_SIZE = self.SQ_SIZE // 8
        self.board = [[0 for _ in range(self.ROW_COL)] for _ in range(self.ROW_COL)]
        self.winning_combinations = self.generate_winning_combinations()
        self.screen_color = '#00B4A5'
        self.line_color = '#179187'
        self.o_color = '#efe7c8'
        self.x_color = '#5c5c5c'
        self.tie_color = '#454444'
        self.font_size = self.SQ_SIZE // 2
        self.player = 1
        self.game_over = False

        py.init()
        self.clock = py.time.Clock()
        py.display.set_caption("Tic-Tac-Toe")

        self.screen = py.display.set_mode((self.DIMENSION, self.DIMENSION))
        self.screen.fill(self.screen_color)
        self.draw_lines()

    def generate_winning_combinations(self):
        size = self.ROW_COL
        rows = [[(i, j) for j in range(size)] for i in range(size)]
        cols = [[(j, i) for j in range(size)] for i in range(size)]
        diag1 = [(i, i) for i in range(size)]
        diag2 = [(i, size - i - 1) for i in range(size)]
        return rows + cols + [diag1, diag2]

    def draw_lines(self):
        lines = []
        for i in range(1, self.ROW_COL):
            lines.append(self.SQ_SIZE * i)

        for loc in lines:
            py.draw.line(self.screen, self.line_color, (self.OFFSET, loc), (self.DIMENSION - self.OFFSET, loc), self.OBJECT_SIZE)
            py.draw.line(self.screen, self.line_color, (loc, self.OFFSET), (loc, self.DIMENSION - self.OFFSET), self.OBJECT_SIZE)

    def draw_winning_line(self, start_pos, end_pos, width):
        color = self.o_color if self.player == 2 else self.x_color
        frames = 15
        dest_x = (end_pos[0] - start_pos[0]) / frames
        dest_y = (end_pos[1] - start_pos[1]) / frames
        for frame in range(frames + 1):
            x = start_pos[0] + dest_x * frame
            y = start_pos[1] + dest_y * frame
            self.screen.fill(self.screen_color)
            self.draw_lines()
            self.update_screen()
            py.draw.line(self.screen, color, start_pos, (x, y), width + 5)
            py.display.update()
            self.clock.tick(60)

    def draw_tie_message(self):
        font = py.font.Font(None, self.font_size)
        message = "DRAW!"
        text = font.render(message, True, self.tie_color)
        text_rect = text.get_rect(center=(self.DIMENSION // 2, self.DIMENSION // 2))
        self.screen.blit(text, text_rect)

    def check_winner(self):
        for combo in self.winning_combinations:
            if self.check_pos(combo):
                start_pos = (combo[0][1] * self.SQ_SIZE + self.SQ_SIZE // 2, combo[0][0] * self.SQ_SIZE + self.SQ_SIZE / 2)
                end_pos = (combo[-1][1] * self.SQ_SIZE + self.SQ_SIZE // 2, combo[-1][0] * self.SQ_SIZE + self.SQ_SIZE / 2)
                self.draw_winning_line(start_pos, end_pos, int(self.OBJECT_SIZE * 1.5))
                return True

        if self.check_tie():
            self.draw_tie_message()
            return True
        return False

    def ai_algo(self):

        def minimax(board, depth, alpha, beta, maximizing_player):

            if check_winner_minimax(board, 2):
                return 1
            elif check_winner_minimax(board, 1):
                return -1
            elif check_tie_minimax(board):
                return 0

            if maximizing_player:
                max_eval = -math.inf
                for r in range(self.ROW_COL):
                    for c in range(self.ROW_COL):
                        if board[r][c] == 0:
                            board[r][c] = 2
                            evaluate = minimax(board, depth + 1, alpha, beta, False)
                            board[r][c] = 0
                            max_eval = max(max_eval, evaluate)
                            alpha = max(alpha, evaluate)
                            if beta <= alpha:
                                break
                return max_eval
            else:
                min_eval = math.inf
                for r in range(self.ROW_COL):
                    for c in range(self.ROW_COL):
                        if board[r][c] == 0:
                            board[r][c] = 1
                            evaluate = minimax(board, depth + 1, alpha, beta, True)
                            board[r][c] = 0
                            min_eval = min(min_eval, evaluate)
                            beta = min(beta, evaluate)
                            if beta <= alpha:
                                break
                return min_eval

        def check_winner_minimax(board, player):
            for combo in self.winning_combinations:
                if all(board[r][c] == player for r, c in combo):
                    return True
            return False

        def check_tie_minimax(board):
            return all(cell != 0 for r in board for cell in r)

        best_score = -math.inf
        move = None
        for row in range(self.ROW_COL):
            for col in range(self.ROW_COL):
                if self.board[row][col] == 0:
                    self.board[row][col] = 2
                    score = minimax(self.board, 0, -math.inf, math.inf, False)
                    self.board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move

    def check_pos(self, combo):
        return all(self.board[row][col] == self.player for row, col in combo)

    def check_tie(self):
        return all(cell != 0 for row in self.board for cell in row)

    def check_valid_squares(self, row, col):
        return self.board[row][col] == 0

    def get_row_col(self, loc):
        return loc[1] // self.SQ_SIZE, loc[0] // self.SQ_SIZE

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def update_screen(self):
        for row in range(self.ROW_COL):
            for col in range(self.ROW_COL):
                if self.board[row][col] == 2:
                    center = (col * self.SQ_SIZE + self.SQ_SIZE / 2, row * self.SQ_SIZE + self.SQ_SIZE / 2)
                    py.draw.circle(self.screen, self.o_color, center, self.O_SIZE, self.OBJECT_SIZE)
                elif self.board[row][col] == 1:
                    s_r_1, e_c_1 = row * self.SQ_SIZE + self.SQ_SIZE - self.x_os, col * self.SQ_SIZE + self.SQ_SIZE - self.x_os
                    s_r_2, e_c_2 = col * self.SQ_SIZE + self.x_os, row * self.SQ_SIZE + self.x_os
                    py.draw.line(self.screen, self.x_color, (s_r_2, s_r_1), (e_c_1, e_c_2), self.X_SIZE)
                    py.draw.line(self.screen, self.x_color, (s_r_2, e_c_2), (e_c_1, s_r_1), self.X_SIZE)

    @staticmethod
    def play_again():
        tic = Tictactoe()
        tic.mainloop()

    def mainloop(self):
        while True:
            for e in py.event.get():
                if e.type == py.MOUSEBUTTONDOWN and not self.game_over:
                    row, col = self.get_row_col(e.pos)
                    if self.check_valid_squares(row, col) and self.player == 1:
                        self.mark_square(row, col, self.player)
                        self.update_screen()
                        self.game_over = self.check_winner()
                        py.display.update()
                        self.player = 2

                if self.player == 2 and not self.game_over:
                    row1, col1 = self.ai_algo()
                    self.mark_square(row1, col1, self.player)
                    self.update_screen()
                    self.game_over = self.check_winner()
                    py.display.update()
                    self.player = 1

                elif e.type == py.QUIT:
                    py.quit()

                if e.type == py.KEYDOWN:
                    if e.key == py.K_z:
                        self.play_again()

            py.display.update()


if __name__ == '__main__':
    t = Tictactoe()
    t.mainloop()
