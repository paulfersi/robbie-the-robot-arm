This is the ROS workspace.

## How it works

There are 2 launchers, one for the joint_state_publisher_gui node and one for the robot_state_publisher node(from another ros package)

## Launch

- ros2 launch robbie_simulator joint_state_publisher_launch.py
- ros2 launch robbie_simulator robot_description_launch.py

The second node publishes the **robbie.urdf** file on the topic **/robot_description**.
The robot joints can be controlled via the joint_state_publisher node that launches an UI made using tkinter.













# Personal notes

**docker build -t robbie_simulator .** When I am in the folder containing the dockerfile

**docker run -it --rm --name robbie_container robbie_simulator**

- robot_state_publisher, joint_state_publisher_gui and gazebo_ros are 3 packages included with ros. 

- **urdf** contsains the robot in unified robot description format

http://wiki.ros.org/urdf/XML/joint

## Run the simulation (inside or outside the docker if the pc has ros2 installed)


## Notes on the code

**DeclareLaunchArgument(name='use_sim_time', default_value='true', description='Use simulation (Gazebo) clock if true'),**
To know whether the nodes should use the clock from gazebo instead of the OS clock.


## Tests with docker

https://turgaykivrak.medium.com/running-gui-applications-using-docker-in-mac-linux-and-windows-b280c1fb52d0

TODO: Gazebo gui doesn't work. I need to implement X11 to access the gui via ssh

Una volta installato XQuartz per mac. 

docker run -it --rm \
  -e DISPLAY=host.docker.internal:0 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --name robbie_container robbie_simulator



