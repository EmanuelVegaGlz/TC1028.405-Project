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

"""
================== funciones principales =======================================
"""

#Esta es la funcion para visualizar las tareas programadas para hoy
def conocer_tareas_hoy(matriz):  
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

                     
#Funcion para conocer las tareas pasadas
def conocer_tareas_pasadas(matriz):
      today = date.today()
      for i in matriz:
            for j in i:
                  if j[2] < today:
                        print(i)

#Funcion para conocer las tareas para mañana
def conocer_tareas_mañana(matriz):
      today = date.today()
      for i in matriz:
            for j in i:
                  if j[2] == today + 1:
                        print(i)

#Mensaje de bienvendida
def bienvenida():    
      a = ("Hola que gusto volver a vernos ¿Que deseas hacer?")
      b = ("Si desea añadir una tarea ingrese 1")
      c = ("Para ver sus tareas ingresa 2")
      d = ("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
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
def valida(min,max,date):
      while date < min or date > max:
            print("Dia ", date, " inexistente, intente de nuevo")
            date = int(input("Introduzca un valor real: "))


#Aqui inicia la ejecucion del codigo

imprime_mensaje(bienvenida())
seleccion_1 = int(input("Escriba la opcion deseada (Solo numeros): "))
while seleccion_1 < 1 or seleccion_1 > 4:
      print("Opcion invalida, vuelve a intentarlo")
      seleccion_1 = int(input("Escriba la opcion deseada: "))

if seleccion_1 == 1:
      seleccion_2 = int(input("Deseas agregar una tarea? Si = 1, No != 1: "))
      mat = []
      sl = str('/')
      while seleccion_2 == 1:
            materia = str(input("Especifique la materia de la tarea: "))
            descripcion = str(input("Escriba una breve descripcion de su tarea: "))
            dia = int(input("¿Que dia lo entrega? (Solo numeros): "))
            while dia < 1 or dia > 31:
                  print("Dia ", dia, " inexistente, intente de nuevo")
                  dia = int(input("¿Que dia lo entrega?"))
            mes = int(input("¿En que mes lo entrega? (Solo numeros): "))
            while mes < 1 or mes > 12:
                  print("Mes ", mes, " inexistente, intente de nuevo")
                  mes = int(input("¿En que mes lo entrega?: "))
            año = int(input("¿De que año? (Solo numeros): "))
            while año < 1:
                  print("Año ", año, " inexistente, intente de nuevo")
                  año = int(input("¿De que año?: "))
            tarea = [materia,descripcion, 'Fecha: ',dia,sl,mes,sl,año]
            mat.append(tarea)
            print("Tarea creada con exito") 
            seleccion_2 = int(input("Deseas agregar otra tarea? Si=1, No=0: "))
      
      rango_bienvenida = bienvenida()
      for i in range(2,5):
            print(rango_bienvenida [i])
      seleccion_1 = int(input("Escriba la opcion deseada: "))

if seleccion_1 == 2:
      imprime_mensaje(mat)
      rango_bienvenida = bienvenida()
      for i in range(3,5):
            print(rango_bienvenida [i])
      seleccion_1 = int(input("Escriba la opcion deseada: "))

if seleccion_1 == 3:
      print("Sus tareas programadas para hoy son: ")
      print(conocer_tareas_hoy(mat))

      msj = bienvenida()
      print(msj[4])
      seleccion_1 = int(input("Escriba la opcion deseada: "))

if seleccion_1 == 4:
      print("Sus tareas pendientes son: ")
      conocer_tareas_pasadas(mat)

else:
      print("Opcion invalida")

print("¡Vuelva pronto!")