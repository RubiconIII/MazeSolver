from collections import deque

class MazeCell(object): #defines characteristics an individual cell of the maze
    north = False
    south = False
    east = False
    west = False
    isStart = False
    isFinish = False
    visited = 0
    
    def __init__ (self, north, south, east, west, isStart, isFinish): #constructor
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.isStart = isStart
        self.isFinish = isFinish
        self.visited = 0 #cannot be visited on creation (0 is unvisited, 1 is "visit-in-progress," 2 is visited)

def make_cell(north, south, east, west, isStart, isFinish): #call this to easily make a new maze cell
    cell = MazeCell(north, south, east, west, isStart, isFinish)
    return cell

def dfs_solve(maze, x, y, num_visited, print_header): #solve with depth-first search
    if print_header == True: #if the caller wants to print the header
            print("Solving your maze with Depth-First Search\n")
            print("Here are the steps: \n")
            
    current_cell = maze[x][y] #set current cell to passed-in start
    current_coord = [x, y] #set current coord to passed-in start
    
    if (current_cell.isFinish == True): #if the current cell is the finish
            print("***********************************")
            print("*** Found the finish at: {},{}! *****".format(current_coord[0], current_coord[1]))
            print("*** I visited {} cells. **********".format(num_visited))
            print("***********************************")
    else:
        maze[x][y].visited = 1 #set current cell to "visit in progress"
        print("Visit in progress at: {},{}".format(x, y))
        num_visited+=1 #increment the visted counter
        
        next_coords = [] #to load with the next coords to visit
        
        if(current_cell.east == False): #if east movmement is allowed, load the coordinates for eastern cell into next_coords
            next_coords.append((current_coord[0] + 1, current_coord[1])) 
            
        if(current_cell.west == False): #if west movmement is allowed, load the coordinates for west cell into next_coords
            next_coords.append((current_coord[0] - 1, current_coord[1]))  
        
        if(current_cell.north == False): #if north movmement is allowed, load the coordinates for northern cell into next_coords
            next_coords.append((current_coord[0], current_coord[1] - 1))
        
        if(current_cell.south == False): #if south movmement is allowed, load the coordinates for southern cell into next_coords
            next_coords.append((current_coord[0], current_coord[1] + 1))
            
        for (x0, y0) in next_coords: #for all of the next cells
            isCoordsValid = test_coords_validity(x0, y0) #make sure the cell isn't outside the graph
            if (isCoordsValid == True and maze[x0][y0].visited == 0): #make sure the coords are valid and not already visited
                dfs_solve(maze, x0, y0, num_visited, False) #recursively call the dfs
        maze[x][y].visited = 2 #set the current coord to visited
        print("Visit complete at: {},{}".format(x, y))
        

def bfs_solve(maze, x, y): #solve with breadth-first search
    print("Solving your maze with Breadth-First Search\n")
    print("Here are the steps: \n")
    
    maze_q = deque() #to keep track of maze cells
    maze_q.append(maze[x][y]) #append the start cell to the maze deque
    
    coords_q = deque() #to keep track of maze coords
    coords_q.append([x, y]) #append the start coords to the coords deque
    
    maze[x][y].visited = 2 #set inital coord to visited
    step_counter = 1 #visited first cell
    
    while (len(maze_q) > 0):
        current_cell = maze_q.pop() #get the next cell from the deque
        current_coord = coords_q.pop() #get the next coords from the deque
        step_counter+=1 #visited another cell
        print("I'm currently at: {}".format(current_coord))
        
        next_coords = [] #to load with the next coords to visit
        
        if(current_cell.east == False): #if east movmement is allowed, load the coordinates for eastern cell into next_coords
            next_coords.append((current_coord[0] + 1, current_coord[1])) 
            
        if(current_cell.west == False): #if west movmement is allowed, load the coordinates for west cell into next_coords
            next_coords.append((current_coord[0] - 1, current_coord[1]))  
        
        if(current_cell.north == False): #if north movmement is allowed, load the coordinates for northern cell into next_coords
            next_coords.append((current_coord[0], current_coord[1] - 1))
        
        if(current_cell.south == False): #if south movmement is allowed, load the coordinates for southern cell into next_coords
            next_coords.append((current_coord[0], current_coord[1] + 1))
            
        print("I'm looking at these next: {}".format(next_coords))
        
        if (current_cell.isFinish == True): #if the current cell is the finish
            print("***********************************")
            print("*** Found the finish at: {},{}! *****".format(current_coord[0], current_coord[1]))
            print("*** I visited {} cells. **********".format(step_counter))
            print("***********************************\n")
            maze_q.clear() #found the shortest route, clear the cells
            coords_q.clear() #found the shortest route, clear the next coords
        else:
            for (x0, y0) in next_coords: #for all of the next cells
                isCoordsValid = test_coords_validity(x0, y0) #make sure the cell isn't outside the graph
                if (isCoordsValid == True and maze[x0][y0].visited == 0): #make sure the coords are valid and not already visited
                    maze_q.append(maze[x0][y0]) #append newly found cells
                    coords_q.append([x0, y0]) #append newly found coords
                    print("Examined maze at: {},{}".format(x0, y0))
                maze[x0][y0].visited = 2 #set the current coord to visited

def test_coords_validity(x, y): #make sure the given coords aren't outside of the graph
    if (x >= 0 and x <= 9 and y >= 0 and y <= 9):
        return True
    else:
        return False
            
def print_maze(maze, w, h): #print out the given maze
    maze_to_print = [["" for x in range(w)] for y in range(h + 1)]
    for y in range(h):
        for x in range(w):
            if (maze[x][y].south == True and maze[x][y].west == True):
                maze_to_print[x][y] = "|_"
            elif (maze[x][y].south == True and maze[x][y].west == True and maze[x][y].isStart == True):
                maze_to_print[x][y] = "|s_"
            elif (maze[x][y].west == True and maze[x][y].isStart == True):
                maze_to_print[x][y] = "|s"
            elif (maze[x][y].south == True and maze[x][y].isStart == True):
                maze_to_print[x][y] = "s__"
            elif (maze[x][y].isStart == True):
                maze_to_print[x][y] = "s "
            elif (maze[x][y].south == True and maze[x][y].west == True and maze[x][y].isFinish == True):
                maze_to_print[x][y] = "|f_"
            elif (maze[x][y].west == True and maze[x][y].isFinish == True):
                maze_to_print[x][y] = "|f"
            elif (maze[x][y].south == True and maze[x][y].isFinish == True):
                maze_to_print[x][y] = "f__"
            elif (maze[x][y].isFinish == True):
                maze_to_print[x][y] = "f "
            elif (maze[x][y].south == True):
                maze_to_print[x][y] = "__"
            elif (maze[x][y].west == True):
                maze_to_print[x][y] = "| "
            else: maze_to_print[x][y] = "  "   
                
    for y1 in range(h): #add the walls on the right side of the maze
            maze_to_print[w][y1] = "|"
    
    print("__" * w) #print out the ceiling
    
    for row in zip(*maze_to_print): #print out the rest of the maze
        print("".join(row))
        
    print("\n")
    
def make_curtis_maze(w, h): #define curtis's maze by cell - exact maze from last homework
    Matrix = [[MazeCell(False, False, False, False, False, False) for x in range(w)] for y in range(h)]
    
    #1st row
    Matrix[0][0] = make_cell(True, False, False, True, True, False)
    Matrix[1][0] = make_cell(True, True, False, False, False, False)
    Matrix[2][0] = make_cell(True, True, False, False, False, False)
    Matrix[3][0] = make_cell(True, False, False, False, False, False)
    Matrix[4][0] = make_cell(True, False, False, False, False, False)
    Matrix[5][0] = make_cell(True, True, False, False, False, False)
    Matrix[6][0] = make_cell(True, True, False, False, False, False)
    Matrix[7][0] = make_cell(True, True, False, False, False, False)
    Matrix[8][0] = make_cell(True, True, False, False, False, False)
    Matrix[9][0] = make_cell(True, False, True, False, False, False)
    
    #2nd row
    Matrix[0][1] = make_cell(False, False, False, True, False, False)
    Matrix[1][1] = make_cell(True, True, False, False, False, False)
    Matrix[2][1] = make_cell(True, True, True, False, False, False)
    Matrix[3][1] = make_cell(False, False, True, True, False, False)
    Matrix[4][1] = make_cell(False, True, True, True, False, False)
    Matrix[5][1] = make_cell(True, False, False, True, False, False)
    Matrix[6][1] = make_cell(True, True, False, False, False, False)
    Matrix[7][1] = make_cell(True, False, True, False, False, False)
    Matrix[8][1] = make_cell(True, True, False, True, False, False)
    Matrix[9][1] = make_cell(False, True, True, False, False, False)
    
    #3nd row
    Matrix[0][2] = make_cell(False, False, True, True, False, False)
    Matrix[1][2] = make_cell(True, False, True, True, False, False)
    Matrix[2][2] = make_cell(True, False, False, True, False, False)
    Matrix[3][2] = make_cell(False, True, True, False, False, False)
    Matrix[4][2] = make_cell(True, False, False, True, False, False)
    Matrix[5][2] = make_cell(False, True, True, False, False, False)
    Matrix[6][2] = make_cell(True, False, False, True, False, False)
    Matrix[7][2] = make_cell(False, True, True, False, False, False)
    Matrix[8][2] = make_cell(True, False, False, True, False, False)
    Matrix[9][2] = make_cell(True, False, True, False, False, False)
    
    #4th row
    Matrix[0][3] = make_cell(True, False, False, True, False, False)
    Matrix[1][3] = make_cell(False, True, True, False, False, False)
    Matrix[2][3] = make_cell(False, False, False, True, False, False)
    Matrix[3][3] = make_cell(True, False, True, False, False, False)
    Matrix[4][3] = make_cell(False, False, True, True, False, False)
    Matrix[5][3] = make_cell(True, False, False, True, False, False)
    Matrix[6][3] = make_cell(False, True, True, False, False, False)
    Matrix[7][3] = make_cell(True, False, False, True, False, False)
    Matrix[8][3] = make_cell(False, True, True, False, False, False)
    Matrix[9][3] = make_cell(False, False, True, True, False, False)
    
    #5th row
    Matrix[0][4] = make_cell(False, False, True, True, False, False)
    Matrix[1][4] = make_cell(True, False, False, True, False, False)
    Matrix[2][4] = make_cell(False, True, True, False, False, False)
    Matrix[3][4] = make_cell(False, False, True, True, False, False)
    Matrix[4][4] = make_cell(False, False, True, True, False, False)
    Matrix[5][4] = make_cell(False, True, False, True, False, False)
    Matrix[6][4] = make_cell(True, True, False, False, False, False)
    Matrix[7][4] = make_cell(False, True, True, False, False, False)
    Matrix[8][4] = make_cell(True, False, True, True, False, False)
    Matrix[9][4] = make_cell(False, False, True, True, False, False)
    
    #6th row
    Matrix[0][5] = make_cell(False, False, True, True, False, False)
    Matrix[1][5] = make_cell(False, True, False, True, False, False)
    Matrix[2][5] = make_cell(True, True, True, False, False, False)
    Matrix[3][5] = make_cell(False, False, True, True, False, False)
    Matrix[4][5] = make_cell(False, True, False, True, False, False)
    Matrix[5][5] = make_cell(True, False, True, False, False, False)
    Matrix[6][5] = make_cell(True, True, False, True, False, False)
    Matrix[7][5] = make_cell(True, True, False, False, False, False)
    Matrix[8][5] = make_cell(False, False, True, False, False, False)
    Matrix[9][5] = make_cell(False, False, True, True, False, False)
    
    #7th row
    Matrix[0][6] = make_cell(False, True, False, True, False, False)
    Matrix[1][6] = make_cell(True, True, False, False, False, False)
    Matrix[2][6] = make_cell(True, False, True, False, False, False)
    Matrix[3][6] = make_cell(False, False, False, True, False, False)
    Matrix[4][6] = make_cell(True, True, False, False, False, False)
    Matrix[5][6] = make_cell(False, True, False, False, False, False)
    Matrix[6][6] = make_cell(True, True, False, False, False, False)
    Matrix[7][6] = make_cell(True, True, False, False, False, False)
    Matrix[8][6] = make_cell(False, True, True, False, False, False)
    Matrix[9][6] = make_cell(False, False, True, True, False, False)
    
    #8th row
    Matrix[0][7] = make_cell(True, False, True, True, False, False)
    Matrix[1][7] = make_cell(True, False, False, True, False, False)
    Matrix[2][7] = make_cell(False, True, True, False, False, False)
    Matrix[3][7] = make_cell(False, False, True, True, False, False)
    Matrix[4][7] = make_cell(True, False, False, True, False, False)
    Matrix[5][7] = make_cell(True, True, False, False, False, False)
    Matrix[6][7] = make_cell(True, False, True, False, False, False)
    Matrix[7][7] = make_cell(True, False, False, True, False, False)
    Matrix[8][7] = make_cell(True, False, True, False, False, False)
    Matrix[9][7] = make_cell(False, False, True, True, False, False)
    
    #9th row
    Matrix[0][8] = make_cell(False, False, True, True, False, False)
    Matrix[1][8] = make_cell(False, True, False, True, False, False)
    Matrix[2][8] = make_cell(True, False, True, False, False, False)
    Matrix[3][8] = make_cell(False, True, True, True, False, False)
    Matrix[4][8] = make_cell(False, False, True, True, False, False)
    Matrix[5][8] = make_cell(True, False, True, True, False, False)
    Matrix[6][8] = make_cell(False, True, False, True, False, False)
    Matrix[7][8] = make_cell(False, True, True, False, False, False)
    Matrix[8][8] = make_cell(False, True, False, True, False, False)
    Matrix[9][8] = make_cell(False, False, True, False, False, False)
        
    #10th row
    Matrix[0][9] = make_cell(False, True, False, True, False, False)
    Matrix[1][9] = make_cell(True, True, False, False, False, False)
    Matrix[2][9] = make_cell(False, True, False, False, False, False)
    Matrix[3][9] = make_cell(True, True, False, False, False, False)
    Matrix[4][9] = make_cell(False, True, True, False, False, False)
    Matrix[5][9] = make_cell(False, True, False, True, False, False)
    Matrix[6][9] = make_cell(True, True, False, False, False, False)
    Matrix[7][9] = make_cell(True, True, False, False, False, False)
    Matrix[8][9] = make_cell(True, True, False, False, False, False)
    Matrix[9][9] = make_cell(False, True, True, False, False, True)
    
    return Matrix

def make_koltas_maze(w, h): #define koltas maze by cell - exact maze as in project spec
    Matrix = [[MazeCell(False, False, False, False, False, False) for x in range(w)] for y in range(h)]
    
    #1st row
    Matrix[0][0] = make_cell(True, False, False, True, True, False)
    Matrix[1][0] = make_cell(True, True, False, False, False, False)
    Matrix[2][0] = make_cell(True, True, False, False, False, False)
    Matrix[3][0] = make_cell(True, True, False, False, False, False)
    Matrix[4][0] = make_cell(True, True, False, False, False, False)
    Matrix[5][0] = make_cell(True, True, False, False, False, False)
    Matrix[6][0] = make_cell(True, True, False, False, False, False)
    Matrix[7][0] = make_cell(True, True, False, False, False, False)
    Matrix[8][0] = make_cell(True, True, False, False, False, False)
    Matrix[9][0] = make_cell(True, False, True, False, False, False)
    
    #2nd row
    Matrix[0][1] = make_cell(False, False, True, True, False, False)
    Matrix[1][1] = make_cell(True, False, False, True, False, False)
    Matrix[2][1] = make_cell(True, True, False, False, False, False)
    Matrix[3][1] = make_cell(True, True, False, False, False, False)
    Matrix[4][1] = make_cell(True, True, False, False, False, False)
    Matrix[5][1] = make_cell(True, True, False, False, False, False)
    Matrix[6][1] = make_cell(True, True, False, False, False, False)
    Matrix[7][1] = make_cell(True, True, False, False, False, False)
    Matrix[8][1] = make_cell(True, True, False, False, False, False)
    Matrix[9][1] = make_cell(False, False, True, False, False, False)
    
    #3rd row
    Matrix[0][2] = make_cell(False, False, True, True, False, False)
    Matrix[1][2] = make_cell(False, True, False, True, False, False)
    Matrix[2][2] = make_cell(True, True, False, False, False, False)
    Matrix[3][2] = make_cell(True, True, False, False, False, False)
    Matrix[4][2] = make_cell(True, False, False, False, False, False)
    Matrix[5][2] = make_cell(True, True, True, False, False, False)
    Matrix[6][2] = make_cell(True, True, False, True, False, False)
    Matrix[7][2] = make_cell(True, True, False, False, False, False)
    Matrix[8][2] = make_cell(True, True, False, False, False, False)
    Matrix[9][2] = make_cell(False, True, True, False, False, False)
    
    #4th row
    Matrix[0][3] = make_cell(False, False, True, True, False, False)
    Matrix[1][3] = make_cell(True, False, False, True, False, False)
    Matrix[2][3] = make_cell(True, False, False, False, False, False)
    Matrix[3][3] = make_cell(True, False, False, False, False, False)
    Matrix[4][3] = make_cell(False, False, True, False, False, False)
    Matrix[5][3] = make_cell(True, False, False, True, False, False)
    Matrix[6][3] = make_cell(True, True, False, False, False, False)
    Matrix[7][3] = make_cell(True, True, False, False, False, False)
    Matrix[8][3] = make_cell(True, True, False, False, False, False)
    Matrix[9][3] = make_cell(True, False, True, False, False, False)
    
    #5th row
    Matrix[0][4] = make_cell(False, False, True, True, False, False)
    Matrix[1][4] = make_cell(False, False, False, True, False, False)
    Matrix[2][4] = make_cell(False, False, False, False, False, False)
    Matrix[3][4] = make_cell(False, False, False, False, False, False)
    Matrix[4][4] = make_cell(False, False, True, False, False, False)
    Matrix[5][4] = make_cell(True, True, False, True, False, False)
    Matrix[6][4] = make_cell(True, True, True, False, False, False)
    Matrix[7][4] = make_cell(True, True, False, True, False, False)
    Matrix[8][4] = make_cell(True, True, True, False, False, False)
    Matrix[9][4] = make_cell(False, False, True, True, False, False)
    
    #6th row
    Matrix[0][5] = make_cell(False, False, True, True, False, False)
    Matrix[1][5] = make_cell(False, True, False, True, False, False)
    Matrix[2][5] = make_cell(False, True, False, False, False, False)
    Matrix[3][5] = make_cell(False, True, False, False, False, False)
    Matrix[4][5] = make_cell(False, True, False, False, False, False)
    Matrix[5][5] = make_cell(True, True, False, False, False, False)
    Matrix[6][5] = make_cell(True, True, False, False, False, False)
    Matrix[7][5] = make_cell(True, True, False, False, False, False)
    Matrix[8][5] = make_cell(True, True, False, False, False, False)
    Matrix[9][5] = make_cell(False, False, True, False, False, False)
    
    #7th row
    Matrix[0][6] = make_cell(False, False, True, True, False, False)
    Matrix[1][6] = make_cell(True, False, False, True, False, False)
    Matrix[2][6] = make_cell(True, True, False, False, False, False)
    Matrix[3][6] = make_cell(True, True, False, False, False, False)
    Matrix[4][6] = make_cell(True, True, False, False, False, False)
    Matrix[5][6] = make_cell(True, True, False, False, False, False)
    Matrix[6][6] = make_cell(True, True, False, False, False, False)
    Matrix[7][6] = make_cell(True, True, False, False, False, False)
    Matrix[8][6] = make_cell(True, True, False, False, False, False)
    Matrix[9][6] = make_cell(False, False, True, False, False, False)
    
    #8th row
    Matrix[0][7] = make_cell(False, False, True, True, False, False)
    Matrix[1][7] = make_cell(False, False, True, True, False, False)
    Matrix[2][7] = make_cell(True, False, False, True, False, False)
    Matrix[3][7] = make_cell(True, False, True, False, False, False)
    Matrix[4][7] = make_cell(True, False, False, True, False, False)
    Matrix[5][7] = make_cell(True, False, True, False, False, False)
    Matrix[6][7] = make_cell(True, False, True, True, False, False)
    Matrix[7][7] = make_cell(True, False, True, True, False, False)
    Matrix[8][7] = make_cell(True, False, False, True, False, False)
    Matrix[9][7] = make_cell(False, True, True, False, False, False)
    
    #9th row
    Matrix[0][8] = make_cell(False, False, True, True, False, False)
    Matrix[1][8] = make_cell(False, False, True, True, False, False)
    Matrix[2][8] = make_cell(False, False, True, True, False, False)
    Matrix[3][8] = make_cell(False, False, True, True, False, False)
    Matrix[4][8] = make_cell(False, False, True, True, False, False)
    Matrix[5][8] = make_cell(False, False, True, True, False, False)
    Matrix[6][8] = make_cell(False, True, True, True, False, False)
    Matrix[7][8] = make_cell(False, False, True, False, False, False)
    Matrix[8][8] = make_cell(False, True, False, True, False, False)
    Matrix[9][8] = make_cell(True, False, True, False, False, False)
    
    #10th row
    Matrix[0][9] = make_cell(False, True, True, True, True, False)
    Matrix[1][9] = make_cell(False, True, False, True, True, False)
    Matrix[2][9] = make_cell(False, True, True, False, False, False)
    Matrix[3][9] = make_cell(False, True, False, True, True, False)
    Matrix[4][9] = make_cell(False, True, True, False, False, False)
    Matrix[5][9] = make_cell(False, True, False, True, True, False)
    Matrix[6][9] = make_cell(True, True, False, False, False, False)
    Matrix[7][9] = make_cell(False, True, False, False, False, False)
    Matrix[8][9] = make_cell(True, True, False, False, False, False)
    Matrix[9][9] = make_cell(False, True, True, False, False, True)
    
    return Matrix

if __name__ == '__main__':
    w, h = 10, 10
    koltas_maze = make_koltas_maze(w, h)
    koltas_maze2 = make_koltas_maze(w, h)
    
    curtis_maze = make_curtis_maze(w, h)
    curtis_maze2 = make_curtis_maze(w, h)
    
    print("Kolta's Maze")
    print_maze(koltas_maze, w, h) 
    bfs_solve(koltas_maze, 0, 0)
    dfs_solve(koltas_maze2, 0, 0, 1, True)
    
    print("\nCurtis' Maze")
    print_maze(curtis_maze, w, h)
    bfs_solve(curtis_maze, 0, 0)
    dfs_solve(curtis_maze2, 0, 0, 1, True)