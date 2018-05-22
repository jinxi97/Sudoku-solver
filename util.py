# Utility file that provide useful data structures
# util.py
# -------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import heapq
import copy

class GameState:
    def __init__(self, Matrix, domain):
        self.matrix = Matrix
        self.domain = domain

    def successor(self):
        """Return a list of GameState after assign Minimum Remaining Value(MRV)"""
        min_d = 10
        min_i = 10
        min_j = 10
        for i in range(9):
            for j in range(9):
                if len(self.domain[i][j]) != 0 and len(self.domain[i][j]) < min_d:
                    min_d = len(self.domain[i][j])
                    min_i = i
                    min_j = j
        # min_d is also the number of the successor state,
        # because each member in domain will be a new assignment
        next_states = list()
        for k in range(min_d):
            new_matrix = copy.deepcopy(self.matrix)
            new_domain = copy.deepcopy(self.domain)
            value = self.domain[min_i][min_j][k]
            new_matrix[min_i][min_j] = value
            new_domain[min_i][min_j] = list()
            for m, n in constraints(min_i, min_j):
                if self.matrix[m][n] == 0 and value in self.domain[m][n]:
                    new_domain[m][n].remove(value)
                    if len(new_domain[m][n]) == 0:
                        return list()
            next_state = GameState(new_matrix, new_domain)
            next_states.append(next_state)
        return next_states


def is_goal_state(GameState):
    # check if the assignment is qualified
    flag = True
    for i in range(9):
        for j in range(9):
            if GameState.matrix[i][j] == 0:
                flag = False
    return flag


def back_tracking_search(start_state):
    if is_goal_state(start_state):
        return start_state.matrix

    fringe = Stack()
    fringe.push(start_state)
    visited = set()
    expanded = set()
    while not fringe.isEmpty():
        current = fringe.pop()
        visited.add(current)
        if is_goal_state(current):
            return current.matrix
        if current not in expanded:
            for successor in current.successor():
                if successor not in visited:
                    fringe.push(successor)
    return 0


def print_matrix(Matrix):
    for i in range(len(Matrix)):
        print(Matrix[i], "\n")


def constraints(i, j):
    list_of_constraints = list()
    for m in range(9):
        if m != i:
            list_of_constraints.append((m, j))
        if m != j:
            list_of_constraints.append((i, m))

    # (x, y) is the coordinate of the point(i, j) in a 3X3 square
    x = i % 3
    y = j % 3
    iList = list()
    jList = list()
    if x == 0:
        iList = [i+1, i+2]
    if x == 1:
        iList = [i-1, i+1]
    if x == 2:
        iList = [i-2, i-1]
    if y == 0:
        jList = [j+1, j+2]
    if y == 1:
        jList = [j-1, j+1]
    if y == 2:
        jList = [j-2, j-1]

    for ii in iList:
        for jj in jList:
            list_of_constraints.append((ii, jj))

    """
    if i % 3 == 0 and j % 3 == 0:
        '''this point is the [0,0] of the 3X3 square'''
        list_of_constraints.extend(((i+1, j+1), (i+1, j+2), (i+2, j+1), (i+2, j+2)))
    if i % 3 == 0 and j % 3 == 1:
        '''this point is the [0, 1] of the 3X3 square'''
        list_of_constraints.extend(((i+1, j-1), (i+1, j+1), (i+2, j-1), (i+2, j+1)))
    if i % 3 == 0 and j % 3 == 2:
        '''this point is the [0, 2] of the 3X3 square'''
        list_of_constraints.extend(((i+1, j-2), (i+1, j-1), (i+2, j-2), (i+2, j-1)))
    if i % 3 == 1 and j % 3 == 0:
        '''this point is the [1, 0] of the 3X3 square'''
        list_of_constraints.extend(((i-1, j+1), (i-1, j+2), (i+1, j+1), (i+1, j+2)))
    if i % 3 == 1 and j % 3 == 1:
        '''this point is the [1, 1] of the 3X3 square'''
        list_of_constraints.extend(((i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)))
    if i % 3 == 1 and j % 3 == 2:
    """
    return list_of_constraints

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)