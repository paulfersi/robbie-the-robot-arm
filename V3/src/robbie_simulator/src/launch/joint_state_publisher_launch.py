from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robbie_simulator',  
            executable='joint_state_publisher_gui',  
            name='joint_state_publisher_gui',
            output='screen'
        )
    ])
