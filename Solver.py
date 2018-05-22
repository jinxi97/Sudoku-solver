import util
import time
# Initialize the sudoku game
w, h = 9, 9
Matrix = [[0 for x in range(w)] for y in range(h)]
domain = [[[i for i in range(1, 10)] for x in range(w)] for y in range(h)]


# load a sudoku puzzle
'''
level: hard

Matrix[0] = [0, 0, 0, 0, 0, 2, 0, 0, 9]
Matrix[1] = [3, 0, 6, 5, 9, 0, 4, 7, 0]
Matrix[2] = [0, 0, 0, 0, 8, 0, 0, 0, 0]
Matrix[3] = [2, 0, 4, 0, 0, 8, 1, 0, 7]
Matrix[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Matrix[5] = [9, 0, 1, 3, 0, 0, 2, 0, 6]
Matrix[6] = [0, 0, 0, 0, 4, 0, 0, 0, 0]
Matrix[7] = [0, 2, 7, 0, 3, 5, 6, 0, 8]
Matrix[8] = [6, 0, 0, 8, 0, 0, 0, 0, 0]
'''
'''
level: easy

Matrix[0] = [6, 0, 8, 3, 9, 0, 0, 1, 0]
Matrix[1] = [0, 4, 0, 0, 0, 0, 0, 8, 5]
Matrix[2] = [1, 0, 0, 0, 0, 2, 0, 4, 0]
Matrix[3] = [4, 0, 0, 2, 0, 0, 0, 7, 0]
Matrix[4] = [5, 0, 1, 6, 0, 9, 4, 0, 8]
Matrix[5] = [0, 2, 0, 0, 0, 7, 0, 0, 9]
Matrix[6] = [0, 9, 0, 1, 0, 0, 0, 0, 4]
Matrix[7] = [2, 8, 0, 0, 0, 0, 0, 9, 0]
Matrix[8] = [0, 1, 0, 0, 6, 8, 7, 0, 2]
'''
'''
level: super hard
'''
Matrix[0] = [0, 0, 0, 0, 5, 0, 7, 0, 8]
Matrix[1] = [0, 0, 0, 7, 0, 0, 0, 0, 0]
Matrix[2] = [0, 6, 1, 4, 0, 8, 0, 0, 0]
Matrix[3] = [5, 0, 0, 3, 0, 0, 0, 7, 0]
Matrix[4] = [0, 0, 4, 0, 0, 0, 9, 0, 0]
Matrix[5] = [0, 8, 0, 0, 0, 6, 0, 0, 1]
Matrix[6] = [0, 0, 0, 1, 0, 5, 6, 4, 0]
Matrix[7] = [0, 0, 0, 0, 0, 7, 0, 0, 0]
Matrix[8] = [2, 0, 3, 0, 8, 0, 0, 0, 0]




start_time = time.time()
# Eliminate impossible values from domain.
for i in range(9):
    for j in range(9):
        # if value is not assigned, reduce its domain. Otherwise, empty the domain.
        if Matrix[i][j] == 0:
            for m, n in util.constraints(i, j):
                if Matrix[m][n] in domain[i][j]:
                    domain[i][j].remove(Matrix[m][n])
        else:
            domain[i][j] = list()

initial_state = util.GameState(Matrix, domain)


if util.back_tracking_search(initial_state) == 0:
    print("This sudoku is not solvable.")
else:
    util.print_matrix(util.back_tracking_search(initial_state))

elapse_time = time.time() - start_time
print("Solved in:", elapse_time, 's')