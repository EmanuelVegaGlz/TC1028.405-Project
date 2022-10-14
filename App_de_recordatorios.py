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
      vacio = ["¡No hay tareas para hoy!"]
      for i in matriz:
            if i[3] == dia_actual and i[5] == mes_actual\
                  and i[7] == año_actual:
                  t_hoy.append(i)  
      if t_hoy == []:
            return vacio
      else:
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
      t_pasadas = []
      vacio = ["¡No hay tareas pendientes!"]
      for i in matriz:
            if i[3] > dia_actual and i[5] == mes_actual and i[7] == año_actual:
                  t_pasadas.append(i)
            if i[3] == dia_actual and i[5] > mes_actual and i[7] == año_actual:
                  t_pasadas.append(i)
            if i[3] == dia_actual and i[5] == mes_actual and i[7] > año_actual:
                  t_pasadas.append(i)
      if t_pasadas == []:
            return vacio
      else:
            return t_pasadas

def conocer_tareas_mañana(matriz):

      """
      (Operadores, funciones, listas, listas anidadas, ciclos y condicionales)
      Recibe: matriz lista anidada
      Compara las fechas de una lista anidada de tareas con la fecha de hoy de la 
      biblioteca datetime buscando que la fecha de la lista sea un dia despues
      a la actual
      Devuelve: Una nueva lista anidada con la recopilacion de las fechas 
      que cumplen la condicion
      """ 

      today = date.today()
      dia_actual = today.day
      mes_actual = today.month
      año_actual = today.year
      t_mañana = []
      vacio = ["¡No hay tareas para mañana!"]
      for i in matriz:
            if i[3] == dia_actual+1 and i[5] == mes_actual\
                  and i[7] == año_actual:
                  t_mañana.append(i)
      if t_mañana == []:
            return vacio
      else:
            return t_mañana

"""
================== funciones auxiliares  =======================================
"""

def bienvenida():
      
      """
      (Funciones, listas, variables)
      Recibe: nada
      Funcion con una listas de mensajes para llamar la funcion e imprimir el
      mensaje de acuerdo al contexto
      Devuelve: Una lista de strings con mensajes
      """ 
    
      a = "Hola que gusto volver a vernos ¿Que deseas hacer?"
      b = "Si desea añadir una tarea ingrese 1"
      c = "Para ver sus tareas ingresa 2"
      d = "Desea visualizar sus tareas que tienes programadas para hoy digite 3"
      e = "Si lo que quiere es conocer sus tareas pasadas seleccione 4"
      f = "Ver las tareas de mañana ingrese 5"
      g = "Para cerrar la app ingrese cualquier otro número"
      mensaje = [
            a,
            b,
            c,
            d,
            e,
            f,
            g     
      ]
      return mensaje

def imprime_mensaje(lista):

      """
      (Funciones, listas, ciclos)
      Recibe: lista que es una lista
      Imprime elemento por elemento de una lista util para listas anidadas y
      darle "formato" a la impresion
      Devuelve: No tiene return porque el proposito de la funcion es imprimir
      """ 

      for i in lista:
            print(i)

def valida(min,max,date,tipo):
            
      """
      (Funciones, listas, variables, ciclos, operadores)
      Recibe:min limite inferior a validar
            max limite superior a validar
            date la variable a validar
            tipo para especificar que es la variable e imprimirlo como
            mensaje de error si es que no cumple con las condiciones
      Funcion para validar que los datos ingresados por el usuario sean reales
      utilizando un ciclo para poderlo comparar con la bibliteca datetime
      se que es una mala practica pedir inputs en una funcion, pero es necesario
      para que esta sea util.
      Devuelve: La variable ingresada por el usario despues de ser validada
      """ 
    
      while date < min or date > max:
            print(tipo, date," inexistente, intente de nuevo")
            date = int(input("Introduzca un valor real: "))
      return date

"""
========  Aqui inicia la ejecucion del codigo ==================================
"""
#Se inicializa una matriz vacia para guardar la listas de tareas
mat = []
welcome = bienvenida()
welcome.pop(6)
imprime_mensaje(welcome)
seleccion_1 = int(input("Escriba la opcion deseada (Solo numeros): "))

#Ciclo para validar que al iniciar el menu se seleccione una opcion valida
while seleccion_1 < 1 or seleccion_1 > 5:
      print("Opcion inexistente, vuelve a intentarlo")
      seleccion_1 = int(input("Escriba la opcion deseada: "))
      print("")

#Ciclo para ir a cualquier opcion dentro del menu y poder cerrar la app
while seleccion_1 == 1 or 2 or 3 or 4 or 5:

      #Agregar tareas
      if seleccion_1 == 1:
            seleccion_2 = int(input("Deseas agregar una tarea? Si = 1, No != 1: "))
            
            while seleccion_2 == 1:
                  materia = str(input("Especifique la materia de la tarea: "))
                  descripcion = str(input("Escriba una breve descripcion de su tarea: "))
                  dia = int(input("¿Que dia lo entrega? (Solo numeros): "))
                  dia = valida(1,31,dia,"Dia")
                  mes = int(input("¿En que mes lo entrega? (Solo numeros): "))
                  mes = valida(1,12,mes,"Mes")
                  año = int(input("¿De que año? (Solo numeros): "))
                  año = valida(2000,3000,año,"Año (aaaa)")
                  tarea = [materia,descripcion, 'Fecha: ',dia,'/',mes,'/',año]
                  mat.append(tarea)
                  print("Tarea creada con exito") 
                  print("")
                  seleccion_2 = int(input("Deseas agregar otra tarea? Si=1, No=0: "))
            
            #Opciones del menu, sin la opcion actual
            print("")
            mensaje_1 = bienvenida()
            mensaje_1.pop(0)
            mensaje_1.pop(0)
            imprime_mensaje(mensaje_1)
            seleccion_1 = int(input("Escriba la opcion deseada: "))
      
      #Mostrar tareas
      if seleccion_1 == 2:
            if mat == []:
                  print("No hay tareas")
            else:
                  imprime_mensaje(mat)
            
            #Opciones del menu, sin la opcion actual
            print("")
            mensaje_1 = bienvenida()
            mensaje_1.pop(0)
            mensaje_1.pop(1)
            imprime_mensaje(mensaje_1)
            seleccion_1 = int(input("Escriba la opcion deseada: "))

      #Mostrar tareas de hoy
      if seleccion_1 == 3:
            if mat == []:
                  print("No hay tareas")
            else:
                  print("Sus tareas programadas para hoy son: ")
                  imprime_mensaje(conocer_tareas_hoy(mat))
            
            #Opciones del menu, sin la opcion actual
            print("")
            mensaje_1 = bienvenida()
            mensaje_1.pop(0)
            mensaje_1.pop(2)
            imprime_mensaje(mensaje_1)
            seleccion_1 = int(input("Escriba la opcion deseada: "))

      #Mostrar tareas pasadas
      if seleccion_1 == 4:
            if mat == []:
                  print("No hay tareas")
            else:
                  print("Sus tareas pasadas son: ")
                  imprime_mensaje(conocer_tareas_pasadas(mat))
            
            #Opciones del menu, sin la opcion actual
            print("")
            mensaje_1 = bienvenida()
            mensaje_1.pop(0)
            mensaje_1.pop(3)
            imprime_mensaje(mensaje_1)
            seleccion_1 = int(input("Escriba la opcion deseada: "))
      
      #Mostrar tareas de mañana
      if seleccion_1 == 5:
            if mat == []:
                  print("No hay tareas")
            else:
                  print("Sus tareas para mañana son: ")
                  imprime_mensaje(conocer_tareas_mañana(mat))
            
            #Opciones del menu, sin la opcion actual
            print("")
            mensaje_1 = bienvenida()
            mensaje_1.pop(0)
            mensaje_1.pop(4)
            imprime_mensaje(mensaje_1)
            seleccion_1 = int(input("Escriba la opcion deseada: "))

print("¡Vuelva pronto!")