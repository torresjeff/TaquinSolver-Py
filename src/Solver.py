from heapq import heapify,  heappop, heappush
# from Board import *


class Solver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        if self.board.is_solved():
            return self.board

        heap = self.board.possible_movements()  # genera los arboles hijos con los posibles movimientos
        min_cost_board = heappop(heap)  # retiramos el tablero con menor costo
        # print("solve, cost = %i" % (min_cost_board.cost()))
        #print("solve, heap = ", heap)
        #print("solve, min_cost_board: ", min_cost_board)
        #print("solve, min_cost_board.parent: ", min_cost_board.previous)
        while not min_cost_board.is_solved() and len(heap) > 0:
            heap.extend(min_cost_board.possible_movements())
            heapify(heap)
            min_cost_board = heappop(heap)
            #print("solve, min_cost_board: ", min_cost_board)
            #print("solve, min_cost_board.parent: ", min_cost_board.previous)
            # print("solve, cost = %i" % (min_cost_board.cost()))
            #print("solve, heap = ", heap)

        print("Se resolvio en tablero en %i movimientos" % min_cost_board.movements())
        print("Tablero inicial: ", self.board)
        print("Tablero final: ", min_cost_board)
        # print(min_cost_board)
        return min_cost_board
