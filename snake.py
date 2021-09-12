import pygame as p
import random as r

class GameObject:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def get_img(self):
        return self.img

    def set_x(self, x:int):
        self.x = x
        
    def set_y(self, y:int):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Apple(GameObject): 

    def __init__(self, x:int, y:int):
        super().__init__(x,y)
        self.img = p.image.load('robo.png')
        self.x = r.randint(1,14)
        self.y = r.randint(1,14)

    def spawn(self):
        pass

    def destroy(self):
        pass

    def __str__(self):
        """TODO: Docstring for __str__.
        returns coordinates for debugging purposes
        """
        return f"Apple at ({self.get_x()},{self.get_y()})"

class Snake:

    BLOCK_WIDTH = 50
    BLOCK_HEIGHT = 50
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 800
    
    def __init__(self):
        p.init()
        p.display.set_caption('VIMSnake!')
        self.display = p.display.set_mode((Snake.SCREEN_WIDTH,Snake.SCREEN_HEIGHT))
        self.clock = p.time.Clock()
        self.init_map()
        
    def init_map(self):
        """Docstring for init_map.
        initializes gamemap.
        """
        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    def print_map_to_console(self):
        """TODO: Docstring for print_map_to_console.
        Prints map to console for debugging purposes.
        """
        for line in self.map:
            for item in line:
                print(item, end= "")
            print()
            
    def draw_map(self):
        """Docstring for draw_map.
        draws gamemap. Each number in self.map array represent a different GameObject.
        """
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 1:
                    p.draw.rect(self.display, (0,0,0),(i*Snake.BLOCK_WIDTH, j*Snake.BLOCK_HEIGHT,Snake.BLOCK_WIDTH, Snake.BLOCK_HEIGHT))
                elif self.map[i][j] == 2:
                    p.draw.rect(self.display, (255,0,0),(i*Snake.BLOCK_WIDTH, j*Snake.BLOCK_HEIGHT,Snake.BLOCK_WIDTH, Snake.BLOCK_HEIGHT))
                else:
                    p.draw.rect(self.display, (0,255,0),(i*Snake.BLOCK_WIDTH, j*Snake.BLOCK_HEIGHT,Snake.BLOCK_WIDTH, Snake.BLOCK_HEIGHT))
        """ TODO NEXT : MAP WITH WALLS, DRAW WALLS AND FLOOR"""

    def mainloop(self):
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    exit()
            apple = Apple(1,1)
            self.map[apple.get_x()][apple.get_y()] = 2
            self.draw_map()
            p.display.flip()
            self.clock.tick(5)

game = Snake()
game.mainloop()
