#!/usr/bin/env python2
#Importante la primera linea para saber en environment

import rospy

#El codigo se ejecutara cuando se llame al ejecutable
if __name__ == "__main__":
    #Initialize the node
    rospy.init_node("test_node")
    rospy.loginfo("Test node initilized")

    # #Log levels
    # rospy.logdebug("Debug message")
    # rospy.loginfo("Hello from my test node")
    # rospy.logwarn("This is a warning")
    # rospy.logerr("This is an error")

    # rospy.sleep(1.0) #Tiempo en segundos

    rate = rospy.Rate(10) #Definimos una frecuencia (en herzios)

    while not rospy.is_shutdown(): #Mientras que no se mate el nodo
        rospy.loginfo("Hello guys")
        rate.sleep() #Se espera la frecuencia elegida antes de seguir