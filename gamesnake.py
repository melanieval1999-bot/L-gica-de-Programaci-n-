import curses
from random import randint

# setup window
curses.initscr()
win = curses.newwin(30, 90, 0, 0) # y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)

ESC = 27

# ---------- PANTALLA DE INICIO ----------
win.nodelay(0)  # modo bloqueante para esperar la tecla

while True:
    win.clear()
    win.border(0)
    win.addstr(10, 25, "JUEGO DE LA SERPIENTE")
    win.addstr(12, 20, "Presiona ENTER para iniciar la partida")
    win.addstr(14, 23, "Presiona ESC para salir")
    win.refresh()

    key_start = win.getch()
    if key_start in [10, 13]:  # ENTER (según sistema puede ser 10 o 13)
        break
    if key_start == ESC:
        curses.endwin()
        exit()

# ---------- BUCLE DE PARTIDAS ----------
while True:
    win.nodelay(1)

    # snake and food
    # (cabeza a la derecha para que no se pise al moverse)
    snake = [(3,13), (3,12), (3,11)]
    food = (10,20)

    win.clear()
    win.border(0)
    win.addch(food[0], food[1], '#')

    # game logic 
    score = 0
    key = curses.KEY_RIGHT
    perdio = False

    # ---------- BUCLE PRINCIPAL DEL JUEGO ----------
    while True:
        win.addstr(0, 2, 'Score ' + str(score) + ' ')
        win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed 

        prev_key  = key
        event = win.getch()
        key = event if event != -1 else prev_key

        # salir directamente si presiona ESC durante la partida
        if key == ESC:
            curses.endwin()
            print(f"Final score = {score}")
            exit()

        if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = prev_key

        # calcula la siguiente
        y = snake[0][0]
        x = snake[0][1]
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_LEFT:
            x -= 1
        if key == curses.KEY_RIGHT:
            x += 1

        snake.insert(0, (y, x))  # nueva cabeza

        # comprobar si se llega al borde
        if y == 0 or y == 29 or x == 0 or x == 89:
            perdio = True
            break

        # si la serpiente se choca consigo misma
        if snake[0] in snake[1:]:
            perdio = True
            break

        if snake[0] == food: 
            # eat the food
            score += 1
            food = ()
            while food == ():
                food = (randint(1, 28), randint(1, 88))
                if food in snake:
                    food = ()
                win.addch(food[0], food[1], '#')
        else:
            # move snake
            last = snake.pop()
            win.addch(last[0], last[1], ' ')

        win.addch(snake[0][0], snake[0][1], '*')

    # ---------- PANTALLA DE GAME OVER ----------
    if perdio:
        win.nodelay(0)  # esperar teclas
        while True:
            win.clear()
            win.border(0)
            win.addstr(10, 30, "GAME OVER")
            win.addstr(12, 28, f"Puntaje: {score}")
            win.addstr(14, 18, "Presiona ENTER para jugar de nuevo")
            win.addstr(16, 23, "Presiona ESC para salir")
            win.refresh()

            k = win.getch()
            if k in [10, 13]:  # ENTER → nueva partida
                break
            if k == ESC:      # ESC → salir del juego
                curses.endwin()
                print(f"Final score = {score}")
                exit()
        # si presiona ENTER, se repite el while True grande y crea una nueva partida