# App de recordatorios

# Bibliotecas

from datetime import date
from datetime import datetime

#Funcion para agregar tareas

def agregar_tarea ():
      opcion_añadir = int(input("Deseas agregar una tarea? Si=1, No=0"))
      while opcion_añadir == 1:
            tarea = str(input())

#Esta es la funcion para visualizar las tareas programadas para hoy
def conocer_tareas_hoy (matriz):  
      today = date.today()
      for i in matriz:
            if i == today:
                  print(i)  

"""
Con las funciones para comparar las tareas tengo un problema con la biblioteca,
pero de ahi en fuera ya arregle los problemas del avance pasado
"""                          

#Funcion para conocer las tareas pendientes
def conocer_tareas_pendientes (matriz):
      today = date.today()
      for i in matriz:
            if i < today:
                  print(i)
      

      
#Aqui inicia la ejecucion del codigo   
print ("Hola que gusto volver a vernos ¿Que deseas hacer?")
print ("Si desea añadir una tarea ingrese 1")
print ("Para ver sus tareas ingresa 2")
print ("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
print ("Por el contrario si lo que quiere es conocer sus tareas pasadas seleccione 4")

seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 1:
      seleccion_2 = int(input("Deseas agregar una tarea? Si=1, No=0: "))
      mat = []
      while seleccion_2 == 1:
            materia = str(input("Especifique la materia de la tarea: "))
            descripcion = str(input("Escriba una breve descripcion de su tarea: "))
            date_dia = int(input ("¿Que dia lo entrega?: "))
            date_mes = int(input ("¿En que mes lo entrega?: "))
            date_año = int(input ("¿De que año?: "))
            tarea = [materia, descripcion, date_dia, date_mes, date_año]
            mat.append (tarea)
            print("Tarea creada con exito") 
            seleccion_2 = int(input("Deseas agregar una tarea? Si=1, No=0: "))
            
      print ("Para ver sus tareas ingresa 2")
      print ("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
      print ("Quiere conocer sus tareas pasadas seleccione 4")
      seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 2:
      print (mat)
      print ("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
      print ("Quiere conocer sus tareas pasadas seleccione 4")
      seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 3:
      print ("Sus tareas programadas para hoy son: ", conocer_tareas_pendientes(tarea))
      print ("Quiere conocer sus tareas pasadas seleccione 4")
      seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 4:
      print ("Sus tareas pendientes son: ", conocer_tareas_pendientes(tarea))
else:
      print("Opcion invalida")

print("¡Vuelva pronto!")