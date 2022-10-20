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
subproceso (vistatarea):

        escribir ("Estas son las actividades que tiene pendiente", todaslastareas)

        escribir ("¿Desea conocer que actividades tiene que entregar hoy? si escriba 1, no escriba 0")

        input int <- conocer_tareas_hoy

        mientras conocer_tareas_hoy ¡= (1 o 0): 

            Repetir:

                escribir ("Opcion no valida vuelva a intentarlo")

        si conocer_tareas_hoy == (1):

            entonces escribir (los espacios del array en donde (fecha) == date actual)

        si no:

            escribir(de acuerdo)

        fin si        


        escribir ("¿Quiere conocer sus tareas atrasadas? si escriba 1, no escriba 0")

        input int <- conocer_pendientes ("Escribe tu opcion: ")

        si conocer_pendientes ¡= (1 o 0):

            entonces repetir:

                escribir ("Opcion no valida vuelva a intentarlo")

            de lo contrario si conocer_pendientes == 1:

                entonces escribir (los espacios del array en donde (fecha) > date actual)

        fin si


        escribir ("¿Quieres añadir otra tarea si escriba 1, no escriba 0?")

        input int <- mastarea ("Escribe tu opcion: ")

        mientras mastarea ¡= (1 o 0):

            repetir:

                escribir ("Opcion no valida vuelva a intentarlo")

        si mastarea = 1:

            entonces ejecutar subproceso (agregartarea)

        si no

                escribir ("Actividades guardadas con exito, ¡Vuelva pronto!")

        Fin subproceso



subproceso (agregartarea)

        escribir ("Especifique la materia de la tarea")

        input string <- (mat)

        escribir ("Escriba una breve descripcion de su tarea")

        input string <- (act)

        escribir ("¿Cuando se entrega su tarea?")

        input date <- (fecha)

        Crear array (actividades) ["Materia: " mat, "Tarea: " act, "Fecha: " fecha]

        Guardar array (actividades)

        Crear array (todaslastareas) [(actividades) 100]

        Fin subproceso



E0 (Bienvenida)

escribir ("Hola que gusto volver a vernos")

escribir ("¿Deseas ver tus tarea o agrgar tareas?")

escribir ("Para ver tus tareas digita 1 para agregar digita 2")

input int <- seleccion

mientras seleccion != 1 o 2:

    repetir:

        escribir ("Opcion invalida, por favor ingrese 1 o 2")

si seleccion == 1

    entonces ejecutar subproceso (vistatareas)

si no seleccion == 2

    ejecutar subproceso (agregartarea)

fin si
      

EF escribir ("¡Gracias por organizarte con nosotros!")

### Instrucciones

Descargar el archivo y correr en terminal con:

    python App_de_recordatorios.py

o abrir en Thonny y dar boton de play.

Seleccionar las opciones del menu e ingresar los datos de tus tareas, no puedas acceder a todas las funcionalidades si antes no ingresas tus tareas, el programa tiene instrucciones y usa biblioteca date de dateime. 
