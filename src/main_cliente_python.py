import client as taquin


def main():
    matrixG = taquin.generate_matrix( 12 )
    matrix = taquin.generate_matrix( 9 )
    domain = input("Ingrese el nombre de dominio: ")
    pid = input("Ingrese el id del jugador: ")
    pid = int(pid)
    opponent = input("Ingrese el id del oponente: ")
    opponent = int(opponent )
    name = input("Ingrese el nombre del jugador: ")
    taquin.generateBoard(domain, matrixG, 1, 1)
    taquin.create_player(domain, pid, name)
    taquin.challenge(domain, matrix, 1, 1, opponent)
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

if __name__ == '__main__':
    main()
