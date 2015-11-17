#!/usr/bin/env python3

import random

class GameBoard(object):
    def __init__(self, N=4):
        self.board = [[0 for _ in range(N)] for _ in range(N)]
        self.N = N
        self.add_chip(self.get_choices())

    def add_chip(self, choices):
        """
        after each move, add one number on the board
        number choices: 2
        """
        x, y = random.choice(choices)
        self.board[x][y] = random.choice([2, 4])

    def get_choices(self):
        choices = []
        for x in range(self.N):
            for y in range(self.N):
                if not self.board[x][y]:
                    choices.append((x, y))
        return choices

    def is_game_over(self):
        # TODO: add this function
        pass

    def is_valid_move(self, direction):
        # TODO: add checker
        pass

    def draw(self):
        line = '{:>4}|' * self.N
        print('-' * (self.N + 1) * self.N)
        for row in self.board:
            print(line.format(*row))
            print('-' * (self.N + 1) * self.N)

    def run(self):
        not_exist = True
        while not_exist:
            self.draw()
            print('left: 0, right: 1, up: 2, down: 3, exit: other')
            direction = int(input('Enter direction: '))
            if direction not in [0, 1, 2, 3]:
                not_exist = False
            else:
                self.move(direction)
                self.add_chip(self.get_choices())

    # Main algorithm
    def move(self, direction):
        """
        Idea:
            similar to read and write 0s in array problem. always keep a write index(k)
        Algorithm:
            keep the first encountered value Index
            if found the second value:
                if second val == first val:
                    update row with 2 * val
                    empty first value
                elif second val != first val:
                    update row with val
                    make second val as the first value
                else: no val: continue
        Directions:
            left, right, up, down = 0, 1, 2, 3
        """
        if direction == 0:
            for i in range(self.N):
                prev = 0
                k = 0
                for j in range(self.N):
                    if not self.board[i][j]:
                        continue
                    if not prev:
                        prev = self.board[i][j]
                        continue
                    if prev == self.board[i][j]:
                        self.board[i][k] = 2 * prev
                        prev = 0
                    else:
                        self.board[i][k] = prev
                        prev = self.board[i][j]
                    k += 1
                if prev:
                    self.board[i][k] = prev
                    k += 1
                while k < self.N:
                    self.board[i][k] = 0
                    k += 1
        elif direction == 1:
            for i in range(self.N):
                prev = 0
                k = self.N - 1
                for j in range(self.N - 1, -1, -1):
                    if not self.board[i][j]:
                        continue
                    if not prev:
                        prev = self.board[i][j]
                        continue
                    if prev == self.board[i][j]:
                        self.board[i][k] = 2 * prev
                        prev = 0
                    else:
                        self.board[i][k] = prev
                        prev = self.board[i][j]
                    k -= 1
                if prev:
                    self.board[i][k] = prev
                    k -= 1
                while k >= 0:
                    self.board[i][k] = 0
                    k -= 1
        elif direction == 2:
            for j in range(self.N):
                prev = 0
                k = 0
                for i in range(self.N):
                    if not self.board[i][j]:
                        continue
                    if not prev:
                        prev = self.board[i][j]
                        continue
                    if prev == self.board[i][j]:
                        self.board[k][j] = 2 * prev
                        prev = 0
                    else:
                        self.board[k][j] = prev
                        prev = self.board[i][j]
                    k += 1
                if prev:
                    self.board[k][j] = prev
                    k += 1
                while k < self.N:
                    self.board[k][j] = 0
                    k += 1
        elif direction == 3:
            for j in range(self.N):
                prev = 0
                k = self.N - 1
                for i in range(self.N - 1, -1, -1):
                    if not self.board[i][j]:
                        continue
                    if not prev:
                        prev = self.board[i][j]
                        continue
                    if prev == self.board[i][j]:
                        self.board[k][j] = 2 * prev
                        prev = 0
                    else:
                        self.board[k][j] = prev
                        prev = self.board[i][j]
                    k -= 1
                if prev:
                    self.board[k][j] = prev
                    k -= 1
                while k >= 0:
                    self.board[k][j] = 0
                    k -= 1



if __name__ == '__main__':
    g = GameBoard()
    g.run()

