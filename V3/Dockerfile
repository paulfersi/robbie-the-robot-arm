# ros foxy uses ubuntu 20.04 to 
FROM ros:foxy

# Install gazebo and clean apt cache 
RUN apt-get update && apt-get install -y \
    ros-foxy-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/ \
    && vim \ 
    && tmux 

# Source ROS2 setup files
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

# creates workspace and copy the project
WORKDIR /ros2_ws
COPY ./src /ros2_ws/src
RUN . /opt/ros/foxy/setup.sh && colcon build

# Source the workspace setup files
RUN echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

# Set the entrypoint
CMD ["bash"]
