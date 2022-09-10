# App de recordatorios

from datetime import datetime #Importe un modulo para hacer uso de fechas
contador_a = int(0)           #Contador para llevar un recuento de las tareas



#Esta es la funcion para visualizar las tareas, una vez que ingresamos las tareas

def vista_tarea (tarea):           
    mostrar_tareas = ["Tarea 1", tarea, "Tarea 2", tarea, "Tarea 3", tarea]  #Aqui estoy tratando de crear una matriz :)
    return mostrar_tareas

#Esta es la funcion para visualizar las tareas programadas para hoy
def conocer_tareas_hoy (tarea):
      pendientes = tarea ([date_dia] == datetime)  #No estoy seguro si es la forma correcta para comparar la fecha de la lista/ 
      return pendientes                        #con la fecha del dia para poder determinar las tareas para hoy, pero esa es la idea.

#Funcion para conocer las tareas pendientes
def conocer_tareas_pendientes (tarea):
      pendientes = tarea ([date_dia] < datetime)
      return pendientes

      
#Aqui inicia la ejecucion del codigo   
print ("Hola que gusto volver a vernos ¿Que deseas hacer?")
print ("Si desea añadir una tarea ingrese 1")
print ("Para ver sus tareas ingresa 2")
print ("Desea visualizar sus tareas que tienes programadas para hoy digite 3")
print ("Por el contrario si lo que quiere es conocer sus tareas pasadas seleccione 4")

seleccion_1 = int (input ("Escriba la opcion deseada: "))

if seleccion_1 == 1:
      seleccion_2 = int(input("Deseas agregar una tarea? Si=1, No=0"))
      while seleccion_2 == 1:
            materia = str (input("Especifique la materia de la tarea: "))
            descripcion = str (input("Escriba una breve descripcion de su tarea: "))
            date_dia = int(input ("¿Que dia lo entrega?: "))
            date_mes = int(input ("¿En que mes lo entrega?: "))
            date_año = int(input ("¿De que año?: "))
            tarea = [materia, descripcion, date_dia, date_mes, date_año]
            print ("Tarea creada con exito")
            seleccion_2 = int(input("Deseas agregar otra tarea? Si=1, No=0"))
      if seleccion_2 == 0:
            print ("De acuerdo vuelva pronto")
      else:
            print("opcion invalida")

if seleccion_1 == 2:
      ver = vista_tarea(tarea)  
      print (ver)

if seleccion_1 == 3:
      print ("Sus tareas programadas para hoy son: ", conocer_tareas_pendientes(tarea))

if seleccion_1 == 4:
      print ("Sus tareas pendientes son: ", conocer_tareas_pendientes(tarea))
else:
      print("Opcion invalida")