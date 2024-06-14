This is the ROS workspace.

**docker build -t robbie_simulator .** When I am in the folder containing the dockerfile

**docker run -it --rm --name robbie_container robbie_simulator**


- **urdf** contsains the robot in unified robot description format

http://wiki.ros.org/urdf/XML/joint

## Run the simulation (inside or outside the docker if the pc has ros2 installed)

```
cd V3
colcon build
source install/setup.bash
```

Launch gazebo

```
ros2 launch my_robot_arm display.launch.py
```

Run the control node

```
ros2 run my_robot_arm move_robot_arm.py
```


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



