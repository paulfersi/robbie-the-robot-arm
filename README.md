# Robbie 

The purpose of this repo is to store the codes for my cute little companion, Robbie the robotic arm. This project is still WIP (cause I don't have a lot of ideas or time to implement them).

I quickly gave up on designing the arm so I just took the basic 3d model from how to mechatronics(Link to STL files: https://cults3d.com/en/3d-model/various/arduino-based-robot-arm-howtomechatronics)



<p align="center">
  <img src="/images/main_robbie.png" width="500">
</p>
<p align="center">
  <img src="/images/buttons.png" width="500">
</p>

## V1

The v1 is made using an **Arduino Mega** and 6 buttons to control the robot in any direction. I wanted to put something else other than the gripper but I ended up putting nothing so all it can do is punch people I guess.

## V2

In the v2 I added an HTTP server and changed the board to an **Arduino Uno R4 Wifi**. The robot can be controlled via a web-ui.

## V3

The v3 features a simulated version of the robotic arm using ROS2 foxy and rviz2.

<p align="center">
  <img src="/images/simulation.png" width="500">
</p>



Sources: https://automaticaddison.com/how-to-load-a-urdf-file-into-rviz-ros-2/