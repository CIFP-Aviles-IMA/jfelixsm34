El trabajo consiste en modificar el código base del brazo que originalmente estaba diseñado para C++ para trabajar con Arduino a programación en Python para trabajar con la Jetson Nano. 
El código y la idea original se obtuvo de [1]. 
Se adaptan las funciones y el resultado es el siguiente: 
Se importan las bibliotecas correspondientes sustituyendo las de C++ por sus homologas de Python y las necesarias para sustituir el Arduino por la nueva controladora y después se definen las variables. 
Se configura el setup. 
Se define el movimiento que debe hacer el robot con la función correspondiente que comparará el valor marcado por los potenciómetros y lo sustituirá por la correspondiente posición de los servomotores. 
Se configura la apertura y cierre de la pinza del robot, asignándole al pulsador de la controladora una entrada en la Jetson nano y programando sus condiciones de trabajo. 

Se crea un pull request el cual propone cambios que puedes hacer en tu main de un repositorio o ponerla en otra rama aparte. 
Tras una revisión se han detectado ciertos fallos en el programa los cuales han sido solucionados de la siguiente manera: 
Comparando ambos programas, se asignan los valores de entrada de los potenciómetros a las del variador. 
Esto es debido a la falta de entradas del tipo correspondiente (PWM) en la Jetson; también se asignan la salida de los distintos motores en la placa de variador. 
Como había ciertas funciones que no estaban muy claras se crea una sección de ayuda. 
Esta saldrá únicamente cuando se solicite la ayuda correspondiente para aclarar un poco el programa o para definir ciertas funciones de este. 

Bibliografía:
​​[1] https://www.printables.com/model/818975-compact-robot-arm-arduino-3d-printed. (s.f.). 
