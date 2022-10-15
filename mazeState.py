from colorama import init, Fore
import random

cell = "c"
wall = "w"
height = 10
width = 10
def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append("u")
        maze.append(line)
    return maze

def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "u":
                print(Fore.WHITE, f"{maze[i][j]}", end="")
            elif maze[i][j] == "c":
                print(Fore.GREEN, f"{maze[i][j]}", end="")
            else:
                print(Fore.RED, f"{maze[i][j]}", end="")
        print('\n')

maze = init_maze(width, height)
print_maze(maze)

starting_height = int(random.random()*height)
starting_width = int(random.random()*width)

if starting_height == 0:
    starting_height += 1
if starting_height == height-1:
    starting_height -= 1
if starting_width == 0:
    starting_width += 1
if starting_width == width - 1:
    starting_width -= 1
    
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height-1, starting_width])
walls.append([starting_height, starting_width-1])
walls.append([starting_height, starting_width+1])
walls.append([starting_height+1, starting_width])

for wall in walls:
    maze[wall[0]][wall[1]] = wall

def surroundingCells(rand_wall):
    s_cells = 0
    if ( maze[rand_wall[0] - 1][rand_wall[1]] == "c"):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1
    return s_cells

def delete_wall(rand_wall):
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)    

def make_walls(width, height):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = 'w'

def create_entrance_exit(width, height):
    for i in range(0, width):
        if(maze[1][i] == "c"):
            maze[0][1] = "c"
            break
    for i in range(width-1, 0, -1):
        if (maze[height-2][i] == "c"):
            maze[height-1][i] == "c"
            break

def create_maze():
    while walls:
        rand_wall = walls[int(random.random()*len(walls))-1]

        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

        if rand_wall[0] != 0:   
            if maze[rand_wall[0]-1][rand_wall[1]] == 'u' and                             maze[rand_wall[0]+1][rand_wall[1]+1] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

        if rand_wall[0] != height-1:
            if maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

        
        if rand_wall[1] != width-1:
            if maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c':
                s_cells = surroundingCells(rand_wall)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'
                    
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                delete_wall(rand_wall)
                continue
            continue

create_maze()
make_walls(width, height)
create_entrance_exit(width, height)
print_maze(maze)
