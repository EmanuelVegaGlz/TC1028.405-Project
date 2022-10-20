# *App de recordatorios*
#### *TC1028.405*
#### **Nombre:** Emanuel Vega
#### **ID:** A01710366

## Contexto

Recientemente muchos de nosotros hemos empezado una nueva etapa en nuestras vidas al entrar a primer semestre de la vida universitaria, por lo que como alumnos necesitamos de herramientas que nos puedan hacer más placentera esta experiencia así como facilitarnos la vida durante nuestra carrera profesional, por lo que tener una herramienta la cual nos pueda ayudar gestionar nuestros tiempos es algo de gran utilidad, al poder tener un control de las actividades que tenemos que realizar para no pasar por alto ninguna y tener un excelente desempeño académico.

La manera en que funciona el algoritmo que ideé, es la siguiente; el programa cuenta con un menú de 6 opciones que puede navegar entre ellas ya que se implementó un ciclo while, antes de entrar al menú hay una función para validar que se ingrese una opción válida y no salga por default en la primera iteración, después de entrar al menú se le pedirá que ingrese numéricamente la opción que desea, siendo del 1 al 6 las opciones validas, si ingresa un numero entero diferente el programa terminara y desplegara un mensaje de despedida.

**Opción 1:** Esta opción es para agregar tareas a la aplicación, el programa le pide al usuario mediante inputs que ingrese la materia y una descripción de su tarea, así como el día, mes y año, implementando una función para validar que los datos ingresados sean reales para que se puedan comparar con la librería en otras opciones del menú. Estas variables se almacenan en una lista, y esa lista se guarda en otra lista que contiene todas las tareas. Adicional cada tarea que se genera se escribe en un archivo para que no se quede solo en la RAM y se pueda almacenar los datos una vez que el programa termina.

**Opción 2:** Muestra todas las tareas que se agreguen durante la ejecución del programa.

**Opción 3:** Buscara dentro de la lista de listas de tareas, las tareas que la fecha coincidan con la fecha actual haciendo uso de la biblioteca datetime. Únicamente con las tareas que se agreguen durante la ejecución del programa.

**Opción 4:** De igual manera hace una búsqueda con un ciclo for dentro de la lista de listas de tareas (declarada como mat) y muestra las tareas pasadas. Únicamente con las tareas que se agreguen durante la ejecución del programa.

**Opción 5:** En esta opción del menú de la misma forma se hace una búsqueda, pero, solo despliega las tareas que se entregan mañana. Únicamente con las tareas que se agreguen durante la ejecución del programa.

**Opción 6:** Aquí se puede ver el historial del programa y observar todas las tareas que se han añadido durante todas las ejecuciones del programa, a través de leer e imprimir el archivo de tareas.txt.




### Pseudocódigo:
        subproceso(tareas_hoy):
                leer (lista_de_tareas)
                si fecha_tareas == fecha_actual:
                    escribir(tareas)

        subproceso(tareas_mañana):
                leer (lista_de_tareas)
                si fecha_tareas == fecha_actual + 1:
                    escribir(tareas)

        subproceso(tareas_pasadas):
                leer (lista_de_tareas)
                si fecha_tareas < fecha_actual:
                    escribir(tareas)

        escribir("Hola que gusto volver a vernos ¿Que deseas hacer?")
        escribir("Si desea añadir una tarea ingrese 1")
        escribir("Para ver sus tareas ingresa 2")
        escribir("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
        escribir("Si lo que quiere es conocer sus tareas pasadas seleccione 4")
        escribir("Ver las tareas de mañana ingrese 5")
        escribir("Ver su historial (Tareas agregadas en otras ocaciones) opcion 6")

        input int <- seleccion

        mientras seleccion > 0 y seleccion < 7:

        repetir:

            si seleccion == (1):
                input str <- materia
                input str <- descripcion
                input int <- fecha
                tarea <- [materia,descripcion,fecha]
                abrir tareas.txt
                tareas.txt <- lista_de_tareas
                cerrar tareas.txt
                input int <- seleccion

            si seleccion == (2):
                entonces escribir (lista_de_tareas)
                input int <- seleccion

            si seleccion == (3):
                entonces ejecutar subproceso (tareas_hoy)
                input int <- seleccion

            si seleccion == (4):
                entonces ejecutar subproceso (tareas_pasadas)
                input int <- seleccion

            si seleccion == (5):
                entonces ejecutar subproceso (tareas_mañana)
                input int <- seleccion

            si seleccion == (6):
                entonces abrir tareas.txt
                escribir(tareas.txt)
                cerrar tareas.txt

            fin si

        escribir("¡Vuelva pronto!")

## Instrucciones

Descargar el archivo y correr en terminal con:

    python App_de_recordatorios.py

o abrir en Thonny y dar boton de play.


Leer los mensajes que se despliegan en el programa y seleccionar las opciones del menú e ingresar los datos de tus tareas, no puedas acceder a todas las funcionalidades si antes no ingresas tus tareas, el programa tiene instrucciones, usa bibliotecas date de dateime y os.

**Recomendaciones para un funcionamiento optimo:**

Procura agregar más de 5 tareas, al menos una que sea para el día actual y otra para mañana.
De igual manera el programa crea el archivo "tareas.txt" en la carpeta en la que se encuentre el código, por lo que se sugiere no cambies de ubicación el archivo, ya que el programa creara otro y se perderán las tareas que generaste.

## Referencias

El código incorpora las bibliotecas **datetime** y **os**.

La biblioteca **datetime** funciona para obtener la fecha del día de hoy, lo que yo hago es obtener el día, el mes y el año actual, los almaceno en una variable y hago comparaciones con las variables ingresadas por el usuario para que a través de condicionales poder determinar que tareas son para hoy, mañana o tareas pasadas.
Es una biblioteca estándar y me apoye de estos recursos para poder implementarlo en el proyecto:

- W3Schools. (2022). Python Datetime. Refsnes Data. Recuperado 20 de octubre de 2022 de, https://www.w3schools.com/python/python_datetime.asp
- Python Software Foundation. (2022) datetime — Basic date and time types. Python Software Foundation. Recuperado 20 de octubre de 2022 de, https://docs.python.org/3/library/datetime.html


Por otra parte la biblioteca **os**, sirve para poder manipular rutas de los archivos en el sistema, este API lo utilizo para validar que el archivo de tareas.txt existe en la carpeta donde se encuentra el programa y si no crear un archivo en blanco y que no truene el programa al momento de seleccionar la opción 6.
Me apoye de la siguiente documentación para poder implementarlo:

- W3Schools. (2022). File Handling. Refsnes Data. Recuperado 20 de octubre de 2022 de, https://www.w3schools.com/python/python_file_handling.asp
- Python Software Foundation. (2022) os — Interfaces misceláneas del sistema operativo. Python Software Foundation. Recuperado 20 de octubre de 2022 de,  
https://docs.python.org/es/3.10/library/os.html
