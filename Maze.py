import pygame
import time
import random
WIDTH = 450
HEIGHT = 450
FPS = 30
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
RED = (255, 0, 0)
YELLOW = (255 ,255 ,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# Maze Variables
x = 0            
y = 0               
w = 20               
grid = []
visited = []
stack = []
solution = {}

class Grid():
    def __init__():
        pass

def build_grid(x, y, w):
    for i in range(1,21):
        x = 20                                                           
        y = y + 20                                                       
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])          
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])         
            grid.append((x,y))                                          
            x = x + 20                                                   


class Directions(Grid):
    def __init__():
        pass

def go_up(x, y):
    pygame.draw.rect(screen, RED, (x + 1, y - w + 1, 19, 39), 0)       
    pygame.display.update()                                           


def go_down(x, y):
    pygame.draw.rect(screen, RED, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()


def go_left(x, y):
    pygame.draw.rect(screen, RED, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()


def go_right(x, y):
    pygame.draw.rect(screen, RED, (x +1, y +1, 39, 19), 0)
    pygame.display.update()


def single_cell( x, y):
    pygame.draw.rect(screen, YELLOW, (x +1, y +1, 18, 18), 0)        
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, RED, (x +1, y +1, 18, 18), 0)      
    pygame.display.update()                                                    

class Maze(Directions):
    def __init__():
        pass

def create_maze(x,y):
    single_cell(x, y)                                            
    stack.append((x,y))                                          
    visited.append((x,y))                                        
    while len(stack) > 0:                                       
        time.sleep(.07)                                          
        cell = []                                                
        if (x + w, y) not in visited and (x + w, y) in grid:     
            cell.append("right")                                  

        if (x - w, y) not in visited and (x - w, y) in grid:     
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:     
            cell.append("up")

        if len(cell) > 0:                                      
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "right":                          
                go_right(x, y)                                   
                solution[(x + w, y)] = x, y                       
                x = x + w                                          
                visited.append((x, y))                              
                stack.append((x, y))                               

            elif cell_chosen == "left":
                go_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                go_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                go_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                   
            single_cell(x, y)                                     
            time.sleep(.05)                                       
            backtracking_cell(x, y)                    


x, y = 20, 20         
build_grid(40, 0, 20) # Size and stuff for the grid       
create_maze(x,y) # Starts the creazting of the maz            


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False