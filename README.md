# App de recordatorios

E0(Bienvenida)
escribir "Hola que gusto volver a vernos
          ¿Deseas ver tus tarea o agrgar tareas?
          Para ver tus tareas digita 1 para agregar digita 2"

repetir mientras input != 1 o 2
si input <- 1
   ejecutar subproceso (vistatareas)
   si input <- 2
      ejecutar subproceso (agregartarea)
      sino
        escribir "Opcion invalida"
