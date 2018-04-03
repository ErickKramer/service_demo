#!/usr/bin/env python

#from ros_package.srv import srv_file
import rospy

class server:
    def __init__(self):
        #initialize the server node
        rospy.init_node("server_demo")

        #Display in the console the message
        rospy.loginfo("Server initiated")

        """
        Create the server
        Structure for server ->
            name_of_server = rospy.Service("service_label", service_name, \
                                        service_function)

        Create the server function where the response is processed

        Structure ->
            def name_server_function(request)

        Tasks:
        1. Add two numbers
        2. Multiply two numbers
        3. Substract two numbers
        4. Divide two numbers (Make sure to calculate exact values)
        5.

        HINT:
            -To access one of the components of the request write request.a for
            the request variable "a".
            -To return the operation result write return response
            -You could also return several operations. E.g. return a+b, c*d
        """



if __name__ == '__main__':
    n = server()

    rospy.spin()
