# App de recordatorios



subproceso (vistatarea)

      escribir ("Estas son las actividades que tiene pendiente")

      escribir (todaslastareas)

      escribir ("¿Desea conocer que actividades tiene que entregar hoy?/

      si escriba 1, no escriba 0")

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

Fin subproceso



subproceso (agregartarea)

     escribir ("Especifique la materia de la tarea")

     input string <- (mat)

     escribir ("Escriba una breve descripcion de su tarea")

     input string <- (act)

     escribir ("¿Cuando se entrega su tarea?")

     input date <- (fecha)

     Crear array (actividades) ["Materia: " mat, "Tarea: " act, "Fecha: " fecha]

     Guardar array (actividades)

     Crear array (todaslastareas) [(actividades) 100]

     Fin subproceso



E0 (Bienvenida)

      escribir ("Hola que gusto volver a vernos/

      ¿Deseas ver tus tarea o agrgar tareas?/

      Para ver tus tareas digita 1 para agregar digita 2")

      input int <- (seleccion)

      mientras seleccion != 1 o 2

      escribir ("Opcion invalida, por favor ingrese 1 o 2")

      si seleccion = 1

      entonces ejecutar subproceso (vistatareas)

      si no seleccion = 2

      ejecutar subproceso (agregartarea)

      fin si
      

EF escribir ("gracias por organizarte con nosotros")
