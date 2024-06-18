import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_share = FindPackageShare(package='robbie_simulator').find('robbie_simulator')
 
    #path to the rviz file
    rviz_config_path = os.path.join(pkg_share, '/src/rviz/robbie.rviz')
 
    #path to the URDF file
    urdf_model_path = os.path.join(pkg_share, '/src/urdf/test_robot.xacro')

    urdf_model = LaunchConfiguration('urdf_model')
    rviz_config_file = LaunchConfiguration('rviz_config_file')

    # Declare the launch arguments  
    declare_urdf_model_path_cmd = DeclareLaunchArgument(
    name='urdf_model', 
    default_value=urdf_model_path, 
    description='Absolute path to urdf file')
     
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
    name='rviz_config_file',
    default_value=rviz_config_path,
    description='Full path to the RVIZ config')

    start_joint_state_publisher_cmd = Node(
    package='joint_state_publisher',
    executable='joint_state_publisher',
    name='joint_state_publisher')

    start_joint_state_publisher_gui_node = Node(
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    name='joint_state_publisher_gui')
 
  # Subscribe to the joint states of the robot, and publish the 3D pose of each link.
    start_robot_state_publisher_cmd = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{'use_sim_time': True, 
    'robot_description': Command(['xacro ', urdf_model])}],
    arguments=[urdf_model_path])

    start_robot_state_publisher_cmd = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{'use_sim_time': True, 
    'robot_description': Command(['xacro ', urdf_model])}],
    arguments=[urdf_model_path])

    start_rviz_cmd = Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    output='screen',
    arguments=['-d', rviz_config_file])

    ld = LaunchDescription()

    ld.add_action(declare_urdf_model_path_cmd)
    ld.add_action(declare_rviz_config_file_cmd)
    ld.add_action(start_joint_state_publisher_cmd)
    ld.add_action(start_joint_state_publisher_gui_node)

    #ld.add_action(start_robot_state_publisher_cmd)
    ld.add_action(start_rviz_cmd)

    return ld

