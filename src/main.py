import client as taquin
from Board import *
from Solver import *

def send_movements(domain, pid, movements):
    for i in movements:
        if i == "r":
            taquin.move_right(domain,pid)
        elif i == "l":
            taquin.move_left(domain,pid)
        elif i == "u":
            taquin.move_up(domain,pid)
        elif i == "d":
            taquin.move_down(domain,pid)

def main():
    # TODO: uncomment. Por ahora no nos interesa utilizar la interfaz grafica

    domain = "http://localhost:8181" # domain al que nos vamos a conectar
    pid = 1
    '''pid = int(pid)
    name = input("Ingrese el nombre del jugador: ")
    taquin.create_player(domain, pid, name)
    '''

    option = int(input("1) Single player, 2) Resolver un reto (Multiplayer), 3) Retar a un jugador, -1) salir\n"))
    while option != -1:
        if option == 1:
            # TODO: Por ahora solo sirve con tableros 2x2
            size = int(input("Ingrese el tamaño N del tablero: "))
            matrix = taquin.generate_matrix(size)  # generamos una matrix de size * size
            board = Board(matrix, size, size-1, size-1)

            # -------------- PARA PROBAR 2x2 ------------
            # matrix = [[3, 1],
            #          [2, None]]

            # board = Board(matrix, 2, 1, 1)
            # -------------------------------------------

            # TODO: uncomment. Por ahora no nos interesa utilizar la interfaz grafica
            taquin.generateBoard(domain, matrix, size-1, size-1) # mandamos la matriz para que se display en la pagina

            if board.is_solvable():
                print("El tablero SI se puede resolver")
                solver = Solver(board)
                movements = solver.solve()
                if len(movements) != 0:
                    send_movements(domain,pid,movements)

            else:
                print("El tablero NO se puede resolver")

        elif option == 2:  # todavia no sirve
            taquin.get_challenge(domain, pid)
        elif option == 3:
            opponent = input("Ingrese el id del oponente: ")
            opponent = int(opponent)
            size = int(input("Ingrese el tamaño N del tablero: "))
            matrix_challenge = taquin.generate_matrix(size)
            taquin.challenge(domain, matrix_challenge, size-1, size-1, opponent)
            print("Reto enviado: ")
            print(matrix_challenge)

        option = int(input("1) Single player, 2) Resolver un reto (Multiplayer), 3) Retar a un jugador, -1) salir\n"))


if __name__ == '__main__':
    main()
