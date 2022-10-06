"""
Proyecto final TC1028.
Pensamiento Computacional para ingenieria.
Profesor: Benjamín Valdés Aguirre.
Nombre: Emanuel Josué Vega González.
ID: A01710366.
El programa funciona como una aplicacion de tareas, que se guardan en listas,
el usuario puede ver sus tareas de acuerdo al dia que se entrega, el programa 
busca la fecha dentro de la matriz.
"""

# Bibliotecas

from datetime import date
from datetime import datetime
from itertools import chain

"""
================== funciones principales =======================================
"""

#Esta es la funcion para visualizar las tareas programadas para hoy
def conocer_tareas_hoy(matriz):  
      today = 4
      for i in matriz:
            if i[2] == today:
                  print(i)  

                     
#Funcion para conocer las tareas pasadas
def conocer_tareas_pasadas(matriz):
      today = 4
      for i in matriz:
            if i[2] < today:
                  print(i)

#Mensaje de bienvendida
def bienvenida():    
      a = ("Hola que gusto volver a vernos ¿Que deseas hacer?")
      b = ("Si desea añadir una tarea ingrese 1")
      c = ("Para ver sus tareas ingresa 2")
      d = ("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
      e = ("Si lo que quiere es conocer sus tareas pasadas seleccione 4")
      mensaje = [
            [a],
            [b],
            [c],
            [d],
            [e],
      ]
      return mensaje

def imprime_mensaje():
      imprimir = bienvenida()
      for i in imprimir:
            print(i)

def imprime_por_opcion(seleccion):
      descartar = bienvenida()
      descartar.remove(0)
      if seleccion == 1:
            descartar.remove(1)
            for i in descartar:
                  print(i)
      if seleccion == 2:
            descartar.remove(2)
            for i in descartar:
                  print(i)
      if seleccion == 3:
            descartar.remove(3)
            for i in descartar:
                  print(i)
      if seleccion == 4:
            descartar.remove(4)
            for i in descartar:
                  print(i)



#Aqui inicia la ejecucion del codigo   
imprime_mensaje()
seleccion_1 = int (input ("Escriba la opcion deseada: "))
while seleccion_1 < 1 or seleccion_1 > 4:
      print("Opcion invalida, vuelve a intentarlo")
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
      print ("Sus tareas programadas para hoy son: ", conocer_tareas_hoy(mat))
      print ("Quiere conocer sus tareas pasadas seleccione 4")
      seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 4:
      print ("Sus tareas pendientes son: ", conocer_tareas_pasadas(mat))
else:
      print("Opcion invalida")

print("¡Vuelva pronto!")