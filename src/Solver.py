from heapq import heapify,  heappop, heappush
# from Board import *


class Solver:
    def __init__(self, board):
        self.board = board

    def solve(self):
        print("Tablero a resolver: ", self.board)
        print("Resolviendo...")
        movements = []
        if self.board.is_solved():
            return movements
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
            # print("solve, heap = ", heap)

        back_min_cost_board = min_cost_board
        while back_min_cost_board is not None:
            parent = back_min_cost_board.previous
            if parent is not None:
                x, y = (parent.getX() - back_min_cost_board.getX()), (parent.getY() - back_min_cost_board.getY())
                if x == 0 and y > 0:  # si y es positivo el movimiento fue hacia la izquierda
                    movements.insert(0, "l")
                elif x == 0 and y < 0:  # si y es negativo el movimiento fue hacia la derecha
                    movements.insert(0, "r")
                elif x > 0 and y == 0:  # si x es positivo el movimiento fue hacia arriba
                    movements.insert(0, "u")
                elif x < 0 and y == 0:  # si x es negativo el movimiento fue hacia abajo
                    movements.insert(0, "d")
            back_min_cost_board = parent
        print("Se resolvio en tablero en %i movimientos" % min_cost_board.movements())
        print("Tablero inicial: ", self.board)
        print("Tablero final: ", min_cost_board)
        # print(min_cost_board)
        return movements
