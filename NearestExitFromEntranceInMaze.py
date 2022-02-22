# Problem: Nearest Exit from Entrance in Maze
# URL: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
#
# Problem outline:
# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
# You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right.
# You cannot step into a cell with a wall, and you cannot step outside the maze.
# Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze.
# The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        current_maze = maze
        num_rows = len(maze)
        num_cols = len(maze[0])
        max_length = num_rows * num_cols

        current_maze[entrance[0]][entrance[1]] = '+'
        current_pos = [entrance]
        step = 1

        # bfs
        while (step < max_length):
            new_pos = []

            # check all four directions around current position
            for pos in current_pos:
                checkPos = [[pos[0] + 1, pos[1]],
                            [pos[0] - 1, pos[1]],
                            [pos[0], pos[1] + 1],
                            [pos[0], pos[1] - 1]]

                for i in checkPos:
                    # skip if invalid index
                    if i[0] >= num_rows or i[0] < 0 or i[1] >= num_cols or i[1] < 0:
                        continue

                    # skip if wall
                    if (current_maze[i[0]][i[1]] == '+'):
                        continue

                    # if exit, return number of steps taken
                    if ((0 in i) or (i[0] == num_rows - 1) or (i[1] == num_cols - 1)):
                        return step

                    current_maze[i[0]][i[1]] = '+';  # change cell to wall to prevent backtracking
                    new_pos.append(i)  # add current position as new positions to continue search from

            # if no more new positions, stop and return no solution
            if len(new_pos) == 0:
                return -1

            current_pos = new_pos
            step += 1

        return -1
