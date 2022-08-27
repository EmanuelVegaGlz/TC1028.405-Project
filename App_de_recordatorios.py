# App de recordatorios



"""   print ("Estas son las actividades que tiene pendiente: ", todas_las_tareas)

      print ("¿Desea conocer que actividades tiene que entregar hoy? \n si escriba 1, no escriba 0")

input int <- (ctphoy)

      repetir mientras ctphoy ¡= (1 o 0)

      escribir ("Opcion no valida vuelva a intentarlo")


      si ctphoy = (1)

      entonces escribir (los espacios del array en donde (fecha)= date actual)

      si no

      escribir ("¿Quiere conocer sus tareas atrasadas?/

              si escriba 1, no escriba 0")

      input int <-(ctpendientes)

      repetir mientras ctpendientes ¡= (1 o 0)

      escribir ("Opcion no valida vuelva a intentarlo")

      si ctpendientes = 1

      entonces escribir (los espacios del array en donde (fecha) > date actual)

      si no

      escribir ("¿Quieres añadir otra tarea/

                si escriba 1, no escriba 0?")

      input int <- (mastarea)

      repetir mientras mastarea ¡= (1 o 0)

      escribir ("Opcion no valida vuelva a intentarlo")

      si mastarea = 1

      entonces ejecutar subproceso (agregartarea)

      si no

      escribir ("Actividades guardadas con exito, ¡Vuelva pronto!")

Fin subproceso"""

def ver_tareas ():
    print ("Viendo las tareas")
    return ver_tareas

def agregar_tarea (materia, actividades,date):
     materia = str (input("Especifique la materia de la tarea"))
     actividades = str (input("Escriba una breve descripcion de su tarea"))
     date = str (input ("¿Cuando se entrega su tarea?"))
     return agregar_tarea [materia, actividades,date]

"""Despues de esta funcion me gustaria crear un arreglo en donde tenga una matriz con las respuetas del usuario
y poder ir almacenadno las tareas con sus fechas y demas parametros """

   
print ("Hola que gusto volver a vernos ¿Deseas ver tus tarea o agrgar tareas?")

seleccion_1 = int (input ("Para ver tus tareas digita 1 para agregar digita 2: "))

if seleccion_1 == 1:
      ver_tareas ()
if seleccion_1 == 2: 
      agregar_tarea ()
elif seleccion_1 != 1 or 2:
      print ("Opcion invalida, por favor ingrese 1 o 2")
      seleccion_1 (input())
else:
      print("!Gracias por organizarte con nosotros vuelve pronto¡")