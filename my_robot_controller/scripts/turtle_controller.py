#!/usr/bin/env python2
#Nodo que combina suscriptor y publicador con un spin. Funcionamiento: evita chocar contra la pared y usar servicios
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen #Para importar el tipo del servicio

previous_x = 0 #Vble para no llamar al servicio demasiadas veces

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("turtle1/set_pen", SetPen)
        #Podemos usar el proxy directamente y llamarlo con los args
        response = set_pen(r, g, b, width, off)
        #En este caso no devuelve nada, pero si fuese un servicio con salida se podria tratar
        #rospy.loginfo(response)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def pose_callback(pose):
    rospy.loginfo("Actual pose of the robot: " + str(pose))
    cmd = Twist()
    if pose.x > 9 or pose.y > 9 or pose.x < 2 or pose.y < 2:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 3.0
        cmd.angular.z = 0.0
    pub.publish(cmd)

    global previous_x
    if pose.x >= 5.5 and previous_x < 5.5:
        previous_x = pose.x
        rospy.loginfo("Setting colour to red")
        call_set_pen_service(255, 0, 0, 4, 0)
    elif pose.x < 5.5 and previous_x >= 5.5:
        previous_x = pose.x
        rospy.loginfo("Setting colour to green")
        call_set_pen_service(0, 255, 0, 4, 0)

if __name__ == "__main__":
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("turtle1/set_pen")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("turtle controller node started")

    rospy.spin()