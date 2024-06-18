from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument(name='use_sim_time', default_value='true', description='Use simulation (Gazebo) clock if true'),
       #DeclareLaunchArgument('robot_description_path',default_value='$(find robbie_simulator)/src/urdf/robbie.urdf',description='Absolute path to robot urdf file'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}],
            arguments=[Command(['xacro ', LaunchConfiguration('robot_description_path')])]
        ),
        #Node(
       #    package='robbie_simulator',
        #   executable='joint_state_publisher_gui',
         #  name='joint_state_publisher_gui',
          # output='screen'
       # ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            output='screen',
            arguments=['-entity', 'robot', '-topic', 'robot_description'],
        )
    ])
