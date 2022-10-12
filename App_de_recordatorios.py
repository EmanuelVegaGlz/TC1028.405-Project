"""
Proyecto final TC1028.
Pensamiento Computacional para ingenieria.
Profesor: Benjamín Valdés Aguirre.
Nombre: Emanuel Josué Vega González.
ID: A01710366.
El programa es una aplicacion de tareas, que se guardan en listas,
el usuario puede ver sus tareas de acuerdo al dia que se entrega, el programa 
busca la fecha dentro de la matriz.
"""

# Bibliotecas

from datetime import date
from datetime import datetime

"""
================== funciones principales =======================================
"""

def conocer_tareas_hoy(matriz):

      """
      (Operadores, funciones, listas, listas anidadas, ciclos y condicionales)
      recibe: matriz lista anidada
      Compara las fechas de una lista de tareas con la fecha de la biblioteca
      datetime, si son iguales se guardan en otra lista
      Devuelve: Una nueva lista anidada con la recopilacion de las fechas 
      que cumplen la condicion
      """  

      today = date.today()
      dia_actual = today.day
      mes_actual = today.month
      año_actual = today.year
      t_hoy = []
      for i in matriz:
            if i[3] == dia_actual and i[5] == mes_actual\
                  and i[7] == año_actual:
                  t_hoy.append(i)  
      return t_hoy
                     
def conocer_tareas_pasadas(matriz):

      """
      (Operadores, funciones, listas, listas anidadas, ciclos y condicionales)
      recibe: matriz lista anidada
      Compara las fechas de una lista de tareas con la fecha de la biblioteca
      datetime y si son menores se guardan en otra lista
      Devuelve: Una nueva lista anidada con la recopilacion de las fechas 
      que cumplen la condicion
      """ 

      today = date.today()
      dia_actual = today.day
      mes_actual = today.month
      año_actual = today.year
      t_mañana = []
      for i in matriz:
            if i[3] > dia_actual or i[5] > mes_actual\
                  or i[7] > año_actual:
                  t_mañana.append(i)
      return t_mañana

def conocer_tareas_mañana(matriz):

      """
      (Operadores, funciones, listas, listas anidadas, ciclos y condicionales)
      Recibe: matriz lista anidada
      Compara las fechas de una lista de tareas con la fecha de hoy de la 
      biblioteca datetime buscando que la fecha de la lista sea un dia despues
      a la de hoy
      Devuelve: Una nueva lista anidada con la recopilacion de las fechas 
      que cumplen la condicion
      """ 

      today = date.today()
      dia_actual = today.day
      mes_actual = today.month
      año_actual = today.year
      t_mañana = []
      for i in matriz:
            if i[3] == dia_actual and i[5] == mes_actual\
                  and i[7] == año_actual:
                  t_mañana.append(i)
      return t_mañana

"""
================== funciones auxiliares  =======================================
"""

def bienvenida():    
      a = ("Hola que gusto volver a vernos ¿Que deseas hacer?")
      b = ("Si desea añadir una tarea ingrese 1")
      c = ("Para ver sus tareas ingresa 2")
      d = ("Desea visualizar sus tareas que tienes programadas para hoy\
            digite 3")
      e = ("Si lo que quiere es conocer sus tareas pasadas seleccione 4")
      mensaje = [
            a,
            b,
            c,
            d,
            e
      ]
      return mensaje

#Funcion para imprimir fila por fila
def imprime_mensaje(lista):
      for i in lista:
            print(i)

#Funcion para validar fecha
def valida(min,max,date,tipo):
      while date < min or date > max:
            print(tipo, date, " inexistente, intente de nuevo")
            date = int(input("Introduzca un valor real: "))
      return date

"""
========  Aqui inicia la ejecucion del codigo ==================================
"""

mat = []
imprime_mensaje(bienvenida())
seleccion_1 = int(input("Escriba la opcion deseada (Solo numeros): "))

while seleccion_1 < 1 or seleccion_1 > 4:
      print("Opcion inexistente, vuelve a intentarlo")
      seleccion_1 = int(input("Escriba la opcion deseada: "))

while seleccion_1 == 1 or 2 or 3 or 4:

      if seleccion_1 == 1:

            seleccion_2 = int(input("Deseas agregar una tarea? Si = 1, \
                  No != 1: "))
            while seleccion_2 == 1:
                  materia = str(input("Especifique la materia de la tarea: "))
                  descripcion = str(input("Escriba una breve descripcion de \
                        su tarea: "))
                  dia = int(input("¿Que dia lo entrega? (Solo numeros): "))
                  dia = valida(1,31,dia,"Dia")
                  mes = int(input("¿En que mes lo entrega? (Solo numeros): "))
                  mes = valida(1,12,mes,"Mes")
                  año = int(input("¿De que año? (Solo numeros): "))
                  año = valida(2000,3000,año,"Año")
                  tarea = [materia,descripcion, 'Fecha: ',dia,'/',mes,'/',año]
                  mat.append(tarea)
                  print("Tarea creada con exito") 
                  seleccion_2 = int(input("Deseas agregar otra tarea? Si=1, \
                        No=0: "))
            
            rango_bienvenida = bienvenida()
            for i in range(2,5):
                  print(rango_bienvenida [i])
            seleccion_1 = int(input("Escriba la opcion deseada: "))

      if seleccion_1 == 2:
            if mat == []:
                  print("No hay tareas")
            else:
                  imprime_mensaje(mat)
            rango_bienvenida = bienvenida()
            for i in range(3,5):
                  print(rango_bienvenida [i])
            seleccion_1 = int(input("Escriba la opcion deseada: "))

      if seleccion_1 == 3:
            
            if mat == []:
                  print("No hay tareas")
            else:
                  print("Sus tareas programadas para hoy son: ")
                  print(conocer_tareas_hoy(mat))
            msj = bienvenida()
            print(msj[4])
            seleccion_1 = int(input("Escriba la opcion deseada: "))

      if seleccion_1 == 4:
            print("Sus tareas pendientes son: ")
            conocer_tareas_pasadas(mat)
            if mat == []:
                  print("No hay tareas")

      else:
            print("Opcion invalida")

print("¡Vuelva pronto!")