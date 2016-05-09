from copy import deepcopy
from heapq import heapify,  heappop, heappush


class Board:

    # Constructor que recibe un tablero.
    # mat = tablero, n = numero de filas, x = fila de la pieza vacia, y = columna de la pieza vacia, previous_board = arbol padre
    def __init__(self, mat, n, x, y, previous_board=None):
        self.matrix = mat
        self.size = n
        self.previous = previous_board
        self.priority_queue = []
        self.x = x
        self.y = y

    # Retorna el tamaño del tablero (numero de filas)
    def size(self):
        return self.size

    # Retorna True si la pieza "en blanco" se encuentra en una fila impar, False si está en una fila par
    def blank_piece_odd_row(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] is None:
                    row = ((self.size - 1) - i)
                    return row % 2 == 0

    # Retorna True si el tablero se puede resolver, False si no se puede resolver
    def is_solvable(self):
        l = []

        for i in range(self.size):
            for j in range(self.size):
                l.append(self.matrix[i][j])

        inversions = self.count_inversions(l)

        return ((self.size % 2 != 0) and (inversions % 2 == 0)) or ((self.size % 2 == 0) and (self.blank_piece_odd_row() == (inversions % 2 == 0)))

    # Cuenta el numero de inversiones de un tablero. Las inversiones se pueden pensar de la siguiente manera:
    # Matriz = [[3, 2, 1]
    #           [4, 8, 5],
    #           [6, 7, None]]
    # 1) Convertir la matriz en una sola fila: [3, 2, 1, 4, 8, 5, 6, 7, None]
    # 2) Las inversiones son las veces que un numero mayor precede a los que son menores que el.
    #    Por ejemplo: en la lista anterior el 3 es el primer elemento. Los elementos menores que 3 que están despues de él son 2 y 1, por lo tanto el 3 produce 2 inversiones.
    #    El elemento "2" produce 1 inversión porque de los elementos que le siguen solo el 1 es menor que él.
    #    El elemento "8" produce 3 inversiones porque 5, 6, 7 son menores que el.
    # 3) El tablero solucionado tiene 0 inversiones
    def count_inversions(self, l):
        inversions = 0
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] is not None and l[j] is not None:
                    if l[i] > l[j]:
                        inversions += 1

        return inversions

    # Determina el costo del tablero utilizando la distancia Manhattan: https://es.wikipedia.org/wiki/Geometr%C3%ADa_del_taxista
    def cost(self):
        cost = 0
        print("cost:")
        print(self.matrix)
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] is not None:
                    row = abs(int(self.matrix[i][j] / self.size))
                    column = abs(int(self.matrix[i][j] % self.size))
                    if column == 0:
                        column = self.size - 1
                        row -= 1
                    else:
                        column -= 1
                    print("cost for %i = %i" % (self.matrix[i][j], abs(row-i) + abs(column-j)))
                    cost += abs(row-i) + abs(column-j)
        return cost

    # Retorna True si el tablero se encuentra en el estado resuelto, False si no
    def is_solved(self):
        current = 1
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != current and self.matrix[i][j] is not None:
                    return False
                current += 1
        return True

    # Genera los tableros hijos y los guarda en la cola de prioridad, el primer elemento es el de mayor prioridad (menor costo, el mejor)
    def possible_movements(self):
        boards = []
        if self.can_move_up():
            board = self.move_up()
            # print("move_up: ", board)
            if board != self:
                boards.append(board)
        if self.can_move_left():
            # print("move_left: ", board)
            board = self.move_left()
            if board != self:
                boards.append(board)

        if self.can_move_right():
            # print("move_right: ", board)
            board = self.move_right()
            if board != self:
                boards.append(board)

        if self.can_move_down():
            board = self.move_down()
            # print("move_down: ", board)
            if board != self:
                boards.append(board)

        # heappush(heap, boards)
        # TODO: optimizar, no hacer heapify cada vez
        heapify(boards)
        # heap.append(boards)
        # heapify(heap)
        return boards

    # verifica que la ficha vacía se pueda mover hacia arriba
    def can_move_up(self):
        return self.x > 0

    # crea un nuevo objeto Board con la nueva configuracion (ficha vacía hacia arriba)
    def move_up(self):
        board = deepcopy(self.matrix)
        board[self.x][self.y], board[self.x - 1][self.y] = board[self.x - 1][self.y], board[self.x][self.y]  # swap
        new_board = Board(board, self.size, self.x - 1, self.y, self)
        print("move_up: ", board)
        return new_board

    # verifica que la ficha vacía se pueda mover hacia abajo
    def can_move_down(self):
        return self.x < self.size-1

    # crea un nuevo objeto Board con la nueva configuracion (ficha vacía hacia abajo)
    def move_down(self):
        board = deepcopy(self.matrix)
        board[self.x][self.y], board[self.x + 1][self.y] = board[self.x + 1][self.y], board[self.x][self.y]  # swap
        new_board = Board(board, self.size, self.x + 1, self.y, self)
        print("move_down: ", board)
        return new_board

    # verifica que la ficha vacía se pueda mover hacia la izquierda
    def can_move_left(self):
        return self.y > 0

    # crea un nuevo objeto Board con la nueva configuracion (ficha vacía a la izquierda)
    def move_left(self):
        board = deepcopy(self.matrix)
        board[self.x][self.y], board[self.x][self.y - 1] = board[self.x][self.y - 1], board[self.x][self.y]  # swap
        new_board = Board(board, self.size, self.x, self.y - 1, self)
        print("move_left: ", board)
        return new_board

    # verifica que la ficha vacía se pueda mover hacia la derecha
    def can_move_right(self):
        return self.y < self.size-1

    # crea un nuevo objeto Board con la nueva configuracion (ficha vacía a la derecha)
    def move_right(self):
        board = deepcopy(self.matrix)
        board[self.x][self.y], board[self.x][self.y + 1] = board[self.x][self.y + 1], board[self.x][self.y]  # swap
        new_board = Board(board, self.size, self.x, self.y + 1, self)
        print("move_right: ", board)
        return new_board

    # Equivalente al "Comparator" de Java, determina si un tablero es igual a otro si las fichas estan en las mismas posiciones. Si son iguales no se vuelven a calcular sus posibles movimientos.
    def __eq__(self, other):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    # Se utiliza para comparar si un tablero es menor que otro (más barato), se hace comparando los costos de ambos tableros
    def __lt__(self, other):
        return self.cost() < other.cost()

    # "toString()"
    def __str__(self):
        # string = "["
        return str(self.matrix)

    # "toString()"
    def __repr__(self):
        return self.__str__()




