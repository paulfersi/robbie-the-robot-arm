This is the ROS workspace.

**docker build -t robbie_simulator** When I am in the folder containing the dockerfile
**docker run -it --rm --name robbie_container robbie_simulator**


- **urdf** contsains the robot in unified robot description format

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
