# ros foxy uses ubuntu 20.04 to 
FROM ros:foxy

# Install gazebo and clean apt cache 
RUN apt-get update && apt-get install -y \
    ros-foxy-gazebo-ros-pkgs \
    && rm -rf /var/lib/apt/lists/ 

# Source ROS2 setup files
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

# creates workspace and copies the src folder into the docker
WORKDIR /V3
COPY ./src /V3/src
RUN . /opt/ros/foxy/setup.sh && colcon build

# Source the workspace setup files
RUN echo "source /V3/install/setup.bash" >> ~/.bashrc

# Set the entrypoint
CMD ["bash"]
