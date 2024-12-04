#aki poneis el dokstrink k kerais
""" Programa de python para el control de un brazo robótico basado en uno ya hecho en c++

y se puede observar su trabajo en https://www.youtube.com/watch?v=AIsVlgopqJc&ab_channel=BuildSomeStuff
se puede conseguir todo su trabajo en esta pagina https://www.printables.com/model/818975-compact-robot-arm-arduino-3d-printed

El trabajo consiste en modificar el código base del brazo que originalmente estaba diseñado para C++ para trabajar con Arduino a programación en Python para trabajar con la Jetson Nano.
Se ha tenido que adaptar las funciones y el resultado es el siguiente:
Primero se importar las bibliotecas correspondientes y después se definen las variables.
El segundo paso, comparando ambos programas, ha sido asignar los valores a los pines correspondientes, al igual que en el ejercicio prestado ha hecho con el Arduino.
Se configura el setup y se relaciona los motores con los pines de la controladora.
Se el movimiento que debe hacer el robot con la función correspondiente.
Se asignan los motores con los potenciómetros correspondientes.
Se configura la apertura y cierre de la pinza del robot a la entrada de la jetson.

 """


#import Wire 
#import Adafruit_PWMServoDriver
import board 
import busio 
import Jetson.GPIO as GPIO
import adafruit_pca9685
import time
i2c = busio.I2C(board.SCL, board.SDA)
from adafruit_servokit import Servokit



#declaro variables
MIN_PULSE_WIDTH= 650
MAX_PULSE_WIDTH= 2350
FREQUENCY= 50

#Instancio el Driver del controlador
#Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
pwm = adafruit_pca9685.PCA9685(i2c)
Kit = Servokit(chanels=16)



#CONFIGURO EL SetUP
time.sleep(5)  
pwm.frequency = FREQUENCY 
GPIO.setmode(GPIO.BOARD)
#hand = pwm.channels[0]
hand        = adafruit_motor.servo.Servo(1) #cualkiera de las 2
wrist       = adafruit_motor.servo.Servo(2)
elbow       = adafruit_motor.servo.Servo(3) #el 0 es la salida se tienen k cambiar
shoulder    = adafruit_motor.servo.Servo(4)            #asignar los motores a los pines de la controladora
base        = adafruit_motor.servo.Servo(5)

potWrist    = adafruit_motor.servo.Servo(6)
potElbow    = adafruit_motor.servo.Servo(7)                                           #asignacion de los potenciometros
potShoulder = adafruit_motor.servo.Servo(8)
potBase     = adafruit_motor.servo.Servo(9)


pwm.setPWMFreq(FREQUENCY)
pwm.setPWM(32, 0, 90)               #posición de inicio del controlador
pwm.begin()
GPIO.setup(7, GPIO.IN) #chanel  tiene k ser un numero Tantas d esta linea como entradas activas


def moveMotor(controlIn, motorOut):

   """ Diferentes parametros del movimiento del motor
   :param pulse_wide: mapeo de la posición del motor
   :param pulse_width: (pulse_wide / 1000000 * FRECUENCY) * 4096
   :param potVal: valor analógico del potenciometro
   :return: envia señal al servomotor correspondiente.
   # pulse width(contolIn) es un numero entero
   # potVal(motorOut) es un valor generado con el movimiento que se intercambia entre los dos robots 
    """
   pulse_wide, pulse_width, potVal = -7
  
  #  potVal = analogRead(controlIn);  
   potVal = GPIO.imput(controlIn)

   pulse_wide = map(potVal, 800, 240, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH)
   pulse_width = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096)   


 #   pwm.setPWM(motorOut, 0, pulse_width);
   pwm = GPIO.PWM(motorOut, pulse_width)

while (True): 
  moveMotor(potWrist, wrist)
  
  moveMotor(potElbow, elbow)                #asignar los motores a sus correspondientes potenciometros
                                            
  moveMotor(potShoulder, shoulder)
  
  moveMotor(potBase, base)

 
  pushButton = GPIO.imput(7)
  if(pushButton == GPIO.LOW):
  
    pwm.setPWM(hand, 0, 180)                        #    //Keep Gripper closed when button is not pressed
    print("Grab")
  
  else:
  
    pwm.setPWM(hand, 0, 90)                         #    //Open Gripper when button is pressed
    print("Release")
  

GPIO.cleanup()




