import copy
import pygame
import time
pygame.init()
import random

WIDTH, HEIGHT = 750, 800
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku Solver")
WHITE = (255, 255, 255)
FPS = 60
game = True
clock = pygame.time.Clock()
NUMBER_FONT = pygame.font.SysFont('chicago', 35)
NUMBER_FONT_BIG = pygame.font.SysFont('chicago', 70)
check = NUMBER_FONT.render('CHECK', True, (0, 0, 200))  # solve
win.blit(check, (450, 760))
check_rect = check.get_rect()

position = [10, 10, 10]

x = None

choice = random.randint(0, 3) #rand number to open random grid file
with open('grid'+str(choice)+'.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f]
grid = l

solved_grid = copy.deepcopy(grid) #copy of grid to get hints


def draw_board(position,x=None): #draw_board
    for i in range(0,9): #draw digits from grid
        for j in range(0,9):
            if grid[i][j] != 0:
                digit = NUMBER_FONT_BIG.render(str(grid[i][j]), True, (0, 0, 0))
                win.blit(digit, (25 + (83 * j),23 + (83 * i)))
            if position[0] == i and position[1] == j and grid[i][j] != 0:
                digit = NUMBER_FONT_BIG.render(str(grid[i][j]), True, (0, 100, 180))
                win.blit(digit, (25 + (83 * j), 23 + (83 * i)))
            if x == 1:
                digit = NUMBER_FONT_BIG.render(str(grid[position[0]][position[1]]), True, (0, 255, 0))
                win.blit(digit, (25 + (83 * position[1]), 23 + (83 * position[0])))
            if x == 0 and position[2] != 0:
                digit = NUMBER_FONT_BIG.render(str(grid[position[0]][position[1]]), True, (255, 0, 0))
                win.blit(digit, (25 + (83 * position[1]), 23 + (83 * position[0])))


    for i in range(0,4): #big_lines
        pygame.draw.line(win, (0, 0, 0), (0, 250 * i), (750, 250 * i), width=4)
        pygame.draw.line(win, (0, 0, 0), (250 * i, 0), (250 * i, 750), width=4)
        pygame.draw.line(win, (102, 102, 150), (250 * i, 750), (250 * i, 800), width=3)

    for i in range(0,9): #small lines
        pygame.draw.line(win, (0, 0, 0), (0, 83*i), (750, 83*i))
        pygame.draw.line(win, (0, 0, 0), (83*i, 0), (83 * i, 750))


    hint = NUMBER_FONT.render('HINT',True,(0,0,200)) #hint text
    win.blit(hint,(90,760))
    hint_rect = hint.get_rect()

    solve = NUMBER_FONT.render('SOLVE',True,(0,0,200)) #solve text
    win.blit(solve,(335,760))
    solve_rect = solve.get_rect()

    check = NUMBER_FONT.render('CHECK', True, (0, 0, 200))  # check text
    win.blit(check, (580, 760))
    check_rect = check.get_rect()


def print_digit_up(): #sprawdzic linie
    for i in range(0,9):
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 0 and mouse_y < 83:
            grid[0][i] = (grid[0][i] + 1) % 10
            clicked = [0,i, grid[0][i]]
            return clicked #return position and digit
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 83 and mouse_y < 166:
            grid[1][i] = (grid[1][i] + 1) % 10
            clicked = [1, i, grid[1][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 166 and mouse_y < 249:
            grid[2][i] = (grid[2][i] + 1) % 10
            clicked = [2, i, grid[2][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 249 and mouse_y < 332:
            grid[3][i] = (grid[3][i] + 1) % 10
            clicked = [3,i, grid[3][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 332 and mouse_y < 415:
            grid[4][i] = (grid[4][i] + 1) % 10
            clicked = [4, i, grid[4][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 415 and mouse_y < 498:
            grid[5][i] = (grid[5][i] + 1) % 10
            clicked = [5, i, grid[5][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83 * (i + 1) and mouse_y > 498 and mouse_y < 581:
            grid[6][i] = (grid[6][i] + 1) % 10
            clicked = [6, i, grid[6][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83 * (i + 1) and mouse_y > 581 and mouse_y < 664:
            grid[7][i] = (grid[7][i] + 1) % 10
            clicked = [7, i, grid[7][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83 * (i + 1) and mouse_y > 664 and mouse_y < 750:
            grid[8][i] = (grid[8][i] + 1) % 10
            clicked = [8, i, grid[8][i]]
            return clicked

def print_digit_down():
    for i in range(0,9):
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 0 and mouse_y < 83:
            grid[0][i] = (grid[0][i] - 1) % 10
            clicked = [0, i, grid[0][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 83 and mouse_y < 166:
            grid[1][i] = (grid[1][i] - 1) % 10
            clicked = [1, i, grid[1][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 166 and mouse_y < 249:
            grid[2][i] = (grid[2][i] - 1) % 10
            clicked = [2, i, grid[2][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 249 and mouse_y < 332:
            grid[3][i] = (grid[3][i] - 1) % 10
            clicked = [3, i, grid[3][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 332 and mouse_y < 415:
            grid[4][i] = (grid[4][i] - 1) % 10
            clicked = [4, i, grid[4][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83*(i+1) and mouse_y > 415 and mouse_y < 498:
            grid[5][i] = (grid[5][i] - 1) % 10
            clicked = [5, i, grid[5][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83 * (i + 1) and mouse_y > 498 and mouse_y < 581:
            grid[6][i] = (grid[6][i] - 1) % 10
            clicked = [6, i, grid[6][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83 * (i + 1) and mouse_y > 581 and mouse_y < 664:
            grid[7][i] = (grid[7][i] - 1) % 10
            clicked = [7, i, grid[7][i]]
            return clicked
        if mouse_x > 83 * i and mouse_x < 83 * (i + 1) and mouse_y > 664 and mouse_y < 750:
            grid[8][i] = (grid[8][i] - 1) % 10
            clicked = [8, i,grid[8][i]]
            return clicked

def possible(position,gridd):
    if position == [10,10,10]:
        return None
    for i in range(0,9): #row
        if gridd[position[0]][i] == position[2] and i != position[1]:
            return False
    for i in range(0,9): #column
        if gridd[i][position[1]] == position[2] and i != position[0]:
            return False
    square_x = position[1] // 3
    square_y = position[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3): # square 3x3
        for j in range(square_x * 3, square_x * 3 + 3):
            if gridd[i][j] == position[2] and (i != position[0] and j != position[1]):
                return False
    return True

def empty(gridd): #find empty square
    for i in range(0,9):
        for j in range(0,9):
            if gridd[i][j] == 0:
                return (i,j)
    return None

def solve(gridd): # sudoku solver
    find = empty(gridd)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        position = [row,col,i]
        if possible(position,gridd):
            gridd[row][col] = i
            if solve(gridd):
                return True
            gridd[row][col] = 0
    return False

solve(solved_grid)

while game:
    clock.tick(FPS)
    mouse_x, mouse_y =pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONUP and (event.button == 3 or event.button ==1) and mouse_x > 500 and mouse_y > 750:
            if position == [10,10,10]:
                pass
            if possible(position,grid) == True:
                x = 1
            if possible(position,grid) == False:
                x = 0
        if event.type == pygame.MOUSEBUTTONUP and (event.button == 3 or event.button ==1) and mouse_x < 250 and mouse_y > 750: ##check hint
            if position == [10,10,10]:
                pass
            else:
                grid[position[0]][position[1]] = solved_grid[position[0]][position[1]]
                x = None
        if event.type == pygame.MOUSEBUTTONUP and (event.button == 3 or event.button ==1) and mouse_x > 250 and mouse_x < 500 and mouse_y > 750:
            solve(grid)
            position = [10,10,10]
            x = None
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and mouse_y < 750:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            position = print_digit_down()
            x = None
            print(position)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and mouse_y < 750:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            position = print_digit_up()
            x = None
            print(position)
    win.fill(WHITE)
    draw_board(position,x)
    pygame.display.update()
