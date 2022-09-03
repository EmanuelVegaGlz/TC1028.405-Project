# App de recordatorios

from datetime import datetime #Importe un modulo para hacer uso de fechas
contador_a = int(1)           #Contador para llevar un recuento de las tareas
veces = int(0)                #Sirve como una variable para contar la cantidad de veces que se ve y almacena una tarea

def total_de_tareas (contador_a, veces):        
      tottareas = contador_a * veces
      return tottareas

#Esta es la funcion para visualizar las tareas, una vez que ingresamos las tareas

def vista_tarea (total_de_tareas):           
    mostrar_tareas = ("Tarea 1", agregar_tarea, "Tarea 2", agregar_tarea, "Tarea 3", agregar_tarea)
    
    return ver_tareas

def conocer_tareas_hoy (lista):
      tareas_de_hoy = lista(fecha == datetoday)
      return tareas_de_hoy

def conocer_tareas_pendientes (lista):
      pendientes = lista(fecha < datetoday)
      return pendientes

#Esta es una funcion que permite agregar una tarea especificando la materia, la fecha y una breve descripcion de la misma
def agregar_tarea (materia, descripcion,date,):
     materia = str (input("Especifique la materia de la tarea"))
     descripcion = str (input("Escriba una breve descripcion de su tarea"))
     date = datetime(input ("Cuando lo entrega"))
     nueva_tarea = [materia, descripcion,date]
     return nueva_tarea 

      
"""Despues de esta funcion me gustaria crear un arreglo en donde tenga una matriz con las respuetas del usuario
y poder ir almacenadno las tareas con sus fechas y demas parametros """

#Aqui inicia la ejecucion del codigo   
print ("Hola que gusto volver a vernos ¿Que deseas hacer?")
print ("Para ver tus tareas ingresa 1")
print ("Para ver las tareas que tienes programadas para hoy digita 2")
print ("Si deseas añadir una tarea ingrese 3")
print ("Por el contrario si lo que quiere es conocer las tareas programadas para hoy escriba 4")
print ("Desea visualizar sus tareas pasadas seleccione 5")
seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 1:
      vista_tarea (parametros)  
      print (vista_tarea)

if seleccion_1 == 2: 
      conocer_tareas_hoy (lista)
      print (conocer_tareas_hoy)

if seleccion_1 != 1 or 2:
      print ("Opcion invalida, por favor ingrese 1 o 2")
      seleccion_1 (input())
else:
      print("!Gracias por organizarte con nosotros vuelve pronto¡")