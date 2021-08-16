import time
import os
import random
import keyboard



class Matrix():
    matrix = []
    x,y = 0,0
    cnt_snake = 0

    def create_Matrix(self, x, y):

        self.x = x
        self.y = y
        self.matrix = [[0 for i in range(y)] for i in range(x)]

    def create_food(self):

        food = random.randint(1, self.x*self.y - self.cnt_snake)
        for i in range(self.x):
            for j in range(self.y):
                if self.matrix[i][j] == 0:
                    food -= 1
                if food == 0:
                    self.matrix[i][j] = 2
                    break


class Board(Matrix):

    def board_print(self):
        for i in self.matrix:
            for j in i:
                if j == 1:
                    print("□", end='')
                elif j ==2:
                    print('0', end="")
                else:
                    print('▉', end='')
            print()

    def clear(self):
        os.system(['cls'][os.name == os.sys.platform])

class Snake(Matrix):
    s_x = 0
    s_y = 0
    key = 'd'
    d_move = {'w': lambda x: (x[0]+1, x[1]),
              'a': lambda y: (y[0], y[1]-1),
              's': lambda x: (x[0]-1, x[1]),
              'd': lambda y: (y[0], y[1]+1)}
    snake = []
    def create_Snake(self):
        self.s_x,self.s_y = self.x//2, self.y//2
        self.matrix[self.s_x][self.s_y] = 1
        self.snake.append((self.s_x,self.s_y))


    def move(self):
        new = self.d_move[self.key]((self.s_x,self.s_y))
        old = self.snake.pop(0)
        self.matrix[old[0]][old[1]] = 0
        self.proverka(new,old)
        self.s_x,self.s_y = new[0],new[1]
        self.snake.append(new)
        self.matrix[new[0]][new[1]] = 1


    def proverka(self,new,old):
        if new[0]>=self.x\
            or new[0]<0\
            or new[1]>=self.y\
            or new[1]<0\
            or self.matrix[new[0]][new[1]]==1:
            exit(print('GAME OVER'))

        if self.matrix[new[0]][new[1]]==2:
            self.matrix[new[0]][new[1]] = 1
            self.cnt_snake+=1
            self.snake.insert(0,old)
            self.create_food()

class Game(Board, Snake):
    def __init__(self,x,y):
        self.create_Matrix(x,y)
        self.create_Snake()
        self.create_food()
        self.board_print()
        time.sleep(0.5)

    def step(self):

        self.board_print()
        time.sleep(0.5)
        self.move()
        self.clear()


def play(game):
    game.step()

New_game = Game(20,20)

while True:
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):  # if key 'q' is pressed
            New_game.key = 'w'
        elif keyboard.is_pressed('a'):
            New_game.key = 'a'
        elif keyboard.is_pressed('s'):
            New_game.key = 's'
        elif keyboard.is_pressed('d'):
            New_game.key = 'd'
    except:
        pass  # if user pressed a key other than the given key the loop will break
    play(New_game)