# App de recordatorios

from datetime import datetime #Importe un modulo para hacer uso de fechas
contador_a = int(1)           #Contador para llevar un recuento de las tareas
veces = int(0)                #Sirve como una variable para contar la cantidad de veces que se ve y almacena una tarea

#Esta es la funcion para llevar el recuento de las tareas
def total_de_tareas (contador_a, veces):        
      total_de_tareas = contador_a * veces
      return total_de_tareas

#Esta es la funcion para visualizar las tareas, una vez que ingresamos las tareas
def ver_tareas (mostrar_tareas, total_de_tareas):           
    mostrar_tareas = ("Tarea 1", agregar_tarea, "Tarea 2", agregar_tarea, "Tarea 3", agregar_tarea)
    total_de_tareas ()
    print (mostrar_tareas)
    print (total_de_tareas)
    return ver_tareas

#Esta es una funcion que permite agregar una tarea especificando la materia, la fecha y una breve descripcion de la misma
def agregar_tarea (materia, descripcion,date, veces):
     materia = str (input("Especifique la materia de la tarea"))
     descripcion = str (input("Escriba una breve descripcion de su tarea"))
     date = datetime(input ())
     veces = veces + 1
     return agregar_tarea [materia, descripcion,date]

      
"""Despues de esta funcion me gustaria crear un arreglo en donde tenga una matriz con las respuetas del usuario
y poder ir almacenadno las tareas con sus fechas y demas parametros """

#Aqui inicia la ejecucion del codigo   
print ("Hola que gusto volver a vernos ¿Deseas ver tus tarea o agrgar tareas?")

seleccion_1 = int (input ("Para ver tus tareas digita 1 para agregar digita 2: "))

if seleccion_1 == 1:
      ver_tareas ()
if seleccion_1 == 2: 
      agregar_tarea ()
      veces=1
elif seleccion_1 != 1 or 2:
      print ("Opcion invalida, por favor ingrese 1 o 2")
      seleccion_1 (input())
else:
      print("!Gracias por organizarte con nosotros vuelve pronto¡")