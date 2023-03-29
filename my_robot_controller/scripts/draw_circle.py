#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#Funcion de callback para tratar los mensajes recibidos del topic suscrito
#Podemos añadir el tipo de mensaje del callback (msg: Pose) para que luego sea mas facil tratarlo
def pose_callback(msg: Pose):
    rospy.loginfo("Actual pose of the robot: " + str(msg))

if __name__ == "__main__":
    rospy.init_node("draw_circle")
    rospy.loginfo("Draw circle node started")

    #Crear un publisher para los comandos de velocidad, con el tipo de mensaje y el tamanio de buffer
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(2)

    #Crear un subscriber para recibir los datos de la pose del robot, con su tipo y su funcion de callback
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    while not rospy.is_shutdown():
        #Se crea un objeto de la clase Twist para el mensaje que vamos a enviar, y se puede modificar uno a uno los param o directamente introducir los 2 
        #vectores que lo forman (linear y angular)
        msg = Twist()
        #Como queremos un circulo solo neceitamos vel lineal en x y angular en z
        msg.linear.x = 2.0
        msg.angular.z = 1.5
        
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Killing draw circle node...")

    #Aqui al final iria el rospy.spin() para dejar en otra hebra la ejecucion, pero como tenemos el bucle del shutdown en este caso no es necesario 
    #porque ya se queda en bucle infinito