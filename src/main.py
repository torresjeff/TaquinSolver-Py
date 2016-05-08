import client as taquin


def main():
    matrix = taquin.generate_matrix(5)
    domain = input("Ingrese el nombre de dominio: ")
    pid = input("Ingrese el id del jugador: ")
    pid = int(pid)
    opponent = input("Ingrese el id del oponente: ")
    opponent = int(opponent)
    name = input("Ingrese el nombre del jugador: ")
    taquin.create_player(domain, pid, name)
    taquin.challenge(domain, matrix, 1, 1, opponent)
    while True:
        direccion = input("Ingrese la direccion r, l, u, d, magic ")
        if direccion == "r":
            taquin.move_right(domain, pid)
        elif direccion == "l":
            taquin.move_left(domain, pid)
        elif direccion == "u":
            taquin.move_up(domain, pid)
        elif direccion == "d":
            taquin.move_down(domain, pid)
        elif direccion == "magic":
            taquin.check(domain, pid)
        print("Tablero actual:")
        print(taquin.get_board(domain, pid))


if __name__ == '__main__':
    main()
