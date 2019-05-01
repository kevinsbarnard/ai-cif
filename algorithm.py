# algorithm.py
# Search algorithms

import queue
import board
import time


class TreeNode:
    data = None
    cost = 0
    parent = None

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost


def get_neighbors(b: board.Board, cell: board.BoardCell):
    neighbors = [
        b.get_cell(cell.row - 1, cell.col),
        b.get_cell(cell.row + 1, cell.col),
        b.get_cell(cell.row, cell.col - 1),
        b.get_cell(cell.row, cell.col + 1),
    ]
    return list(filter(lambda node: node.color == 'gray' or node.color == 'yellow', neighbors))


def bfs(b: board.Board, delay=0):
    start = None
    for row in b.cells:
        for cell in row:
            if cell.color == 'blue':
                start = cell

    q = queue.Queue()
    q.put(TreeNode(start))
    while not q.empty():
        tree_node = q.get()
        neighbors = get_neighbors(b, tree_node.data)
        for neighbor in neighbors:
            child_node = TreeNode(neighbor, parent=tree_node)
            if child_node.data.color == 'yellow':
                return child_node
            else:
                neighbor.set_color('blue4')
            q.put(child_node)
        time.sleep(delay)


def dfs(b: board.Board, delay=0):
    start = None
    for row in b.cells:
        for cell in row:
            if cell.color == 'blue':
                start = cell

    q = queue.LifoQueue()
    q.put(TreeNode(start))
    while not q.empty():
        tree_node = q.get()
        neighbors = get_neighbors(b, tree_node.data)
        for neighbor in neighbors:
            child_node = TreeNode(neighbor, parent=tree_node)
            if child_node.data.color == 'yellow':
                return child_node
            else:
                neighbor.set_color('blue4')
            q.put(child_node)
        time.sleep(delay)


def manhattan(pt1: board.BoardCell, pt2: board.BoardCell):
    return abs(pt1.row - pt2.row) + abs(pt1.col - pt2.col)


def a_star(b: board.Board, delay=0):
    start = None
    goal = None
    for row in b.cells:
        for cell in row:
            if cell.color == 'blue':
                start = cell
            elif cell.color == 'yellow':
                goal = cell

    q = queue.PriorityQueue()
    start_node = TreeNode(start)
    start_node.cost = 0
    q.put(start_node)
    while not q.empty():
        tree_node = q.get()
        neighbors = get_neighbors(b, tree_node.data)
        for neighbor in neighbors:
            child_node = TreeNode(neighbor, parent=tree_node)
            if child_node.data.color == 'yellow':
                return child_node
            else:
                neighbor.set_color('blue4')
            child_node.cost = tree_node.cost - manhattan(tree_node.data, goal) + 1 + manhattan(neighbor, goal)
            q.put(child_node)
        time.sleep(delay)


def greedy(b: board.Board, delay=0):
    start = None
    goal = None
    for row in b.cells:
        for cell in row:
            if cell.color == 'blue':
                start = cell
            elif cell.color == 'yellow':
                goal = cell

    q = queue.PriorityQueue()
    start_node = TreeNode(start)
    start_node.cost = manhattan(start, goal)
    q.put(start_node)
    while not q.empty():
        tree_node = q.get()
        neighbors = get_neighbors(b, tree_node.data)
        for neighbor in neighbors:
            child_node = TreeNode(neighbor, parent=tree_node)
            if child_node.data.color == 'yellow':
                return child_node
            else:
                neighbor.set_color('blue4')
            child_node.cost = manhattan(neighbor, goal)
            q.put(child_node)
        time.sleep(delay)


def traceback(node: TreeNode):
    trace = []
    while node:
        trace.insert(0, node.data)
        node = node.parent
    return trace
