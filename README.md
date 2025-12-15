Tema del proyecto: SNAKE GAME 

Objetivo: Desarrollar y presentar el software Snake Game como un producto informático funcional y escalable, demostrando la correcta aplicación de las herramientas aprendidas en clase para demostrar su usabilidad y potencial de adaptación para compradores o instituciones interesadas en soluciones digitales educativas y de entretenimiento.

Introducción: En el marco del proceso de selección y evaluación de software, y aplicando las herramientas estudiadas durante el curso: entre ellas análisis de requerimientos, diagramas de flujo, depuración, pruebas y documentación técnica presento el proyecto “Snake Game”, un programa desarrollado en Python que representa una solución lúdica, accesible y adaptable a diferentes contextos educativos y de entretenimiento digital. El propósito de este trabajo es demostrar cómo, a partir de principios fundamentales de la programación estructurada y del diseño de interfaces textuales, es posible construir un producto informático funcional, atractivo y escalable. El Snake Game integra elementos esenciales: uso de la librería curses para la construcción de interfaces interactivas, manejo de bucles, condiciones, listas dinámicas, control de eventos del teclado y gestión de estados, permitiendo así una experiencia de usuario fluida y coherente. 

Funcionalidades del juego: 

- Pantalla de inicio interactiva:
  
    Muestra un menú inicial con el título “JUEGO DE LA SERPIENTE”.
  
    Indica al usuario que puede presionar ENTER para iniciar o ESC para salir del programa.
  
    Usa curses en modo bloqueante para esperar la acción del jugador antes de comenzar.
  
- Ventana de juego personalizada con curses:
  
    Crea una ventana de tamaño fijo (30 x 90) con bordes visibles.
  
    Permite actualizar la pantalla de manera dinámica sin parpadeos.
  
    Muestra en la parte superior el puntaje actual (Score) durante toda la partida.
  
- Movimiento de la serpiente controlado por el teclado:
  
    La serpiente inicia con una posición y dirección predefinidas, moviéndose hacia la derecha.
  
    El jugador controla la dirección de la serpiente con las flechas del teclado (KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT).
  
    El programa valida que solo se acepten teclas válidas; si se presiona otra tecla, mantiene la dirección anterior.
  
- Gestión de la serpiente como lista dinámica:
  
    La serpiente se representa como una lista de tuplas (y, x), donde cada elemento es un segmento del cuerpo.
  
    En cada movimiento se inserta una nueva cabeza al inicio de la lista y se elimina el último segmento (cola), simulando el         desplazamiento.
  
    Cuando come comida, no se elimina la cola, por lo que la serpiente aumenta de longitud.
  
- Generación de comida aleatoria y sistema de puntaje:
  
    La comida se representa con el carácter # y se coloca en posiciones aleatorias con randint.
  
    Se verifica que la comida no aparezca sobre el cuerpo de la serpiente.
  
    Cuando la cabeza de la serpiente coincide con la posición de la comida:
  
    Aumenta el puntaje (score) en 1.
  
    Se genera una nueva comida en otra posición aleatoria válida.
  
- Detección de colisiones y condición de derrota:
  
    El juego detecta si la serpiente choca contra: Los bordes de la ventana (y == 0, y == 19, x == 0, x == 89).
  
    Su propio cuerpo (la cabeza aparece en alguna de las posiciones del resto de la lista).
  
    Si ocurre una colisión, se activa el estado de derrota (perdio = True) y se sale del bucle principal de juego.
  
- Pantalla de “Game Over” con opción de volver a jugar:
  
    Al perder, se muestra una pantalla de GAME OVER con el puntaje alcanzado.
  
    El usuario puede:
  
    Presionar ENTER para empezar una nueva partida (se reinicia todo el juego).
  
    Presionar ESC para salir definitivamente del juego.
  
    El bucle externo (while True grande) permite volver a crear una nueva partida sin cerrar el programa.
  
- Salida controlada con tecla ESC:
  
    En cualquier momento de la partida, si el usuario presiona ESC, el juego:
  
    Finaliza la ventana de curses con curses.endwin().
  
    Imprime en consola el puntaje final.
  
    Termina la ejecución del programa con exit().
  
Explicación del software: El Snake Game es un programa desarrollado en Python que utiliza la librería curses para crear una interfaz interactiva en la consola. El juego inicia con una pantalla de bienvenida donde el usuario decide si quiere comenzar una partida o salir. Una vez iniciada la partida, el jugador controla una serpiente que se desplaza por la ventana de juego utilizando las flechas del teclado. La serpiente debe comer la comida representada por el símbolo #, lo que aumenta su longitud y el puntaje del jugador.
Internamente, la serpiente se gestiona mediante una lista de coordenadas que se actualiza en cada ciclo del bucle principal. El software utiliza condiciones para detectar colisiones tanto con los bordes de la ventana como con el propio cuerpo de la serpiente. Cuando ocurre una colisión, se muestra una pantalla de “GAME OVER” donde el usuario puede elegir entre volver a jugar o salir del programa. En conjunto, el software integra manejo de bucles, condiciones, listas dinámicas, control de teclado y gestión de estados, lo que lo convierte en un ejemplo completo de aplicación interactiva en consola.
