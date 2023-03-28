#!/usr/bin/env python3
#Importante la primera linea para saber en environment

import rospy

#El codigo se ejecutara cuando se llame al ejecutable
if __name__ == "__main__":
    #Initialize the node
    rospy.init_node("test_node")

    #Log levels
    rospy.logdebug("Debug message")
    rospy.loginfo("Hello from my test node")
    rospy.logwarn("This is a warning")
    rospy.logerr("This is an error")

    rospy.sleep(1.0) #Tiempo en segundos