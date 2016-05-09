from heapq import heapify,  heappop, heappush
# from Board import *


class Solver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        if self.board.is_solved():
            return self.board

        heap = self.board.possible_movements()
        min_cost_board = heappop(heap)
        print("solve, cost = %i" % (min_cost_board.cost()))
        while not min_cost_board.is_solved() and len(heap) > 0:
            heap.extend(min_cost_board.possible_movements())
            heapify(heap)
            min_cost_board = heappop(heap)
            print("solve, cost = %i" % (min_cost_board.cost()))
            print("heap = ", heap)
        return min_cost_board
