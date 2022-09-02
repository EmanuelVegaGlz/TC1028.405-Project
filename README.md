# *App de recordatorios*

####                                                                                                                                         **Nombre:** Emanuel Vega
####                                                                                                                                             **ID:** A01710366

## Contexto

Recientemente muchos de nosotros hemos empezado una nueva etapa en nuestras vidas al entrar a primer semestre de la vida universitaria, por lo que como alumnos necesitamos de herramientas que nos puedan hacer más placentera esta experiencia así como facilitarnos la vida durante nuestra carrera profesional, por lo que tener una herramienta la cual nos pueda ayudar gestionar nuestros tiempos es algo de gran utilidad, al poder tener un control de las actividades que tenemos que realizar para no pasar por alto ninguna y tener un excelente desempeño académico.

La manera en que funciona el algoritmo que ideé, es la siguiente; el usuario entra a la aplicación y de entrada además de la bienvenida tendrá un menú principal con dos opciones, ver las tareas pendientes o agregar una tarea, al seleccionar agregar tarea el programa le pedirá al usuario que ingrese una serie de parámetros para poder almacenar las tarea, datos tales como lo son la materia, una breve descripción de la actividad y la fecha. Posteriormente podrá visualizar las tareas que tiene con la opción de ver todas las tareas, las tareas del día o las tareas previas. Con la opción de después de ver las tareas añadir otra.

La lógica del algoritmo es dividiendo las funciones por subprocesos para después invocarlos, de igual manera para las opciones hacia el usuario se ocupan condicionales y para el almacenamiento de tareas con sus respectivas características se hace uso de listas, para almacenar todas las tareas es una lista de la lista con las tareas y sus parámetros.



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

escribir ("Hola que gusto volver a vernos

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
