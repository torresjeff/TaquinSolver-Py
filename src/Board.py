
class Board:

    def __init__(self, mat, n):
        self.matrix = mat
        self.size = n

    # retorna el tamaño del tablero (numero de filas)
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

        return ((self.size % 2 != 0) and (inversions % 2 == 0)) or (
        (self.size % 2 == 0) and (self.blank_piece_odd_row() == (inversions % 2 == 0)))


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