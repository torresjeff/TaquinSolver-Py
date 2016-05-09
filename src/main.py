import client as taquin
from solver import *


def main():

    # TODO: uncomment. Por ahora no nos interesa utilizar la interfaz grafica
    """
    domain = "http://localhost:8080" # domain al que nos vamos a conectar
    pid = input("Ingrese el id del jugador: ")
    pid = int(pid)
    name = input("Ingrese el nombre del jugador: ")
    taquin.create_player(domain, pid, name)
    """

    option = int(input("1) Single player, 2) Resolver un reto (Multiplayer), 3) Retar a un jugador, -1) salir\n"))
    while option != -1:
        if option == 1:
            size = int(input("Ingrese el tamaño N del tablero: "))
            matrix = taquin.generate_matrix(size)  # generamos una matrix de size * size

            # TODO: uncomment. Por ahora no nos interesa utilizar la interfaz grafica
            # taquin.generateBoard(domain, matrix, size-1, size-1) # mandamos la matriz para que se display en la pagina

            if is_solvable(matrix, size):
                print("El tablero SI se puede resolver")
                #Llamar funcion que resuelva el tablero
                
            else:
                print("El tablero NO se puede resolver")

            """
            while True:
                direction = input("Ingrese la direccion r, l, u, d, magic ")
                if direction == "r":
                    taquin.move_right(domain, pid)
                elif direction == "l":
                    taquin.move_left(domain, pid)
                elif direction == "u":
                    taquin.move_up(domain, pid)
                elif direction == "d":
                    taquin.move_down(domain, pid)
                elif direction == "magic":
                    taquin.check(domain, pid)
                    taquin.check(domain, pid)
                    taquin.check(domain, pid)
                    taquin.check(domain, pid)
                    taquin.check(domain, pid)
            """

        elif option == 2:  # todavia no sirve
            taquin.get_challenge(domain, pid)
        elif option == 3:
            opponent = input("Ingrese el id del oponente: ")
            opponent = int(opponent)
            size = int(input("Ingrese el tamaño N del tablero: "))
            matrix_challenge = taquin.generate_matrix(size)
            taquin.challenge(domain, matrix_challenge, 1, 1, opponent)
            print("Reto enviado: ")
            print(matrix_challenge)

        option = int(input("1) Single player, 2) Resolver un reto (Multiplayer), 3) Retar a un jugador, -1) salir\n"))


if __name__ == '__main__':
    main()
