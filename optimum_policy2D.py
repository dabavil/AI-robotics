# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

  #initialize value variable which will be used to store the cost of policy to goal from any position in any orientation
  value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
           [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
           [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
           [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]

  #explicitly set this to 0 for grid cell corresponding to goal in any orientation
  for i in range(len(value)):
    value[i][goal[0]][goal[1]] = 0

  closed = [[[0 for row in range(len(grid[0]))] for col in range(len(grid))],
           [[0 for row in range(len(grid[0]))] for col in range(len(grid))],
           [[0 for row in range(len(grid[0]))] for col in range(len(grid))],
           [[0 for row in range(len(grid[0]))] for col in range(len(grid))]]

  for i in range(len(closed)):
    closed[i][goal[0]][goal[1]] = 1 

  best_move = [[[0 for row in range(len(grid[0]))] for col in range(len(grid))],
              [[0 for row in range(len(grid[0]))] for col in range(len(grid))],
              [[0 for row in range(len(grid[0]))] for col in range(len(grid))],
              [[0 for row in range(len(grid[0]))] for col in range(len(grid))]]

         
  #initialize policy

  policy = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]

  x = goal[0]
  y = goal[1]
  orient = init[1]
  total_cost = 0

  open_list = [[total_cost, x, y, 0],[total_cost, x, y, 1],[total_cost, x, y, 2],[total_cost, x, y, 3]]

  resign = False  

  while not resign:
    if len(open_list) == 0:
      resign = True
      break
    else:
      open_list.sort()
      open_list.reverse()
      next_cell = open_list.pop()

      total_cost = next_cell[0]
      x = next_cell[1]
      y = next_cell[2]
      orient = next_cell[3]
        
      for a in range(len(action)):
        x2 = x - forward[orient][0]
        y2 = y - forward[orient][1]
        orient2 = (orient - action[a]) % len(forward)
        total_cost2 = total_cost + cost[a]

        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
          if closed[orient2][x2][y2] == 0 and grid[x2][y2] == 0:
            if total_cost2 < value[orient2][x2][y2]:
              value[orient2][x2][y2] = total_cost2
              best_move[orient2][x2][y2] = a
              open_list.append([total_cost2, x2, y2, orient2])

  x = init[0]
  y = init [1]
  z = init[2]

  for i in range(100):
    if x == goal[0] and y == goal[1]:
      policy[x][y] = '*'
      return policy
    else:
      policy[x][y] = action_name[best_move[z][x][y]]
      
      z = (z + action[best_move[z][x][y]]) % len(forward)
      x += forward[z][0]
      y += forward[z][1]
    

  return policy


def print_array_2D(array):
    for element in array:
        print element
    print "\n"

def print_array_3D(arrays):
    for array in arrays:
      for element in array:
        print element
      print "\n"
    print "\n"

print_array_2D(optimum_policy2D(grid,init,goal,cost))





