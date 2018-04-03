# ROS Patterns
## Service / Client

This is an introduction practice for service and client

## Instructions:
1. Create a ros_package
	```
	$ catkin_create_pkg service_demo std_msgs rospy
	```
2. Copy the nodes from the nodes from the repository "service_demo/src/" into the src folder of the package created

3. Create a folder called srv. Inside the folder create a file called "two_ints.srv" (It can be a different name).
	```
	$ mkdir srv
	$ nano srv/two_int.srv
	```
4. In the service file create two int64 variables for the request and a int64 variable for the response
  ```
  Reference to slide number 5
  ```

5. Modify CMakeLists.txt file
  ```
  4.1 Inside find_package{catkin REQUIRED COMPONENTS} add message_generation,
	4.2 Uncomment add_service_files(Files ) and add the name of the service file <two_ints.srv>. (PS: < > not required).
	4.3 Uncomment generate_messages(DEPENDENCIES std_msgs).
  ```
6. Modify package.xml file
	```
	5.1 Uncomment the line <build_depend>message_generation</build_depend>.
	5.2 Uncommet the line <exec_depend>message_runtime</exec_depend>
	NOTE: To uncomment delete the <!-- -->.
	```
7. Complete the nodes inside src/ by following the instructions.
  ```
  Do not forget to make the nodes executable
  $ chmod +x server_demo.py
  $ chmod +x client_demo.py
  ```

8. Build the workspace
  ```
  $ catkin build
  Alternatively
  $ catkin_make
  ```
